from __future__ import annotations

import unittest

from discovery.textutil import (
    canonicalize_url,
    content_fingerprint,
    extract_bill_numbers,
    parse_date,
    strip_html,
    within_lookback,
)


class TextutilTests(unittest.TestCase):
    def test_canonicalize_strips_tracking_and_normalizes_bills(self) -> None:
        url = (
            "https://WAPP.capitol.tn.gov/apps/BillInfo/Default"
            "?utm_source=x&BillNumber=sb0195&ga=114"
        )
        canonical = canonicalize_url(url)
        self.assertIn("BillNumber=SB0195", canonical)
        self.assertNotIn("utm_source", canonical)
        self.assertTrue(canonical.startswith("https://wapp.capitol.tn.gov"))

    def test_parse_ag_date(self) -> None:
        self.assertEqual(parse_date("Wednesday, August 26, 2026 | 08:35am"), "2026-08-26")

    def test_parse_rss_date(self) -> None:
        self.assertEqual(parse_date("Tue, 01 Sep 2026 16:00:33 +0000"), "2026-09-01")

    def test_strip_html_and_entities(self) -> None:
        self.assertEqual(strip_html("<p>vehicle&#x27;s driving data</p>"), "vehicle's driving data")

    def test_extract_bill_numbers(self) -> None:
        self.assertEqual(extract_bill_numbers("See HB 1891 and SB1891."), ("HB1891", "SB1891"))

    def test_companion_bills_share_content_fingerprint(self) -> None:
        abstract = "As introduced, enacts the PEEPS Act for historical location data."
        house = content_fingerprint("HB2608: Privacy - " + abstract, abstract)
        senate = content_fingerprint("SB2215: Privacy - " + abstract, abstract)
        self.assertEqual(house, senate)

    def test_lookback_window(self) -> None:
        self.assertTrue(within_lookback("2026-09-01", 21, today="2026-09-05"))
        self.assertFalse(within_lookback("2026-01-01", 21, today="2026-09-05"))
        self.assertTrue(within_lookback(None, 21, today="2026-09-05"))
