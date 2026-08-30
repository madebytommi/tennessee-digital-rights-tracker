#!/usr/bin/env python3
"""Apply only narrowly approved structural tracker repairs after validation fails."""

from __future__ import annotations

from datetime import date
import json
import os
from pathlib import Path
import re
import subprocess
import sys

import requests
from google import genai

MARKER = "<!-- gemini-safe-fix -->"
ROOT = Path(__file__).resolve().parents[1]
SAFE_HEADING = "Revision history"


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def upsert_comment(repo: str, pr_number: str, token: str, body: str) -> None:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    comments_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    response = requests.get(comments_url, headers=headers, timeout=30)
    response.raise_for_status()
    existing = next(
        (
            item
            for item in response.json()
            if MARKER in item.get("body", "")
            and item.get("user", {}).get("login") == "github-actions[bot]"
        ),
        None,
    )
    payload = {"body": f"{MARKER}\n### Gemini safe-fix\n\n{body}"}
    if existing:
        url = f"https://api.github.com/repos/{repo}/issues/comments/{existing['id']}"
        result = requests.patch(url, headers=headers, json=payload, timeout=30)
    else:
        result = requests.post(comments_url, headers=headers, json=payload, timeout=30)
    result.raise_for_status()


def normalize_repo_path(raw_path: str) -> str | None:
    normalized = raw_path.replace("\\", "/")
    for marker in ("/_entries/", "/_special_cases/"):
        if marker in normalized:
            return marker.lstrip("/") + normalized.split(marker, 1)[1]
    if normalized.startswith("_entries/") or normalized.startswith("_special_cases/"):
        return normalized
    return None


def parse_failures(log_text: str) -> tuple[list[str], list[str]]:
    safe_paths: list[str] = []
    unsafe: list[str] = []
    failure_lines = [line[2:] for line in log_text.splitlines() if line.startswith("- ")]

    for failure in failure_lines:
        match = re.fullmatch(r"(.+?): missing headings: (.+)", failure)
        if not match:
            unsafe.append(failure)
            continue
        path = normalize_repo_path(match.group(1))
        headings = {item.strip() for item in match.group(2).split(",") if item.strip()}
        if path and headings == {SAFE_HEADING}:
            safe_paths.append(path)
        else:
            unsafe.append(failure)

    if not failure_lines:
        unsafe.append("Validator output did not contain parseable failure lines.")
    return sorted(set(safe_paths)), unsafe


def gemini_confirms_safe(api_key: str, validator_output: str, safe_paths: list[str]) -> tuple[bool, str]:
    prompt = f"""Classify a proposed automated repository repair.

HARD POLICY: The only repair eligible for automatic mutation is adding a missing level-2 Markdown heading exactly named `Revision history` to tracker Markdown files under `_entries/` or `_special_cases/`. No factual, legal, policy, source, date, status, category, confidence, tag, URL, or substantive prose may be altered. You cannot expand this policy.

Validator output:
{validator_output[:12000]}

Paths already deterministically matched by the hard policy:
{json.dumps(safe_paths, indent=2)}

Return JSON only, with this exact shape:
{{"classification":"safe_structural" or "review_required","reason":"one short sentence"}}

Choose `review_required` if there is any doubt.
"""
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    text = (response.text or "").strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.DOTALL)
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return False, "Gemini did not return valid classification JSON."
    return parsed.get("classification") == "safe_structural", str(parsed.get("reason", "No reason supplied."))


def add_revision_history_heading(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if re.search(r"^##\s+Revision history\s*$", text, flags=re.MULTILINE):
        return
    repair_note = (
        f"- **{date.today().isoformat()}:** Automated structural repair: added the required "
        "Revision history section after repository validation flagged the heading as missing."
    )
    updated = text.rstrip() + f"\n\n## Revision history\n\n{repair_note}\n"
    path.write_text(updated, encoding="utf-8")


def run_validator() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "scripts/validate_entries.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    if len(sys.argv) != 2:
        raise RuntimeError("Usage: gemini_safe_fix.py <validator-log>")

    api_key = require_env("GEMINI_API_KEY")
    github_token = require_env("GITHUB_TOKEN")
    repo = require_env("REPO")
    pr_number = require_env("PR_NUMBER")
    validator_log = Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace")

    safe_paths, unsafe_failures = parse_failures(validator_log)
    if unsafe_failures or not safe_paths:
        summary = "No automatic edit was made because the validator reported an issue outside the allowlist."
        details = "\n".join(f"- `{item}`" for item in unsafe_failures[:20])
        upsert_comment(repo, pr_number, github_token, f"{summary}\n\n{details}")
        print(summary)
        return 0

    confirmed, reason = gemini_confirms_safe(api_key, validator_log, safe_paths)
    if not confirmed:
        message = f"No automatic edit was made. Gemini classified this as requiring human review.\n\nReason: {reason}"
        upsert_comment(repo, pr_number, github_token, message)
        print(message)
        return 0

    for relative in safe_paths:
        target = (ROOT / relative).resolve()
        if ROOT not in target.parents or not target.is_file():
            raise RuntimeError(f"Refusing unexpected path: {relative}")
        add_revision_history_heading(target)

    changed = subprocess.check_output(["git", "diff", "--name-only"], cwd=ROOT, text=True).splitlines()
    if set(changed) - set(safe_paths):
        raise RuntimeError(f"Refusing repair because unexpected files changed: {changed}")

    validation = run_validator()
    combined = (validation.stdout + "\n" + validation.stderr).strip()
    if validation.returncode != 0:
        subprocess.run(["git", "restore", "--", *safe_paths], cwd=ROOT, check=False)
        upsert_comment(
            repo,
            pr_number,
            github_token,
            "Gemini identified an allowlisted structural repair, but the repaired tree still failed validation. "
            "The edit was discarded and human review is required.\n\n```text\n"
            + combined[:8000]
            + "\n```",
        )
        return 0

    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], cwd=ROOT, check=True)
    subprocess.run(
        ["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(["git", "add", "--", *safe_paths], cwd=ROOT, check=True)
    subprocess.run(
        ["git", "commit", "-m", "chore: auto-fix safe tracker validation"],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(["git", "push"], cwd=ROOT, check=True)

    paths_text = "\n".join(f"- `{path}`" for path in safe_paths)
    upsert_comment(
        repo,
        pr_number,
        github_token,
        "Applied a narrowly allowlisted structural repair and reran the tracker validator successfully.\n\n"
        f"{paths_text}\n\nGemini classification: {reason}\n\nNo substantive factual or legal content was edited.",
    )
    print("Safe structural repair committed and pushed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Gemini safe-fix failed: {exc}", file=sys.stderr)
        raise
