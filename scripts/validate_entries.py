#!/usr/bin/env python3
"""Validate published Tracker entries and Special Cases."""

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
ENTRY_DIR = ROOT / "_entries"
SPECIAL_CASE_DIR = ROOT / "_special_cases"

ENTRY_REQUIRED_FIELDS = {
    "title",
    "date",
    "event_date",
    "last_reviewed",
    "status",
    "level",
    "category",
    "jurisdiction",
    "confidence",
    "summary",
    "primary_source_url",
    "primary_source_type",
    "tags",
}

SPECIAL_CASE_REQUIRED_FIELDS = {
    "title",
    "case_id",
    "date_opened",
    "last_reviewed",
    "scope_start",
    "status",
    "level",
    "category",
    "jurisdiction",
    "confidence",
    "summary",
    "tags",
}

ALLOWED_STATUS = {
    "Proposed", "Monitoring", "Active", "Blocked",
    "Enjoined", "Repealed", "Expired", "Resolved",
}

ALLOWED_LEVELS = {"Local", "State", "Federal", "Multi-level"}

ALLOWED_CATEGORIES = {
    "lgbtq-trans-policy",
    "government-surveillance",
    "health-data-privacy",
    "online-identity-age-verification",
    "government-ai-automation",
    "digital-civic-information",
    "election-systems-data",
}

ALLOWED_CONFIDENCE = {"High", "Medium", "Low"}

ENTRY_REQUIRED_HEADINGS = {
    "What happened?",
    "What the primary source says",
    "What is confirmed?",
    "What remains uncertain?",
    "Who may be affected?",
    "Privacy and civil-liberties significance",
    "Lawful actions and resources",
    "Sources",
    "Revision history",
}

SPECIAL_CASE_REQUIRED_HEADINGS = {
    "Case scope",
    "Tennessee nexus",
    "Current status",
    "Documented timeline",
    "How the pieces connect",
    "What is confirmed?",
    "What is not established?",
    "What remains uncertain?",
    "Digital-rights significance",
    "Update triggers",
    "Lawful actions and resources",
    "Sources",
    "Revision history",
}

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_markdown(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not match:
        raise ValueError("missing valid YAML front matter")
    metadata = yaml.safe_load(match.group(1)) or {}
    if not isinstance(metadata, dict):
        raise ValueError("front matter must be a mapping")
    return metadata, match.group(2)


def is_valid_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def as_date(value: object) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None


def validate_common(path: Path, metadata: dict, failures: list[str]) -> None:
    if metadata.get("status") not in ALLOWED_STATUS:
        failures.append(f"{path}: invalid status")
    if metadata.get("level") not in ALLOWED_LEVELS:
        failures.append(f"{path}: invalid level")
    if metadata.get("category") not in ALLOWED_CATEGORIES:
        failures.append(f"{path}: invalid category")
    if metadata.get("confidence") not in ALLOWED_CONFIDENCE:
        failures.append(f"{path}: invalid confidence")

    tags = metadata.get("tags")
    if not isinstance(tags, list) or not tags:
        failures.append(f"{path}: tags must be a non-empty list")


def validate_headings(
    path: Path,
    body: str,
    required: set[str],
    failures: list[str],
) -> None:
    headings = set(re.findall(r"^##\s+(.+?)\s*$", body, re.MULTILINE))
    absent = sorted(required - headings)
    if absent:
        failures.append(f"{path}: missing headings: {', '.join(absent)}")


def main() -> int:
    failures: list[str] = []
    entries: list[tuple[Path, dict]] = []
    special_cases: list[tuple[Path, dict]] = []

    entry_paths = [
        path for path in sorted(ENTRY_DIR.glob("*.md"))
        if path.name != "ENTRY_TEMPLATE.md"
    ]
    case_paths = sorted(SPECIAL_CASE_DIR.glob("*.md"))

    case_ids: dict[str, Path] = {}

    for path in case_paths:
        try:
            metadata, body = parse_markdown(path)
        except Exception as exc:
            failures.append(f"{path}: {exc}")
            continue

        special_cases.append((path, metadata))

        missing = sorted(SPECIAL_CASE_REQUIRED_FIELDS - metadata.keys())
        if missing:
            failures.append(f"{path}: missing fields: {', '.join(missing)}")

        validate_common(path, metadata, failures)
        validate_headings(path, body, SPECIAL_CASE_REQUIRED_HEADINGS, failures)

        case_id = metadata.get("case_id")
        if not isinstance(case_id, str) or not SLUG_RE.fullmatch(case_id):
            failures.append(f"{path}: case_id must be a lowercase hyphenated slug")
        elif case_id in case_ids:
            failures.append(
                f"{path}: duplicate case_id also used by {case_ids[case_id]}"
            )
        else:
            case_ids[case_id] = path

        opened = as_date(metadata.get("date_opened"))
        reviewed = as_date(metadata.get("last_reviewed"))
        scope_start = as_date(metadata.get("scope_start"))
        scope_end_raw = metadata.get("scope_end")
        scope_end = as_date(scope_end_raw) if scope_end_raw not in {None, ""} else None

        if opened is None:
            failures.append(f"{path}: date_opened must be an ISO date")
        if reviewed is None:
            failures.append(f"{path}: last_reviewed must be an ISO date")
        if scope_start is None:
            failures.append(f"{path}: scope_start must be an ISO date")
        if opened and reviewed and reviewed < opened:
            failures.append(f"{path}: last_reviewed cannot precede date_opened")
        if scope_start and scope_end and scope_end < scope_start:
            failures.append(f"{path}: scope_end cannot precede scope_start")

    related_counts = {case_id: 0 for case_id in case_ids}

    for path in entry_paths:
        try:
            metadata, body = parse_markdown(path)
        except Exception as exc:
            failures.append(f"{path}: {exc}")
            continue

        entries.append((path, metadata))

        missing = sorted(ENTRY_REQUIRED_FIELDS - metadata.keys())
        if missing:
            failures.append(f"{path}: missing fields: {', '.join(missing)}")

        validate_common(path, metadata, failures)
        validate_headings(path, body, ENTRY_REQUIRED_HEADINGS, failures)

        if not is_valid_url(metadata.get("primary_source_url")):
            failures.append(f"{path}: primary_source_url must be an http(s) URL")

        special_case_id = metadata.get("special_case_id")
        if special_case_id is not None:
            if not isinstance(special_case_id, str) or not SLUG_RE.fullmatch(special_case_id):
                failures.append(
                    f"{path}: special_case_id must be a lowercase hyphenated slug"
                )
            elif special_case_id not in case_ids:
                failures.append(
                    f"{path}: special_case_id does not match a published Special Case"
                )
            else:
                related_counts[special_case_id] += 1

    for case_id, count in related_counts.items():
        if count == 0:
            failures.append(
                f"{case_ids[case_id]}: published Special Case must have at least one related entry"
            )

    if failures:
        print("Tracker validation failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    entry_count = len(entries)
    case_count = len(special_cases)
    relationship_count = sum(related_counts.values())
    print(
        f"Validated {entry_count} published entr{'y' if entry_count == 1 else 'ies'}."
    )
    print(
        f"Validated {case_count} Special Case{'s' if case_count != 1 else ''}."
    )
    print(
        f"Validated {relationship_count} Special Case relationship"
        f"{'s' if relationship_count != 1 else ''}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
