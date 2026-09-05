from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from discovery.dedupe import load_seen, mark_seen, match_existing_entry, previously_processed, save_seen
from discovery.entries import load_tracker_entries
from discovery.types import Candidate, TrackerEntry


def _candidate(**overrides: object) -> Candidate:
    base = dict(
        candidate_id="tn-ga:114:HB1891",
        source_id="general-assembly",
        source_name="Tennessee General Assembly",
        title="HB1891: age verification for websites",
        url="https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB1891&ga=113",
        summary="Requires age verification.",
        extra={"bill_number": "HB1891"},
        matched_keywords=("age-identity-verification",),
        content_fingerprint="abc123",
    )
    base.update(overrides)
    return Candidate(**base)  # type: ignore[arg-type]


class DedupeTests(unittest.TestCase):
    def test_seen_roundtrip(self) -> None:
        candidate = _candidate()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "seen.json"
            state = load_seen(path)
            self.assertEqual(state["items"], {})
            mark_seen(state, candidate, "issue-created", issue_number=12)
            save_seen(state, path)
            reloaded = load_seen(path)
            self.assertEqual(previously_processed(reloaded, candidate), "seen:issue-created")

    def test_content_fingerprint_alias(self) -> None:
        first = _candidate()
        companion = _candidate(
            candidate_id="tn-ga:114:SB1234",
            title="SB1234: age verification for websites",
            url="https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=SB1234&ga=114",
        )
        state = {"version": 1, "items": {}}
        mark_seen(state, first, "below-threshold")
        self.assertEqual(previously_processed(state, companion), "seen:content-fingerprint")

    def test_matches_existing_entry_by_bill_number(self) -> None:
        entry = TrackerEntry(
            slug="2025-01-01-protect-tennessee-minors-age-verification",
            path="x.md",
            title="Tennessee requires age verification",
            summary="PTMA age verification.",
            category="online-identity-age-verification",
            tags=("age-verification",),
            primary_source_url="https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB1891&ga=113",
            body_excerpt="Public Chapter 899 implements HB1891.",
        )
        match = match_existing_entry(_candidate(), [entry])
        self.assertIsNotNone(match)
        assert match is not None
        self.assertEqual(match[0].slug, entry.slug)

    def test_loads_published_tracker_entries(self) -> None:
        entries = load_tracker_entries()
        self.assertGreaterEqual(len(entries), 1)
        self.assertTrue(any(entry.primary_source_url for entry in entries))
