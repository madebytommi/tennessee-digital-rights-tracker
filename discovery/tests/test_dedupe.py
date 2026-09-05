from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from discovery.dedupe import (
    hint_entry_slug,
    load_seen,
    mark_seen,
    match_existing_entry,
    previously_processed,
    save_seen,
    triage_candidate,
)
from discovery.entries import load_tracker_entries
from discovery.evaluate import build_prompt
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


def _entry() -> TrackerEntry:
    return TrackerEntry(
        slug="2025-01-01-protect-tennessee-minors-age-verification",
        path="x.md",
        title="Tennessee requires age verification",
        summary="PTMA age verification.",
        category="online-identity-age-verification",
        tags=("age-verification",),
        primary_source_url="https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB1891&ga=113",
        body_excerpt="Public Chapter 899 implements HB1891.",
    )


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

    def test_identical_previously_seen_bill_is_skipped(self) -> None:
        candidate = _candidate()
        state = {"version": 1, "items": {}}
        mark_seen(state, candidate, "below-threshold")
        skip_reason, hint = triage_candidate(candidate, state, [], [])
        self.assertEqual(skip_reason, "seen:below-threshold")
        self.assertIsNone(hint)

    def test_same_bill_with_changed_content_is_evaluated_again(self) -> None:
        original = _candidate(summary="As introduced, requires age verification.")
        updated = _candidate(
            summary="As enacted, requires age verification and parental consent.",
            content_fingerprint="def456",
        )
        state = {"version": 1, "items": {}}
        mark_seen(state, original, "below-threshold")
        self.assertIsNone(previously_processed(state, updated))
        skip_reason, hint = triage_candidate(updated, state, [_entry()], [])
        self.assertIsNone(skip_reason)
        self.assertIsNotNone(hint)
        assert hint is not None
        self.assertTrue(hint.startswith("UPDATE EXISTING:"))

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
        match = match_existing_entry(_candidate(), [_entry()])
        self.assertIsNotNone(match)
        assert match is not None
        self.assertEqual(match[0].slug, _entry().slug)

    def test_existing_entry_match_reaches_evaluation(self) -> None:
        candidate = _candidate()
        skip_reason, hint = triage_candidate(candidate, {"items": {}}, [_entry()], [])
        self.assertIsNone(skip_reason)
        self.assertIsNotNone(hint)

    def test_existing_entry_match_is_update_existing_hint(self) -> None:
        candidate = _candidate()
        skip_reason, hint = triage_candidate(candidate, {"items": {}}, [_entry()], [])
        self.assertIsNone(skip_reason)
        self.assertIsNotNone(hint)
        assert hint is not None
        self.assertTrue(hint.startswith("UPDATE EXISTING:"))
        self.assertIn(_entry().slug, hint)
        self.assertEqual(hint_entry_slug(hint), _entry().slug)
        prompt = build_prompt(candidate, [_entry()], hint)
        self.assertIn("UPDATE EXISTING", prompt)
        self.assertIn(_entry().slug, prompt)
        self.assertIn("strong signal", prompt)

    def test_duplicate_open_discovery_issue_is_suppressed(self) -> None:
        candidate = _candidate()
        issues = [
            {
                "number": 88,
                "title": "[Discovery] HB1891: age verification for websites",
                "body": (
                    "<!-- tennessee-rights-scout: tn-ga:114:HB1891 -->\n"
                    "https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB1891&ga=113"
                ),
            }
        ]
        skip_reason, hint = triage_candidate(candidate, {"items": {}}, [_entry()], issues)
        self.assertEqual(skip_reason, "duplicate-issue:88")
        self.assertIsNone(hint)

    def test_loads_published_tracker_entries(self) -> None:
        entries = load_tracker_entries()
        self.assertGreaterEqual(len(entries), 1)
        self.assertTrue(any(entry.primary_source_url for entry in entries))
