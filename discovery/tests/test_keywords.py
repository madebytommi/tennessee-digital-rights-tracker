from __future__ import annotations

import unittest

from discovery.keywords import is_relevant, match_topics, match_topics_from_item


class KeywordTests(unittest.TestCase):
    def test_matches_alpr_and_privacy_topics(self) -> None:
        topics = match_topics(
            "Greenbrier Police Department expanded Flock Safety automated license plate readers."
        )
        self.assertIn("alpr-flock", topics)

    def test_matches_age_verification(self) -> None:
        topics = match_topics("The bill would require age verification for social media accounts.")
        self.assertIn("age-identity-verification", topics)
        self.assertIn("social-media-regulation", topics)

    def test_does_not_match_ordinary_news(self) -> None:
        self.assertFalse(is_relevant("The Titans won on Sunday after a late field goal."))

    def test_ai_token_does_not_match_aid(self) -> None:
        self.assertNotIn("ai-automation", match_topics("The agency will provide financial aid."))
        self.assertIn("ai-automation", match_topics("The state is procuring an AI eligibility system."))

    def test_matches_platform_child_safety_settlement(self) -> None:
        topics = match_topics(
            "Settlement with Meta Platforms, Inc. requires safety features to protect children on Instagram and Facebook."
        )
        self.assertIn("social-media-regulation", topics)

    def test_item_matcher_ignores_late_share_widget_text(self) -> None:
        title = "After decades of overhunting, black bears return"
        summary = "Wildlife biologists counted more bears this year." + (" padding" * 80) + " Share on Facebook YouTube Instagram"
        self.assertEqual(match_topics_from_item(title, summary), ())
