"""ACLU of Tennessee press-release adapter."""

from __future__ import annotations

import logging

from discovery.http import FetchError, fetch_text
from discovery.keywords import match_topics_from_item
from discovery.rss import parse_rss_items
from discovery.textutil import canonicalize_url, content_fingerprint
from discovery.types import Candidate

LOGGER = logging.getLogger("scout.source.aclu_tn")

FEED_URL = "https://www.aclu-tn.org/press-releases/feed/"


def parse_aclu_feed(xml_text: str) -> list[Candidate]:
    candidates: list[Candidate] = []
    for item in parse_rss_items(xml_text):
        title = item.get("title") or ""
        url = canonicalize_url(item.get("url") or "")
        summary = item.get("summary") or ""
        if not title or not url:
            continue
        topics = match_topics_from_item(title, summary)
        if not topics:
            continue
        candidates.append(
            Candidate(
                candidate_id=f"aclu-tn:{content_fingerprint(url, title)}",
                source_id="aclu-tn",
                source_name="ACLU of Tennessee",
                title=title[:240],
                url=url,
                summary=(summary or title)[:1200],
                published_at=item.get("published_at"),
                extra={"document_kind": "press-release"},
                matched_keywords=topics,
                content_fingerprint=content_fingerprint(title, summary),
            )
        )
    return candidates


def fetch_aclu_tn() -> list[Candidate]:
    try:
        xml_text = fetch_text(FEED_URL, accept="application/rss+xml, application/xml;q=0.9, */*;q=0.8")
    except FetchError as exc:
        LOGGER.warning("ACLU of Tennessee feed fetch failed: %s", exc)
        return []
    candidates = parse_aclu_feed(xml_text)
    LOGGER.info("aclu-tn produced %s keyword-matching candidate(s)", len(candidates))
    return candidates
