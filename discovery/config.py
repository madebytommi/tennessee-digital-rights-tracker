"""Runtime defaults for the Tennessee Rights Scout."""

from __future__ import annotations

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
GEMINI_PAUSE_SECONDS = 0.6

GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_API_KEY_ENV = "GEMINI_API_KEY"

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
