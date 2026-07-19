#!/usr/bin/env python3
"""Validate required front matter and section headings for tracker entries."""

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
ENTRY_DIR = ROOT / "_entries"

REQUIRED_FIELDS = {
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
}

ALLOWED_CONFIDENCE = {"High", "Medium", "Low"}

REQUIRED_HEADINGS = {
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


def parse_entry(path: Path) -> tuple[dict, str]:
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


def main() -> int:
    failures: list[str] = []
    entries = [
        path for path in sorted(ENTRY_DIR.glob("*.md"))
        if path.name != "ENTRY_TEMPLATE.md"
    ]

    if not entries:
        print("No published entries found. Template-only scaffold is valid.")
        return 0

    for path in entries:
        try:
            metadata, body = parse_entry(path)
        except Exception as exc:
            failures.append(f"{path}: {exc}")
            continue

        missing = sorted(REQUIRED_FIELDS - metadata.keys())
        if missing:
            failures.append(f"{path}: missing fields: {', '.join(missing)}")

        if metadata.get("status") not in ALLOWED_STATUS:
            failures.append(f"{path}: invalid status")
        if metadata.get("level") not in ALLOWED_LEVELS:
            failures.append(f"{path}: invalid level")
        if metadata.get("category") not in ALLOWED_CATEGORIES:
            failures.append(f"{path}: invalid category")
        if metadata.get("confidence") not in ALLOWED_CONFIDENCE:
            failures.append(f"{path}: invalid confidence")
        if not is_valid_url(metadata.get("primary_source_url")):
            failures.append(f"{path}: primary_source_url must be an http(s) URL")

        tags = metadata.get("tags")
        if not isinstance(tags, list) or not tags:
            failures.append(f"{path}: tags must be a non-empty list")

        headings = set(re.findall(r"^##\s+(.+?)\s*$", body, re.MULTILINE))
        absent_headings = sorted(REQUIRED_HEADINGS - headings)
        if absent_headings:
            failures.append(
                f"{path}: missing headings: {', '.join(absent_headings)}"
            )

    if failures:
        print("Entry validation failed:\n")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Validated {len(entries)} published entr{'y' if len(entries) == 1 else 'ies'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
