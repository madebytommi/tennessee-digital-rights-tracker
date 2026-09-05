from __future__ import annotations

import unittest

from discovery.discover import collapse_same_content, prioritize
from discovery.types import Candidate


def _candidate(**overrides: object) -> Candidate:
    base = dict(
        candidate_id="lookout:new",
        source_id="lookout",
        source_name="Tennessee Lookout",
        title="County expands Flock cameras",
        url="https://tennesseelookout.com/example",
        summary="ALPR expansion.",
        published_at="2026-09-01",
        matched_keywords=("alpr-flock",),
        content_fingerprint="fp-new",
    )
    base.update(overrides)
    return Candidate(**base)  # type: ignore[arg-type]


def _ids(candidates: list[Candidate]) -> list[str]:
    return [item.candidate_id for item in candidates]


def _update_hint(slug: str) -> str:
    return f"UPDATE EXISTING: {slug} (identifier:HB1891)"


class PrioritizeTests(unittest.TestCase):
    def test_update_existing_candidates_are_placed_before_new_candidates(self) -> None:
        older_update = _candidate(
            candidate_id="tn-ga:114:HB1891",
            published_at="2025-01-15",
            content_fingerprint="fp-hb1891",
        )
        newer_lead = _candidate(
            candidate_id="lookout:flock",
            published_at="2026-09-04",
            content_fingerprint="fp-flock",
        )
        hints = {older_update.candidate_id: _update_hint("ptma")}
        ordered = prioritize([newer_lead, older_update], hints)
        self.assertEqual(_ids(ordered), ["tn-ga:114:HB1891", "lookout:flock"])

    def test_update_candidates_survive_max_evaluate_cutoff(self) -> None:
        updates = [
            _candidate(
                candidate_id=f"tn-ga:114:HB{i}",
                published_at="2025-02-01",
                content_fingerprint=f"fp-update-{i}",
            )
            for i in (1891, 1234, 999)
        ]
        new_leads = [
            _candidate(
                candidate_id=f"lookout:{i:02d}",
                published_at=f"2026-09-{i:02d}",
                content_fingerprint=f"fp-new-{i}",
            )
            for i in range(30, 0, -1)
        ]
        mixed = new_leads + updates
        hints = {item.candidate_id: _update_hint("entry") for item in updates}
        date_only = prioritize(mixed)
        self.assertNotIn("tn-ga:114:HB1891", _ids(date_only[:25]))

        ordered = prioritize(mixed, hints)
        selected = ordered[:25]
        self.assertEqual(
            _ids(selected)[:3],
            ["tn-ga:114:HB1891", "tn-ga:114:HB1234", "tn-ga:114:HB999"],
        )
        self.assertTrue(all(item.candidate_id.startswith("tn-ga:") for item in selected[:3]))
        self.assertEqual(len(selected), 25)

    def test_dated_non_update_candidates_remain_newest_first_after_updates(self) -> None:
        update = _candidate(
            candidate_id="tn-ga:114:HB1891",
            published_at="2024-03-01",
            content_fingerprint="fp-update",
        )
        older = _candidate(candidate_id="lookout:older", published_at="2026-08-01", content_fingerprint="fp-old")
        newer = _candidate(candidate_id="lookout:newer", published_at="2026-09-04", content_fingerprint="fp-new")
        hints = {update.candidate_id: _update_hint("ptma")}
        ordered = prioritize([older, update, newer], hints)
        self.assertEqual(_ids(ordered), ["tn-ga:114:HB1891", "lookout:newer", "lookout:older"])

    def test_undated_candidates_remain_after_dated_candidates(self) -> None:
        update = _candidate(
            candidate_id="tn-ga:114:HB1891",
            published_at="2024-03-01",
            content_fingerprint="fp-update",
        )
        dated = _candidate(candidate_id="lookout:dated", published_at="2026-09-01", content_fingerprint="fp-dated")
        undated = _candidate(
            candidate_id="lookout:undated",
            published_at=None,
            content_fingerprint="fp-undated",
        )
        hints = {update.candidate_id: _update_hint("ptma")}
        ordered = prioritize([undated, dated, update], hints)
        self.assertEqual(_ids(ordered), ["tn-ga:114:HB1891", "lookout:dated", "lookout:undated"])

    def test_undated_update_still_precedes_new_dated_leads(self) -> None:
        undated_update = _candidate(
            candidate_id="tn-ga:114:HB1891",
            published_at=None,
            content_fingerprint="fp-update",
        )
        dated_new = _candidate(
            candidate_id="lookout:dated",
            published_at="2026-09-04",
            content_fingerprint="fp-dated",
        )
        hints = {undated_update.candidate_id: _update_hint("ptma")}
        ordered = prioritize([dated_new, undated_update], hints)
        self.assertEqual(_ids(ordered), ["tn-ga:114:HB1891", "lookout:dated"])

    def test_deterministic_ordering_is_preserved(self) -> None:
        first_update = _candidate(
            candidate_id="tn-ga:114:HB1891",
            published_at="2025-01-01",
            content_fingerprint="fp-u1",
        )
        second_update = _candidate(
            candidate_id="tn-ga:114:SB1891",
            published_at="2025-01-01",
            content_fingerprint="fp-u2",
        )
        first_new = _candidate(
            candidate_id="lookout:a",
            published_at="2026-09-01",
            content_fingerprint="fp-a",
        )
        second_new = _candidate(
            candidate_id="lookout:b",
            published_at="2026-09-01",
            content_fingerprint="fp-b",
        )
        hints = {
            first_update.candidate_id: _update_hint("ptma"),
            second_update.candidate_id: _update_hint("ptma"),
        }
        # Same timestamps within each group: keep incoming relative order.
        incoming = [second_update, first_update, first_new, second_new]
        ordered = prioritize(incoming, hints)
        self.assertEqual(
            _ids(ordered),
            ["tn-ga:114:SB1891", "tn-ga:114:HB1891", "lookout:a", "lookout:b"],
        )
        again = prioritize(incoming, hints)
        self.assertEqual(_ids(ordered), _ids(again))

    def test_without_hints_dated_items_stay_newest_first(self) -> None:
        older = _candidate(candidate_id="lookout:older", published_at="2026-01-01")
        newer = _candidate(candidate_id="lookout:newer", published_at="2026-09-01")
        undated = _candidate(candidate_id="lookout:undated", published_at=None)
        self.assertEqual(
            _ids(prioritize([undated, older, newer])),
            ["lookout:newer", "lookout:older", "lookout:undated"],
        )


