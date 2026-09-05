from __future__ import annotations

import unittest

from discovery.evaluate import parse_evaluation_payload, should_surface
from discovery.issue import format_issue_body, format_issue_title
from discovery.types import Candidate, Evaluation


class EvaluateTests(unittest.TestCase):
    def test_parse_json_inside_fence(self) -> None:
        text = """```json
{
  "tennessee_relevance": 0.9,
  "digital_rights_relevance": 0.8,
  "significance": 0.7,
  "source_quality": 0.85,
  "novelty": 0.6,
  "suggested_action": "NEW ENTRY",
  "confidence": "Medium",
  "matching_entry": null,
  "summary": "A bill would require age verification.",
  "why_it_matters": "It would create a statewide identity-check mandate.",
  "explanation": "Primary legislative source with a clear Tennessee nexus."
}
```"""
        evaluation = parse_evaluation_payload(text)
        self.assertEqual(evaluation.suggested_action, "NEW ENTRY")
        self.assertGreater(evaluation.composite, 0.7)
        self.assertTrue(should_surface(evaluation))

    def test_below_threshold_not_surfaced(self) -> None:
        evaluation = parse_evaluation_payload(
            """
            {
              "tennessee_relevance": 0.2,
              "digital_rights_relevance": 0.2,
              "significance": 0.2,
              "source_quality": 0.5,
              "novelty": 0.5,
              "suggested_action": "WATCH",
              "confidence": "Low",
              "matching_entry": "none",
              "summary": "Weak connection.",
              "why_it_matters": "Unclear.",
              "explanation": "Incidental mention."
            }
            """
        )
        self.assertFalse(should_surface(evaluation))
        self.assertIsNone(evaluation.matching_entry)

    def test_issue_body_contains_required_fields(self) -> None:
        candidate = Candidate(
            candidate_id="lookout:1",
            source_id="lookout",
            source_name="Tennessee Lookout",
            title="County expands Flock cameras",
            url="https://tennesseelookout.com/example",
            summary="ALPR expansion.",
            matched_keywords=("alpr-flock",),
        )
        evaluation = Evaluation(
            tennessee_relevance=0.9,
            digital_rights_relevance=0.9,
            significance=0.8,
            source_quality=0.7,
            novelty=0.8,
            composite=0.84,
            suggested_action="NEW ENTRY",
            confidence="Medium",
            matching_entry=None,
            summary="A county expanded Flock ALPRs.",
            why_it_matters="License-plate databases can affect location privacy.",
            explanation="Local news lead; needs primary records.",
        )
        body = format_issue_body(candidate, evaluation, matching_entry=None)
        title = format_issue_title(candidate)
        self.assertTrue(title.startswith("[Discovery]"))
        for needle in (
            "Source URL",
            "Short summary",
            "Relevance score",
            "Confidence",
            "Suggested action",
            "Possible matching tracker entry",
            "Why it may matter",
            "`NEW ENTRY`",
            "https://tennesseelookout.com/example",
        ):
            self.assertIn(needle, body)
