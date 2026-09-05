"""Tennessee General Assembly bill-search adapter."""

from __future__ import annotations

from datetime import date
import html as html_lib
import logging
import re
import time
from urllib.parse import quote_plus

from discovery.config import SOURCE_PAUSE_SECONDS
from discovery.http import FetchError, fetch_text
from discovery.keywords import LEGISLATIVE_SEARCH_TERMS, match_topics_from_item
from discovery.textutil import canonicalize_url, collapse_ws, content_fingerprint, strip_html
from discovery.types import Candidate

LOGGER = logging.getLogger("scout.source.general_assembly")

SEARCH_URL = (
    "https://wapp.capitol.tn.gov/apps/BillSearch/BillSearchAdvanced"
    "?terms={terms}&searchtype=bills"
)
BILL_INFO_BASE = "https://wapp.capitol.tn.gov/apps/BillInfo/Default"

ROW_RE = re.compile(
    r"<tr>\s*<td[^>]*>\s*<a href=\"([^\"]+)\"[^>]*>\s*"
    r"<span class=\"bill-number\">([^<]+)</span>.*?"
    r"<td[^>]*>\s*<a href=\"[^\"]+\"[^>]*>\s*(.*?)</a>",
    re.S | re.I,
)


def current_ga_number(today: date | None = None) -> int:
    """Return the Tennessee General Assembly number for a given date.

    Odd years start a new two-year assembly. The 114th began in 2025.
    """
    day = today or date.today()
    session_start_year = day.year if day.year % 2 == 1 else day.year - 1
    return 114 + (session_start_year - 2025) // 2


def parse_bill_search_html(html_text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for match in ROW_RE.finditer(html_text):
        url = canonicalize_url(html_lib.unescape(match.group(1)))
        bill_number = re.sub(r"\s+", "", strip_html(match.group(2)).upper())
        abstract_html = match.group(3)
        abstract = strip_html(abstract_html)
        subject = ""
        strong = re.search(r"<strong>([^<]+)</strong>", abstract_html, re.I)
        if strong:
            subject = strip_html(strong.group(1))
        if bill_number in seen:
            continue
        seen.add(bill_number)
        rows.append(
            {
                "bill_number": bill_number,
                "url": url,
                "subject": subject,
                "abstract": abstract,
            }
        )
    return rows


def _candidate_from_row(row: dict[str, str], ga: int) -> Candidate | None:
    bill_number = row["bill_number"]
    url = row["url"] or f"{BILL_INFO_BASE}?BillNumber={bill_number}&ga={ga}"
    url = canonicalize_url(url)
    if "BillNumber=" not in url:
        url = canonicalize_url(f"{BILL_INFO_BASE}?BillNumber={bill_number}&ga={ga}")
    title = collapse_ws(f"{bill_number}: {row['abstract']}" if row["abstract"] else bill_number)
    summary = row["abstract"]
    blob = f"{title} {summary} {row.get('subject', '')}"
    topics = match_topics_from_item(title, blob)
    if not topics:
        return None
    return Candidate(
        candidate_id=f"tn-ga:{ga}:{bill_number}",
        source_id="general-assembly",
        source_name="Tennessee General Assembly",
        title=title[:240],
        url=url,
        summary=summary[:1200],
        published_at=None,
        extra={
            "bill_number": bill_number,
            "ga": ga,
            "subject": row.get("subject") or "",
            "document_kind": "legislation",
        },
        matched_keywords=topics,
        content_fingerprint=content_fingerprint(title, summary),
    )


def fetch_general_assembly(*, search_terms: tuple[str, ...] | None = None) -> list[Candidate]:
    ga = current_ga_number()
    terms = search_terms or LEGISLATIVE_SEARCH_TERMS
    merged: dict[str, Candidate] = {}
    for term in terms:
        url = SEARCH_URL.format(terms=quote_plus(term))
        try:
            html_text = fetch_text(url)
        except FetchError as exc:
            LOGGER.warning("General Assembly search for %r failed: %s", term, exc)
            time.sleep(SOURCE_PAUSE_SECONDS)
            continue
        rows = parse_bill_search_html(html_text)
        LOGGER.info("general-assembly search %r returned %s row(s)", term, len(rows))
        for row in rows:
            candidate = _candidate_from_row(row, ga)
            if candidate is None:
                continue
            merged[candidate.candidate_id] = candidate
        time.sleep(SOURCE_PAUSE_SECONDS)
    LOGGER.info("general-assembly produced %s unique keyword-matching bill(s)", len(merged))
    return list(merged.values())
