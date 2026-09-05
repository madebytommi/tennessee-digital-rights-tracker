"""Small HTTP helper with retries, timeouts, and an identifying User-Agent."""

from __future__ import annotations

import json
import logging
import time
import urllib.error
import urllib.request

from discovery.config import HTTP_RETRIES, HTTP_TIMEOUT_SECONDS, USER_AGENT

LOGGER = logging.getLogger("scout.http")


class FetchError(RuntimeError):
    """Raised when a source cannot be retrieved after retries."""


def fetch_bytes(url: str, *, accept: str | None = None, headers: dict[str, str] | None = None) -> bytes:
    request_headers = {
        "User-Agent": USER_AGENT,
        "Accept": accept or "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    if headers:
        request_headers.update(headers)
    last_error: Exception | None = None
    attempts = HTTP_RETRIES + 1
    for attempt in range(1, attempts + 1):
        try:
            req = urllib.request.Request(url, headers=request_headers, method="GET")
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_SECONDS) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last_error = exc
            LOGGER.warning("GET %s failed (attempt %s/%s): %s", url, attempt, attempts, exc)
            if attempt < attempts:
                time.sleep(0.8 * attempt)
    raise FetchError(f"Failed to fetch {url}: {last_error}") from last_error


def fetch_text(url: str, **kwargs: object) -> str:
    payload = fetch_bytes(url, **kwargs)  # type: ignore[arg-type]
    return payload.decode("utf-8", errors="replace")


def fetch_json(url: str, *, headers: dict[str, str] | None = None) -> object:
    merged = {"Accept": "application/json"}
    if headers:
        merged.update(headers)
    text = fetch_text(url, accept="application/json", headers=merged)
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise FetchError(f"Invalid JSON from {url}: {exc}") from exc