class CollapseTests(unittest.TestCase):
    def test_same_content_collapse_prefers_update_existing_candidate(self) -> None:
        non_update = _candidate(
            candidate_id="tn-ga:114:SB1891",
            title="SB1891: age verification for websites",
            content_fingerprint="same-bill",
        )
        update = _candidate(
            candidate_id="tn-ga:114:HB1891",
            title="HB1891: age verification for websites",
            content_fingerprint="same-bill",
        )
        hints = {update.candidate_id: _update_hint("ptma")}
        collapsed = collapse_same_content([non_update, update], hints)
        self.assertEqual(_ids(collapsed), ["tn-ga:114:HB1891"])

    def test_same_content_keeps_first_when_both_are_updates(self) -> None:
        first = _candidate(candidate_id="tn-ga:114:HB1891", content_fingerprint="same-bill")
        second = _candidate(candidate_id="tn-ga:114:SB1891", content_fingerprint="same-bill")
        hints = {
            first.candidate_id: _update_hint("ptma"),
            second.candidate_id: _update_hint("ptma"),
        }
        collapsed = collapse_same_content([first, second], hints)
        self.assertEqual(_ids(collapsed), ["tn-ga:114:HB1891"])

    def test_same_content_keeps_first_when_neither_is_update(self) -> None:
        first = _candidate(candidate_id="lookout:one", content_fingerprint="same-story")
        second = _candidate(candidate_id="aclu:one", content_fingerprint="same-story")
        collapsed = collapse_same_content([first, second], {})
        self.assertEqual(_ids(collapsed), ["lookout:one"])

    def test_collapse_then_prioritize_keeps_update_inside_max_evaluate(self) -> None:
        update = _candidate(
            candidate_id="tn-ga:114:HB1891",
            published_at="2025-01-01",
            content_fingerprint="same-bill",
        )
        companion = _candidate(
            candidate_id="tn-ga:114:SB1891",
            published_at="2026-09-04",
            content_fingerprint="same-bill",
        )
        newer_leads = [
            _candidate(
                candidate_id=f"lookout:{i:02d}",
                published_at=f"2026-08-{i:02d}",
                content_fingerprint=f"fp-{i}",
            )
            for i in range(1, 26)
        ]
        hints = {update.candidate_id: _update_hint("ptma")}
        incoming = [companion, *newer_leads, update]
        collapsed = collapse_same_content(incoming, hints)
        ordered = prioritize(collapsed, hints)
        self.assertEqual(ordered[0].candidate_id, "tn-ga:114:HB1891")
        self.assertNotIn("tn-ga:114:SB1891", _ids(ordered))
        self.assertIn("tn-ga:114:HB1891", _ids(ordered[:25]))
