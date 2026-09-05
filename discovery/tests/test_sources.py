from __future__ import annotations

from pathlib import Path
import unittest

from discovery.sources.aclu_tn import parse_aclu_feed
from discovery.sources.attorney_general import parse_news_html, parse_opinions_html
from discovery.sources.courtlistener import parse_courtlistener_results
from discovery.sources.general_assembly import current_ga_number, parse_bill_search_html
from discovery.sources.lookout import parse_lookout_feed
from datetime import date

FIXTURES = Path(__file__).resolve().parent / "fixtures"


class SourceParserTests(unittest.TestCase):
    def test_bill_search_parser(self) -> None:
        html = (FIXTURES / "bill_search.html").read_text(encoding="utf-8")
        rows = parse_bill_search_html(html)
        self.assertEqual(rows[0]["bill_number"], "SB0195")
        self.assertIn("driving data", rows[0]["abstract"])
        self.assertEqual(len(rows), 2)

    def test_ga_number_for_2026(self) -> None:
        self.assertEqual(current_ga_number(date(2026, 9, 5)), 114)
        self.assertEqual(current_ga_number(date(2025, 1, 14)), 114)
        self.assertEqual(current_ga_number(date(2027, 2, 1)), 115)

    def test_ag_news_keeps_digital_rights_item(self) -> None:
        html = (FIXTURES / "ag_news.html").read_text(encoding="utf-8")
        items = parse_news_html(html)
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]["published_at"], "2026-08-26")
        self.assertTrue(items[0]["url"].endswith("/pr26-33.html"))

    def test_ag_opinions_parser(self) -> None:
        html = (FIXTURES / "ag_opinions.html").read_text(encoding="utf-8")
        items = parse_opinions_html(html)
        self.assertEqual(items[0]["opinion_number"], "Opinion No. 26-06")
        self.assertIn("Social-Media", items[0]["title"])

    def test_lookout_feed_filters_keywords(self) -> None:
        xml_text = (FIXTURES / "rss.xml").read_text(encoding="utf-8")
        candidates = parse_lookout_feed(xml_text)
        self.assertEqual(len(candidates), 1)
        self.assertIn("Flock", candidates[0].title)
        self.assertIn("alpr-flock", candidates[0].matched_keywords)

    def test_aclu_feed_parser_uses_same_rss_helper(self) -> None:
        xml_text = (FIXTURES / "rss.xml").read_text(encoding="utf-8")
        candidates = parse_aclu_feed(xml_text)
        self.assertEqual(len(candidates), 1)

    def test_courtlistener_parser_requires_keyword_match(self) -> None:
        payload = {
            "results": [
                {
                    "absolute_url": "/opinion/1/netchoice-v-skrmetti/",
                    "caseName": "NetChoice v. Skrmetti",
                    "docketNumber": "24-1234",
                    "court": "Court of Appeals for the Sixth Circuit",
                    "court_id": "ca6",
                    "dateFiled": "2026-08-28",
                    "cluster_id": 99,
                    "opinions": [{"snippet": "Tennessee age verification law for social media"}],
                },
                {
                    "absolute_url": "/opinion/2/united-states-v-smith/",
                    "caseName": "United States v. Smith",
                    "docketNumber": "24-1",
                    "court": "Court of Appeals for the Sixth Circuit",
                    "court_id": "ca6",
                    "dateFiled": "2026-08-28",
                    "cluster_id": 100,
                    "opinions": [{"snippet": "sentencing guidelines in a drug case"}],
                },
            ]
        }
        candidates = parse_courtlistener_results(payload)
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0].candidate_id, "cl:99")
        self.assertIn("age-identity-verification", candidates[0].matched_keywords)
