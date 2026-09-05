"""URL, HTML, date, and fingerprint helpers."""

from __future__ import annotations

from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from hashlib import sha256
import html
import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

BILL_RE = re.compile(r"\b((?:HB|SB|HR|SR|HJR|SJR)\s*\d{2,4})\b", re.I)
PUBLIC_CHAPTER_RE = re.compile(r"\b(?:public\s+chapter|pub\.\s*ch\.?)\s*(\d{2,4})\b", re.I)
TRACKING_PARAMS = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
    "fbclid",
    "gclid",
    "mc_cid",
    "mc_eid",
}

_TAG_RE = re.compile(r"(?is)<(script|style).*?>.*?</\1>")
_HTML_RE = re.compile(r"(?s)<[^>]+>")
_WS_RE = re.compile(r"\s+")
_MARK_RE = re.compile(r"</?mark>", re.I)


def strip_html(value: str | None) -> str:
    if not value:
        return ""
    text = _TAG_RE.sub(" ", value)
    text = _MARK_RE.sub("", text)
    text = _HTML_RE.sub(" ", text)
    text = html.unescape(text)
    return collapse_ws(text)


def collapse_ws(value: str | None) -> str:
    if not value:
        return ""
    return _WS_RE.sub(" ", value).strip()


def canonicalize_url(url: str) -> str:
    raw = collapse_ws(html.unescape(url or ""))
    if not raw:
        return ""
    parts = urlsplit(raw)
    scheme = (parts.scheme or "https").lower()
    netloc = parts.netloc.lower()
    if netloc.startswith("www."):
        netloc_key = netloc
    else:
        netloc_key = netloc
    path = parts.path.rstrip("/") or "/"
    query_items = [
        (key, value)
        for key, value in parse_qsl(parts.query, keep_blank_values=True)
        if key.lower() not in TRACKING_PARAMS
    ]
    # Keep bill identifiers stable across query-param order/case.
    normalized_query = []
    for key, value in query_items:
        if key.lower() == "billnumber":
            normalized_query.append(("BillNumber", value.upper().replace(" ", "")))
        elif key.lower() == "ga":
            normalized_query.append(("ga", value))
        else:
            normalized_query.append((key, value))
    query = urlencode(normalized_query, doseq=True)
    return urlunsplit((scheme, netloc_key, path, query, ""))


def sha_short(*parts: str, length: int = 16) -> str:
    payload = "\n".join(parts).encode("utf-8", errors="replace")
    return sha256(payload).hexdigest()[:length]


def content_fingerprint(title: str, summary: str) -> str:
    normalized = collapse_ws(f"{title} {summary}").lower()
    normalized = BILL_RE.sub(" ", normalized)
    normalized = re.sub(r"[^a-z0-9\s]+", " ", normalized)
    return sha_short(collapse_ws(normalized), length=20)


def extract_bill_numbers(text: str) -> tuple[str, ...]:
    found: list[str] = []
    seen: set[str] = set()
    for match in BILL_RE.findall(text or ""):
        compact = re.sub(r"\s+", "", match.upper())
        if compact not in seen:
            seen.add(compact)
            found.append(compact)
    return tuple(found)


def extract_public_chapters(text: str) -> tuple[str, ...]:
    found: list[str] = []
    seen: set[str] = set()
    for match in PUBLIC_CHAPTER_RE.findall(text or ""):
        key = f"PC{match}"
        if key not in seen:
            seen.add(key)
            found.append(key)
    return tuple(found)


def parse_date(value: str | None) -> str | None:
    """Return YYYY-MM-DD when a date can be parsed; otherwise None."""
    if not value:
        return None
    text = strip_html(value)
    text = text.split("|", 1)[0].strip()
    text = re.sub(r"^[A-Za-z]+,\s+", "", text)
    iso_match = re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", text)
    if iso_match:
        return iso_match.group(1)
    try:
        parsed = parsedate_to_datetime(text)
        if parsed is not None:
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.date().isoformat()
    except (TypeError, ValueError, IndexError):
        pass
    for fmt in (
        "%B %d, %Y",
        "%b %d, %Y",
        "%B %d %Y",
        "%m/%d/%Y",
        "%Y/%m/%d",
    ):
        try:
            return datetime.strptime(text, fmt).date().isoformat()
        except ValueError:
            continue
    match = re.search(
        r"\b(January|February|March|April|May|June|July|August|"
        r"September|October|November|December)\s+\d{1,2},\s+20\d{2}\b",
        text,
        re.I,
    )
    if match:
        try:
            return datetime.strptime(match.group(0), "%B %d, %Y").date().isoformat()
        except ValueError:
            return None
    return None


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def within_lookback(published_at: str | None, lookback_days: int, today: str | None = None) -> bool:
    if not published_at:
        return True
    try:
        item_day = datetime.strptime(published_at[:10], "%Y-%m-%d").date()
    except ValueError:
        return True
    if today:
        current = datetime.strptime(today[:10], "%Y-%m-%d").date()
    else:
        current = datetime.now(timezone.utc).date()
    return (current - item_day).days <= lookback_days
