"""Create GitHub issues for high-scoring scout candidates."""

from __future__ import annotations

import json
import logging
import os
import urllib.error
import urllib.parse
import urllib.request

from discovery.config import ISSUE_LABEL, ISSUE_MARKER_PREFIX, ISSUE_TITLE_PREFIX, USER_AGENT
from discovery.evaluate import should_surface
from discovery.types import Candidate, Evaluation

LOGGER = logging.getLogger("scout.issue")
API_VERSION = "2022-11-28"


class GitHubError(RuntimeError):
    pass


def _token() -> str:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        raise GitHubError("GITHUB_TOKEN is not set")
    return token


def _repo(explicit: str | None = None) -> str:
    repo = explicit or os.environ.get("GITHUB_REPOSITORY") or os.environ.get("REPO")
    if not repo or "/" not in repo:
        raise GitHubError("Repository was not provided (GITHUB_REPOSITORY or --repo)")
    return repo


def _request(method: str, url: str, token: str, payload: dict | None = None) -> object:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": API_VERSION,
        "User-Agent": USER_AGENT,
    }
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            raw = response.read()
            if not raw:
                return {}
            return json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise GitHubError(f"{method} {url} failed ({exc.code}): {detail[:500]}") from exc


def ensure_discovery_label(repo: str | None = None) -> None:
    token = _token()
    repository = _repo(repo)
    url = f"https://api.github.com/repos/{repository}/labels/{urllib.parse.quote(ISSUE_LABEL)}"
    try:
        _request("GET", url, token)
        return
    except GitHubError as exc:
        if "404" not in str(exc):
            LOGGER.warning("Could not check %s label: %s", ISSUE_LABEL, exc)
            return
    create_url = f"https://api.github.com/repos/{repository}/labels"
    try:
        _request(
            "POST",
            create_url,
            token,
            {
                "name": ISSUE_LABEL,
                "color": "0E8A16",
                "description": "Automated Tennessee Rights Scout lead for human review. Not a published entry.",
            },
        )
        LOGGER.info("Created GitHub label '%s'", ISSUE_LABEL)
    except GitHubError as exc:
        LOGGER.warning("Could not create %s label: %s", ISSUE_LABEL, exc)


def list_discovery_issues(repo: str | None = None) -> list[dict]:
    token = _token()
    repository = _repo(repo)
    issues: list[dict] = []
    page = 1
    while page <= 5:
        query = urllib.parse.urlencode(
            {
                "state": "open",
                "labels": ISSUE_LABEL,
                "per_page": 100,
                "page": page,
            }
        )
        url = f"https://api.github.com/repos/{repository}/issues?{query}"
        try:
            payload = _request("GET", url, token)
        except GitHubError as exc:
            LOGGER.warning("Could not list discovery issues: %s", exc)
            break
        if not isinstance(payload, list) or not payload:
            break
        for item in payload:
            if isinstance(item, dict) and "pull_request" not in item:
                issues.append(item)
        if len(payload) < 100:
            break
        page += 1
    LOGGER.info("Loaded %s open GitHub issue(s) labeled %s", len(issues), ISSUE_LABEL)
    return issues


def format_issue_title(candidate: Candidate) -> str:
    title = candidate.title.strip()
    if len(title) > 180:
        title = title[:177].rstrip() + "..."
    prefix = f"{ISSUE_TITLE_PREFIX} "
    if title.startswith(ISSUE_TITLE_PREFIX):
        return title[:250]
    return f"{prefix}{title}"[:250]


def format_issue_body(
    candidate: Candidate,
    evaluation: Evaluation,
    *,
    matching_entry: str | None,
) -> str:
    scores = (
        f"- Tennessee relevance: {evaluation.tennessee_relevance:.2f}\n"
        f"- Digital/civil-rights relevance: {evaluation.digital_rights_relevance:.2f}\n"
        f"- Significance: {evaluation.significance:.2f}\n"
        f"- Source quality: {evaluation.source_quality:.2f}\n"
        f"- Novelty: {evaluation.novelty:.2f}\n"
        f"- Composite: {evaluation.composite:.2f}"
    )
    keywords = ", ".join(candidate.matched_keywords) or "none recorded"
    matching = matching_entry or evaluation.matching_entry or "none identified"
    extra_bits = []
    for key in ("bill_number", "docket_number", "court", "document_kind"):
        value = (candidate.extra or {}).get(key)
        if value:
            extra_bits.append(f"- {key.replace('_', ' ')}: `{value}`")
    extra = "\n".join(extra_bits) if extra_bits else "- none"
    return f"""{ISSUE_MARKER_PREFIX} {candidate.candidate_id} -->

This issue was opened by the Tennessee Rights Scout. It is a **discovery lead for human review**, not a published Tracker entry and not evidence.

Do not copy this text into `_entries/` without independent research under `docs/research-protocol.md`. Gemini scoring is a triage aid, not a source.

## Title
{candidate.title}

## Source
{candidate.source_name} (`{candidate.source_id}`)

## Source URL
{candidate.url}

## Short summary
{evaluation.summary or candidate.summary}

## Relevance score
{scores}

## Confidence
{evaluation.confidence}

## Suggested action
`{evaluation.suggested_action}`

## Possible matching tracker entry
{matching}

## Why it may matter
{evaluation.why_it_matters or evaluation.explanation or "Not provided."}

## Scoring notes
{evaluation.explanation or "Not provided."}

## Scout metadata
- Candidate ID: `{candidate.candidate_id}`
- Published / filed date: {candidate.published_at or "unknown"}
- Keyword topics: {keywords}
{extra}

## Human review checklist
- [ ] Open the source URL and inspect the underlying record
- [ ] Search existing entries, Special Cases, and issues
- [ ] Confirm Tennessee nexus and digital-rights relevance
- [ ] Separate documented facts from claims and analysis
- [ ] If it belongs in the Tracker, follow `templates/ENTRY_TEMPLATE.md` — do not auto-publish
"""


def create_discovery_issue(
    candidate: Candidate,
    evaluation: Evaluation,
    *,
    matching_entry: str | None = None,
    repo: str | None = None,
    dry_run: bool = False,
) -> dict | None:
    if not should_surface(evaluation):
        LOGGER.info("Skipping issue for %s; score below threshold", candidate.candidate_id)
        return None
    title = format_issue_title(candidate)
    body = format_issue_body(candidate, evaluation, matching_entry=matching_entry)
    if dry_run:
        LOGGER.info("DRY RUN would open issue: %s", title)
        return {"title": title, "body": body, "dry_run": True}
    token = _token()
    repository = _repo(repo)
    url = f"https://api.github.com/repos/{repository}/issues"
    payload = _request(
        "POST",
        url,
        token,
        {"title": title, "body": body, "labels": [ISSUE_LABEL]},
    )
    if not isinstance(payload, dict):
        raise GitHubError("GitHub issue response was not an object")
    number = payload.get("number")
    html_url = payload.get("html_url")
    LOGGER.info("Opened GitHub issue #%s %s", number, html_url)
    return payload
