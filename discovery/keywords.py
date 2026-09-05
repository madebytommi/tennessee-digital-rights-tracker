"""Keyword and topic filters for Tracker-relevant digital-rights issues."""

from __future__ import annotations

import re

from discovery.textutil import collapse_ws

# Phrases are matched case-insensitively. Short tokens use word boundaries.
TOPIC_PHRASES: dict[str, tuple[str, ...]] = {
    "privacy": (
        "privacy",
        "personal data",
        "personal information",
        "data collection",
        "data sharing",
        "data-sharing",
        "data broker",
        "data-broker",
        "consumer data",
        "sensitive data",
        "identifying information",
        "information sharing",
        "records request",
        "public records",
        "open records",
    ),
    "surveillance": (
        "surveillance",
        "wiretap",
        "geofence",
        "geo-fence",
        "stingray",
        "cell-site simulator",
        "cell site simulator",
        "social-media monitoring",
        "social media monitoring",
        "camera system",
        "cctv",
        "location tracking",
        "location data",
        "real-time crime",
        "fusion center",
    ),
    "alpr-flock": (
        "alpr",
        "automated license plate",
        "automatic license plate",
        "license plate reader",
        "license-plate reader",
        "license plate recognition",
        "licence plate reader",
        "flock safety",
        "flock camera",
        "flock alpr",
    ),
    "facial-recognition": (
        "facial recognition",
        "face recognition",
        "face surveillance",
        "face scan",
        "clearview",
    ),
    "biometrics": (
        "biometric",
        "fingerprints",
        "fingerprint database",
        "iris scan",
        "voice print",
        "voiceprint",
        "palm print",
    ),
    "ai-automation": (
        "artificial intelligence",
        "machine learning",
        "automated decision",
        "algorithmic",
        "generative ai",
        "deepfake",
        "deep fake",
        "synthetic media",
        "automated decision-making",
        "risk scoring",
        "government ai",
    ),
    "social-media-regulation": (
        "social media",
        "social-media",
        "content moderation",
        "platform obligation",
        "section 230",
        "app store",
        "instagram",
        "meta platforms",
    ),
    "age-identity-verification": (
        "age verification",
        "age-verification",
        "age assurance",
        "parental consent",
        "digital id",
        "digital identification",
        "identity verification",
        "know your customer",
        "age gate",
        "age-gate",
    ),
    "online-speech": (
        "free speech",
        "first amendment",
        "online speech",
        "compelled speech",
        "censorship",
        "book ban",
        "campus speech",
        "viewpoint discrimination",
    ),
    "lgbtq-trans-digital": (
        "transgender",
        "gender identity",
        "gender-affirming",
        "gender affirming",
        "preferred pronoun",
        "lgbtq",
        "nonbinary",
        "non-binary",
        "drag performance",
        "transition-related",
        "sex designated",
    ),
    "reproductive-health-data": (
        "abortion",
        "reproductive",
        "mifepristone",
        "medication abortion",
        "health data",
        "medical record",
        "patient data",
        "hipaa",
        "tenncare",
        "abortion pill",
        "abortion-inducing",
    ),
    "election-data": (
        "voter data",
        "voter file",
        "voter registration database",
        "election infrastructure",
        "election cybersecurity",
        "save database",
        "citizenship verification",
    ),
}

TOKEN_PATTERNS: tuple[tuple[str, str], ...] = (
    ("ai-automation", r"\bai\b"),
    ("alpr-flock", r"\blpr\b"),
    ("alpr-flock", r"\banpr\b"),
    ("age-identity-verification", r"\bkyc\b"),
    ("reproductive-health-data", r"\behr\b"),
)

_PHRASE_INDEX: list[tuple[str, str, re.Pattern[str]]] = []
for _topic, _phrases in TOPIC_PHRASES.items():
    for _phrase in _phrases:
        _PHRASE_INDEX.append(
            (
                _topic,
                _phrase,
                re.compile(r"(?<![a-z0-9])" + re.escape(_phrase) + r"(?![a-z0-9])", re.I),
            )
        )

_TOKEN_INDEX = tuple(
    (topic, re.compile(pattern, re.I)) for topic, pattern in TOKEN_PATTERNS
)

# Legislative search uses a smaller set of official-looking terms so the
# General Assembly adapter stays within a handful of HTTP requests.
LEGISLATIVE_SEARCH_TERMS: tuple[str, ...] = (
    "privacy",
    "surveillance",
    "biometric",
    "facial recognition",
    "license plate",
    "age verification",
    "social media",
    "artificial intelligence",
    "deepfake",
    "transgender",
    "abortion",
    "data broker",
    "voter data",
)

COURTLISTENER_QUERY = (
    "(privacy OR surveillance OR biometric OR \"facial recognition\" OR ALPR "
    "OR \"license plate\" OR \"social media\" OR \"age verification\" "
    "OR \"first amendment\" OR transgender OR \"gender identity\" OR abortion "
    "OR deepfake OR \"artificial intelligence\" OR biometric OR Flock) "
    "AND (Tennessee OR Tennessean OR Nashville OR Memphis OR Knoxville "
    "OR Chattanooga OR \"Tenn.\")"
)


def match_topics_from_item(title: str, summary: str, *, summary_limit: int = 500) -> tuple[str, ...]:
    """Match against the title plus a short summary prefix.

    Using the full article body would treat share widgets and unrelated
    later paragraphs as if they were the subject of the item.
    """
    return match_topics(f"{title}\n{(summary or '')[:summary_limit]}")


def match_topics(text: str) -> tuple[str, ...]:
    haystack = collapse_ws(text)
    if not haystack:
        return ()
    matched: list[str] = []
    seen: set[str] = set()
    for topic, _phrase, pattern in _PHRASE_INDEX:
        if topic in seen:
            continue
        if pattern.search(haystack):
            seen.add(topic)
            matched.append(topic)
    for topic, pattern in _TOKEN_INDEX:
        if topic in seen:
            continue
        if pattern.search(haystack):
            seen.add(topic)
            matched.append(topic)
    return tuple(matched)


def is_relevant(text: str) -> bool:
    return bool(match_topics(text))
