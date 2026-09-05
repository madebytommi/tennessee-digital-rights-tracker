"""CourtListener adapter for Sixth Circuit and Tennessee federal courts."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
import logging
import os
from urllib.parse import urlencode

from discovery.http import FetchError, fetch_json
from discovery.keywords import COURTLISTENER_QUERY, match_topics_from_item
from discovery.textutil import canonicalize_url, content_fingerprint, strip_html
from discovery.types import Candidate

LOGGER = logging.getLogger("scout.source.courtlistener")

SEARCH_ENDPOINT = "https://www.courtlistener.com/api/rest/v4/search/"
COURT_IDS = "ca6,tned,tnmd,tnwd"


def _auth_headers() -> dict[str, str]:
    token = os.environ.get("COURTLISTENER_TOKEN") or os.environ.get("COURTLISTENER_API_TOKEN")
    if token:
        return {"Authorization": f"Token {token}"}
    return {}


def parse_courtlistener_results(payload: object) -> list[Candidate]:
    if not isinstance(payload, dict):
        return []
    results = payload.get("results") or []
    candidates: list[Candidate] = []
    if not isinstance(results, list):
        return []
    for row in results:
        if not isinstance(row, dict):
            continue
        path = str(row.get("absolute_url") or "")
        if not path:
            continue
        url = canonicalize_url("https://www.courtlistener.com" + path)
        case_name = strip_html(str(row.get("caseName") or row.get("caseNameFull") or "Untitled case"))
        docket = strip_html(str(row.get("docketNumber") or ""))
        court = strip_html(str(row.get("court") or row.get("court_id") or ""))
        date_filed = str(row.get("dateFiled") or "")[:10] or None
        snippets = []
        for opinion in row.get("opinions") or []:
            if isinstance(opinion, dict) and opinion.get("snippet"):
                snippets.append(strip_html(str(opinion["snippet"])))
        summary = strip_html(" ".join(snippets)) or (
            f"{case_name} ({court}" + (f", {docket}" if docket else "") + ")."
        )
        blob = f"{case_name} {court} {docket} {summary}"
        topics = match_topics_from_item(case_name, blob)
        if not topics:
            continue
        cluster_id = str(row.get("cluster_id") or row.get("id") or path)
        title = case_name if not docket else f"{case_name} ({docket})"
        candidates.append(
            Candidate(
                candidate_id=f"cl:{cluster_id}",
                source_id="courtlistener",
                source_name="CourtListener",
                title=title[:240],
                url=url,
                summary=summary[:1200],
                published_at=date_filed,
                extra={
                    "court": court,
                    "court_id": row.get("court_id"),
                    "docket_number": docket,
                    "status": row.get("status"),
                    "document_kind": "court-opinion",
                },
                matched_keywords=topics,
                content_fingerprint=content_fingerprint(title, summary),
            )
        )
    return candidates


def fetch_courtlistener(*, lookback_days: int = 21) -> list[Candidate]:
    filed_after = (
        datetime.now(timezone.utc) - timedelta(days=lookback_days)
    ).date().isoformat()
    params = {
        "type": "o",
        "court": COURT_IDS,
        "q": COURTLISTENER_QUERY,
        "order_by": "dateFiled desc",
        "page_size": "20",
        "highlight": "on",
        "filed_after": filed_after,
    }
    url = f"{SEARCH_ENDPOINT}?{urlencode(params)}"
    try:
        payload = fetch_json(url, headers=_auth_headers())
    except FetchError as exc:
        LOGGER.warning("CourtListener fetch with filed_after failed (%s); retrying without date filter", exc)
        params.pop("filed_after", None)
        url = f"{SEARCH_ENDPOINT}?{urlencode(params)}"
        try:
            payload = fetch_json(url, headers=_auth_headers())
        except FetchError as retry_exc:
            LOGGER.warning("CourtListener fetch failed: %s", retry_exc)
            return []
    if isinstance(payload, dict) and payload.get("detail"):
        LOGGER.warning("CourtListener API detail: %s", payload.get("detail"))
    candidates = parse_courtlistener_results(payload)
    count = payload.get("count") if isinstance(payload, dict) else "?"
    LOGGER.info(
        "courtlistener fetched count=%s, keyword-matching=%s (filed_after=%s)",
        count,
        len(candidates),
        filed_after,
    )
    return candidates
