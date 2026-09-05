"""Durable and practical duplicate detection for scout candidates."""

from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timezone
import json
import logging
from pathlib import Path
import re

from discovery.config import DEFAULT_SEEN_PATH
from discovery.entries import entry_identifiers, entry_search_blob
from discovery.textutil import canonicalize_url, collapse_ws, extract_bill_numbers, extract_public_chapters
from discovery.types import Candidate, SeenRecord, TrackerEntry

LOGGER = logging.getLogger("scout.dedupe")

SEEN_VERSION = 1
UPDATE_HINT_PREFIX = "UPDATE EXISTING:"


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def empty_state() -> dict:
    return {"version": SEEN_VERSION, "updated_at": None, "items": {}}


def load_seen(path: Path | None = None) -> dict:
    seen_path = path or DEFAULT_SEEN_PATH
    if not seen_path.exists():
        return empty_state()
    try:
        payload = json.loads(seen_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        LOGGER.warning("Could not read %s (%s); starting with empty seen state", seen_path, exc)
        return empty_state()
    if not isinstance(payload, dict) or "items" not in payload:
        LOGGER.warning("Seen state in %s is malformed; starting empty", seen_path)
        return empty_state()
    payload.setdefault("version", SEEN_VERSION)
    payload.setdefault("items", {})
    return payload


def save_seen(state: dict, path: Path | None = None) -> None:
    seen_path = path or DEFAULT_SEEN_PATH
    seen_path.parent.mkdir(parents=True, exist_ok=True)
    state = dict(state)
    state["version"] = SEEN_VERSION
    state["updated_at"] = _now()
    tmp = seen_path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(seen_path)


def record_to_item(record: SeenRecord) -> dict:
    payload = asdict(record)
    return payload


def mark_seen(state: dict, candidate: Candidate, status: str, **fields: object) -> None:
    now = _now()
    items: dict = state.setdefault("items", {})
    existing = items.get(candidate.candidate_id) or {}
    record = {
        "candidate_id": candidate.candidate_id,
        "url": candidate.url,
        "title": candidate.title,
        "source_id": candidate.source_id,
        "status": status,
        "first_seen": existing.get("first_seen") or now,
        "last_seen": now,
        "content_fingerprint": candidate.content_fingerprint,
        "issue_number": existing.get("issue_number"),
        "composite": existing.get("composite"),
        "suggested_action": existing.get("suggested_action"),
    }
    for key, value in fields.items():
        record[key] = value
    items[candidate.candidate_id] = record
    if candidate.content_fingerprint:
        items[f"fp:{candidate.content_fingerprint}"] = {
            "candidate_id": candidate.candidate_id,
            "status": "fingerprint-alias",
            "first_seen": now,
            "last_seen": now,
        }


def _fingerprints_match(stored: object, current: str) -> bool:
    stored_fp = str(stored or "")
    current_fp = current or ""
    return stored_fp == current_fp


def previously_processed(state: dict, candidate: Candidate) -> str | None:
    """Skip only identical discoveries, not later developments of the same item.

    Same candidate ID plus the same content fingerprint is a duplicate.
    Same candidate ID with a changed fingerprint is a new development.
    Identical content seen under another ID or URL is still a duplicate.
    """
    items = state.get("items") or {}
    current_fp = candidate.content_fingerprint or ""
    direct = items.get(candidate.candidate_id)
    if isinstance(direct, dict) and direct.get("status") not in {None, "fingerprint-alias"}:
        if _fingerprints_match(direct.get("content_fingerprint"), current_fp):
            return f"seen:{direct.get('status') or 'processed'}"
        return None
    if current_fp:
        alias = items.get(f"fp:{current_fp}")
        if isinstance(alias, dict):
            return "seen:content-fingerprint"
    candidate_url = canonicalize_url(candidate.url)
    if not candidate_url:
        return None
    for item in items.values():
        if not isinstance(item, dict):
            continue
        if item.get("status") == "fingerprint-alias":
            continue
        if canonicalize_url(str(item.get("url") or "")) != candidate_url:
            continue
        if item.get("candidate_id") == candidate.candidate_id:
            # Same ID with a changed fingerprint is handled above.
            continue
        if _fingerprints_match(item.get("content_fingerprint"), current_fp):
            return "seen:url"
    return None


def format_update_hint(entry: TrackerEntry, reason: str) -> str:
    return f"{UPDATE_HINT_PREFIX} {entry.slug} ({reason})"


def hint_entry_slug(hint: str | None) -> str | None:
    if not hint:
        return None
    text = hint.strip()
    if text.startswith(UPDATE_HINT_PREFIX):
        text = text[len(UPDATE_HINT_PREFIX):].strip()
    slug = text.split()[0] if text else ""
    return slug or None


def matching_hint(candidate: Candidate, entries: list[TrackerEntry]) -> str | None:
    match = match_existing_entry(candidate, entries)
    if not match:
        return None
    entry, reason = match
    return format_update_hint(entry, reason)


def triage_candidate(
    candidate: Candidate,
    seen: dict,
    entries: list[TrackerEntry],
    issue_index: list[dict],
) -> tuple[str | None, str | None]:
    """Return (skip_reason, update_hint).

    A skip_reason means the candidate should not be evaluated or surfaced.
    An update_hint means a published entry likely matches and should be
    passed to Gemini as an UPDATE EXISTING signal, not as a rejection.
    """
    seen_reason = previously_processed(seen, candidate)
    if seen_reason:
        return seen_reason, None
    existing_issue = existing_issue_for_candidate(candidate, issue_index)
    if existing_issue:
        number = existing_issue.get("number")
        return f"duplicate-issue:{number}", None
    return None, matching_hint(candidate, entries)


def _token_set(text: str) -> set[str]:
    return {token for token in re.findall(r"[a-z0-9]{3,}", collapse_ws(text).lower())}


def match_existing_entry(candidate: Candidate, entries: list[TrackerEntry]) -> tuple[TrackerEntry, str] | None:
    """Return a likely matching published entry when the overlap is practical."""
    candidate_blob = f"{candidate.title} {candidate.summary} {candidate.url}"
    candidate_ids = set(extract_bill_numbers(candidate_blob))
    candidate_ids.update(extract_public_chapters(candidate_blob))
    extra = candidate.extra or {}
    if extra.get("bill_number"):
        candidate_ids.add(str(extra["bill_number"]).upper().replace(" ", ""))
    candidate_url = canonicalize_url(candidate.url)
    candidate_tokens = _token_set(f"{candidate.title} {candidate.summary}")

    best: tuple[float, TrackerEntry, str] | None = None
    for entry in entries:
        entry_ids = entry_identifiers(entry)
        if candidate_url and candidate_url == entry.primary_source_url:
            return entry, "primary-source-url"
        if candidate_url and candidate_url in entry_search_blob(entry):
            return entry, "url-in-entry"
        shared_ids = candidate_ids & entry_ids
        if shared_ids:
            return entry, f"identifier:{sorted(shared_ids)[0]}"
        entry_tokens = _token_set(f"{entry.title} {entry.summary}")
        if not candidate_tokens or not entry_tokens:
            continue
        overlap = len(candidate_tokens & entry_tokens) / max(1, min(len(candidate_tokens), len(entry_tokens)))
        # Conservative title-ish overlap; used only as a hint, not automatic identity.
        if overlap >= 0.55 and len(candidate_tokens & entry_tokens) >= 6:
            score = overlap
            if best is None or score > best[0]:
                best = (score, entry, f"title-overlap:{overlap:.2f}")
    if best:
        return best[1], best[2]
    return None


def existing_issue_for_candidate(candidate: Candidate, issue_index: list[dict]) -> dict | None:
    candidate_url = canonicalize_url(candidate.url)
    marker = f"{candidate.candidate_id}"
    for issue in issue_index:
        body = str(issue.get("body") or "")
        title = str(issue.get("title") or "")
        if marker and marker in body:
            return issue
        if candidate_url and candidate_url in body:
            return issue
        if candidate.title and candidate.title.lower() in title.lower() and candidate.title:
            return issue
    return None
