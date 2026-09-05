"""Tennessee Lookout RSS adapter."""

from __future__ import annotations

import logging

from discovery.http import FetchError, fetch_text
from discovery.keywords import match_topics_from_item
from discovery.rss import parse_rss_items
from discovery.textutil import canonicalize_url, content_fingerprint
from discovery.types import Candidate

LOGGER = logging.getLogger("scout.source.lookout")

FEED_URL = "https://tennesseelookout.com/feed/"


def parse_lookout_feed(xml_text: str) -> list[Candidate]:
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
                candidate_id=f"lookout:{content_fingerprint(url, title)}",
                source_id="lookout",
                source_name="Tennessee Lookout",
                title=title[:240],
                url=url,
                summary=(summary or title)[:1200],
                published_at=item.get("published_at"),
                extra={"document_kind": "news"},
                matched_keywords=topics,
                content_fingerprint=content_fingerprint(title, summary),
            )
        )
    return candidates


def fetch_lookout() -> list[Candidate]:
    try:
        xml_text = fetch_text(FEED_URL, accept="application/rss+xml, application/xml;q=0.9, */*;q=0.8")
    except FetchError as exc:
        LOGGER.warning("Tennessee Lookout feed fetch failed: %s", exc)
        return []
    candidates = parse_lookout_feed(xml_text)
    LOGGER.info("lookout produced %s keyword-matching candidate(s)", len(candidates))
    return candidates
