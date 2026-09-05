"""Runtime defaults for the Tennessee Rights Scout."""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DISCOVERY_DIR = Path(__file__).resolve().parent
DATA_DIR = ROOT / "discovery-data"
DEFAULT_SEEN_PATH = DATA_DIR / "seen.json"
ENTRY_DIR = ROOT / "_entries"
SPECIAL_CASE_DIR = ROOT / "_special_cases"

USER_AGENT = (
    "TennesseeRightsScout/1.0 "
    "(+https://github.com/madebytommi/tennessee-digital-rights-tracker; "
    "human-reviewed discovery)"
)

HTTP_TIMEOUT_SECONDS = 30
HTTP_RETRIES = 1
SOURCE_PAUSE_SECONDS = 0.4

# Free-tier Gemini 3.5 Flash-Lite allows 15 requests/minute. Scout is faster
# than that, so evaluation calls wait at least this long between starts.
DEFAULT_GEMINI_MIN_INTERVAL_SECONDS = 4.5
GEMINI_MIN_INTERVAL_ENV = "GEMINI_MIN_INTERVAL_SECONDS"
GEMINI_MAX_ATTEMPTS = 5
GEMINI_RATE_LIMIT_FALLBACK_SECONDS = 20.0
GEMINI_UNAVAILABLE_INITIAL_BACKOFF_SECONDS = 2.0
GEMINI_UNAVAILABLE_MAX_BACKOFF_SECONDS = 32.0

DEFAULT_GEMINI_MODEL = "gemini-3.5-flash-lite"
GEMINI_MODEL_ENV = "GEMINI_MODEL"
GEMINI_API_KEY_ENV = "GEMINI_API_KEY"
# Default model id when GEMINI_MODEL is unset. Prefer gemini_model().
GEMINI_MODEL = DEFAULT_GEMINI_MODEL

LOOKBACK_DAYS = 21
MAX_EVALUATE = 25
MAX_ISSUES_PER_RUN = 8

# Surface a candidate only when the overall score and both relevance axes
# clear these floors. Gemini scoring is a triage aid, not publication.
COMPOSITE_THRESHOLD = 0.62
TENNESSEE_THRESHOLD = 0.45
DIGITAL_RIGHTS_THRESHOLD = 0.45

SCORE_WEIGHTS = {
    "tennessee_relevance": 0.25,
    "digital_rights_relevance": 0.25,
    "significance": 0.20,
    "source_quality": 0.15,
    "novelty": 0.15,
}

ISSUE_LABEL = "discovery"
ISSUE_TITLE_PREFIX = "[Discovery]"
ISSUE_MARKER_PREFIX = "<!-- tennessee-rights-scout:"


def gemini_model() -> str:
    """Return the configured Gemini model, defaulting to Flash-Lite."""
    override = os.environ.get(GEMINI_MODEL_ENV, "").strip()
    return override or DEFAULT_GEMINI_MODEL


def gemini_min_interval_seconds() -> float:
    """Minimum seconds between Gemini request starts."""
    raw = os.environ.get(GEMINI_MIN_INTERVAL_ENV, "").strip()
    if not raw:
        return DEFAULT_GEMINI_MIN_INTERVAL_SECONDS
    try:
        return max(0.0, float(raw))
    except ValueError:
        return DEFAULT_GEMINI_MIN_INTERVAL_SECONDS
