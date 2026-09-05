"""Load published Tracker entries for practical duplicate matching."""

from __future__ import annotations

from pathlib import Path
import re

import yaml

from discovery.config import ENTRY_DIR, SPECIAL_CASE_DIR
from discovery.textutil import canonicalize_url, extract_bill_numbers, extract_public_chapters, strip_html
from discovery.types import TrackerEntry

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.S)


def _parse_markdown(path: Path) -> TrackerEntry | None:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None
    metadata = yaml.safe_load(match.group(1)) or {}
    if not isinstance(metadata, dict):
        return None
    body = match.group(2)
    tags = metadata.get("tags") or []
    if not isinstance(tags, list):
        tags = [str(tags)]
    return TrackerEntry(
        slug=path.stem,
        path=str(path),
        title=str(metadata.get("title") or path.stem),
        summary=str(metadata.get("summary") or ""),
        category=str(metadata.get("category") or ""),
        tags=tuple(str(tag) for tag in tags),
        primary_source_url=canonicalize_url(str(metadata.get("primary_source_url") or "")),
        body_excerpt=strip_html(body)[:4000],
    )


def load_tracker_entries(root: Path | None = None) -> list[TrackerEntry]:
    base_entries = ENTRY_DIR if root is None else root / "_entries"
    base_cases = SPECIAL_CASE_DIR if root is None else root / "_special_cases"
    records: list[TrackerEntry] = []
    for directory in (base_entries, base_cases):
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            parsed = _parse_markdown(path)
            if parsed is not None:
                records.append(parsed)
    return records


def entry_search_blob(entry: TrackerEntry) -> str:
    return " ".join(
        [
            entry.slug,
            entry.title,
            entry.summary,
            entry.category,
            " ".join(entry.tags),
            entry.primary_source_url,
            entry.body_excerpt,
        ]
    )


def entry_identifiers(entry: TrackerEntry) -> set[str]:
    blob = entry_search_blob(entry)
    ids = set(extract_bill_numbers(blob))
    ids.update(extract_public_chapters(blob))
    if entry.primary_source_url:
        ids.add(entry.primary_source_url)
    return ids
