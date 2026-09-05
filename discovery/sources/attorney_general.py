"""Tennessee Attorney General news and opinion adapter."""

from __future__ import annotations

from datetime import date
import logging
import re
from urllib.parse import urljoin

from discovery.http import FetchError, fetch_text
from discovery.keywords import match_topics_from_item
from discovery.textutil import canonicalize_url, content_fingerprint, parse_date, strip_html
from discovery.types import Candidate

LOGGER = logging.getLogger("scout.source.attorney_general")

NEWS_URL = "https://www.tn.gov/attorneygeneral/news.html"
OPINIONS_INDEX = "https://www.tn.gov/attorneygeneral/opinions.html"
TN_ORIGIN = "https://www.tn.gov"

NEWS_RE = re.compile(
    r'<article class="news"[^>]*>.*?'
    r'<div class="title">\s*<a href="([^"]+)"[^>]*>(.*?)</a>.*?'
    r'<div class="date">(.*?)</div>.*?'
    r'<div class="text">\s*(.*?)\s*</div>',
    re.S | re.I,
)
OPINION_RE = re.compile(
    r'<li>\s*<a[^>]+href="([^"]+)"[^>]*>\s*(Opinion No\.\s*[^:<]+):\s*(.*?)</a>\s*</li>',
    re.S | re.I,
)
YEAR_PAGE_RE = re.compile(
    r'href="([^"]*opinions/\d{4}-opinions\.html)"',
    re.I,
)


def parse_news_html(html_text: str) -> list[dict[str, str | None]]:
    items: list[dict[str, str | None]] = []
    for match in NEWS_RE.finditer(html_text):
        href = match.group(1)
        url = canonicalize_url(urljoin(TN_ORIGIN, href))
        title = strip_html(match.group(2))
        published = parse_date(match.group(3))
        summary = strip_html(match.group(4))
        items.append({"title": title, "url": url, "published_at": published, "summary": summary})
    return items


def parse_opinions_html(html_text: str) -> list[dict[str, str | None]]:
    items: list[dict[str, str | None]] = []
    for match in OPINION_RE.finditer(html_text):
        href = match.group(1)
        url = canonicalize_url(urljoin(TN_ORIGIN, href))
        number = strip_html(match.group(2))
        title_rest = strip_html(match.group(3))
        title = f"{number}: {title_rest}".strip()
        items.append(
            {
                "title": title,
                "url": url,
                "published_at": None,
                "summary": title_rest,
                "opinion_number": number,
            }
        )
    return items


def _to_candidate(item: dict[str, str | None], *, kind: str) -> Candidate | None:
    title = item.get("title") or ""
    summary = item.get("summary") or ""
    url = item.get("url") or ""
    if not title or not url:
        return None
    topics = match_topics_from_item(title, summary)
    if not topics:
        return None
    if kind == "opinion":
        number = strip_html(item.get("opinion_number") or title)
        slug = re.sub(r"[^0-9a-z-]+", "-", number.lower()).strip("-")
        candidate_id = f"tn-ag-op:{slug}"
        source_name = "Tennessee Attorney General opinions"
    else:
        path = url.rstrip("/").rsplit("/", 1)[-1].replace(".html", "")
        candidate_id = f"tn-ag-news:{path}"
        source_name = "Tennessee Attorney General news"
    return Candidate(
        candidate_id=candidate_id,
        source_id="attorney-general",
        source_name=source_name,
        title=title[:240],
        url=url,
        summary=(summary or title)[:1200],
        published_at=item.get("published_at"),
        extra={"document_kind": kind},
        matched_keywords=topics,
        content_fingerprint=content_fingerprint(title, summary),
    )


def fetch_attorney_general() -> list[Candidate]:
    candidates: list[Candidate] = []
    try:
        news_html = fetch_text(NEWS_URL)
        news_items = parse_news_html(news_html)
        LOGGER.info("attorney-general news fetched %s item(s)", len(news_items))
        for item in news_items:
            candidate = _to_candidate(item, kind="news")
            if candidate:
                candidates.append(candidate)
    except FetchError as exc:
        LOGGER.warning("Attorney General news fetch failed: %s", exc)

    try:
        index_html = fetch_text(OPINIONS_INDEX)
        year_pages = YEAR_PAGE_RE.findall(index_html)
        current_year = date.today().year
        targets = [
            canonicalize_url(urljoin(TN_ORIGIN, href))
            for href in year_pages
            if str(current_year) in href or str(current_year - 1) in href
        ]
        if not targets:
            targets = [
                canonicalize_url(
                    f"https://www.tn.gov/attorneygeneral/opinions/{current_year}-opinions.html"
                )
            ]
        seen_urls: set[str] = set()
        for page_url in targets:
            if page_url in seen_urls:
                continue
            seen_urls.add(page_url)
            opinions_html = fetch_text(page_url)
            opinion_items = parse_opinions_html(opinions_html)
            LOGGER.info("attorney-general opinions %s fetched %s item(s)", page_url, len(opinion_items))
            for item in opinion_items:
                candidate = _to_candidate(item, kind="opinion")
                if candidate:
                    candidates.append(candidate)
    except FetchError as exc:
        LOGGER.warning("Attorney General opinions fetch failed: %s", exc)

    LOGGER.info("attorney-general produced %s keyword-matching candidate(s)", len(candidates))
    return candidates
