from __future__ import annotations

import json
import os
import unittest
from unittest import mock

from discovery.config import (
    DEFAULT_GEMINI_MIN_INTERVAL_SECONDS,
    DEFAULT_GEMINI_MODEL,
    GEMINI_MAX_ATTEMPTS,
    GEMINI_RATE_LIMIT_FALLBACK_SECONDS,
    gemini_min_interval_seconds,
    gemini_model,
)
from discovery.evaluate import (
    call_gemini_with_retry,
    evaluate_candidate,
    parse_evaluation_payload,
    reset_gemini_pacing,
    should_surface,
)
from discovery.issue import format_issue_body, format_issue_title
from discovery.types import Candidate, Evaluation


class EvaluateTests(unittest.TestCase):
    def test_parse_json_inside_fence(self) -> None:
        text = """```json
{
  "tennessee_relevance": 0.9,
  "digital_rights_relevance": 0.8,
  "significance": 0.7,
  "source_quality": 0.85,
  "novelty": 0.6,
  "suggested_action": "NEW ENTRY",
  "confidence": "Medium",
  "matching_entry": null,
  "summary": "A bill would require age verification.",
  "why_it_matters": "It would create a statewide identity-check mandate.",
  "explanation": "Primary legislative source with a clear Tennessee nexus."
}
```"""
        evaluation = parse_evaluation_payload(text)
        self.assertEqual(evaluation.suggested_action, "NEW ENTRY")
        self.assertGreater(evaluation.composite, 0.7)
        self.assertTrue(should_surface(evaluation))

    def test_below_threshold_not_surfaced(self) -> None:
        evaluation = parse_evaluation_payload(
            """
            {
              "tennessee_relevance": 0.2,
              "digital_rights_relevance": 0.2,
              "significance": 0.2,
              "source_quality": 0.5,
              "novelty": 0.5,
              "suggested_action": "WATCH",
              "confidence": "Low",
              "matching_entry": "none",
              "summary": "Weak connection.",
              "why_it_matters": "Unclear.",
              "explanation": "Incidental mention."
            }
            """
        )
        self.assertFalse(should_surface(evaluation))
        self.assertIsNone(evaluation.matching_entry)

    def test_issue_body_contains_required_fields(self) -> None:
        candidate = Candidate(
            candidate_id="lookout:1",
            source_id="lookout",
            source_name="Tennessee Lookout",
            title="County expands Flock cameras",
            url="https://tennesseelookout.com/example",
            summary="ALPR expansion.",
            matched_keywords=("alpr-flock",),
        )
        evaluation = Evaluation(
            tennessee_relevance=0.9,
            digital_rights_relevance=0.9,
            significance=0.8,
            source_quality=0.7,
            novelty=0.8,
            composite=0.84,
            suggested_action="NEW ENTRY",
            confidence="Medium",
            matching_entry=None,
            summary="A county expanded Flock ALPRs.",
            why_it_matters="License-plate databases can affect location privacy.",
            explanation="Local news lead; needs primary records.",
        )
        body = format_issue_body(candidate, evaluation, matching_entry=None)
        title = format_issue_title(candidate)
        self.assertTrue(title.startswith("[Discovery]"))
        for needle in (
            "Source URL",
            "Short summary",
            "Relevance score",
            "Confidence",
            "Suggested action",
            "Possible matching tracker entry",
            "Why it may matter",
            "`NEW ENTRY`",
            "https://tennesseelookout.com/example",
        ):
            self.assertIn(needle, body)


class FakeGeminiError(Exception):
    def __init__(
        self,
        code: int,
        status: str,
        message: str = "",
        details: object | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.code = code
        self.status = status
        self.message = message or f"{code} {status}"
        self.details = details if details is not None else {"error": {"code": code, "status": status}}
        self.response = mock.Mock(headers=headers or {})
        super().__init__(f"{code} {status}. {self.details}")


class FakeClock:
    def __init__(self, start: float = 0.0) -> None:
        self.now = start
        self.sleeps: list[float] = []

    def monotonic(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


def _good_payload() -> str:
    return json.dumps(
        {
            "tennessee_relevance": 0.9,
            "digital_rights_relevance": 0.8,
            "significance": 0.7,
            "source_quality": 0.85,
            "novelty": 0.6,
            "suggested_action": "NEW ENTRY",
            "confidence": "Medium",
            "matching_entry": None,
            "summary": "A bill would require age verification.",
            "why_it_matters": "It would create a statewide identity-check mandate.",
            "explanation": "Primary legislative source with a clear Tennessee nexus.",
        }
    )


def _candidate() -> Candidate:
    return Candidate(
        candidate_id="lookout:rate-limit-test",
        source_id="lookout",
        source_name="Tennessee Lookout",
        title="County expands Flock cameras",
        url="https://tennesseelookout.com/example",
        summary="ALPR expansion.",
        matched_keywords=("alpr-flock",),
    )


class GeminiConfigTests(unittest.TestCase):
    def test_default_model_is_gemini_3_5_flash_lite(self) -> None:
        with mock.patch.dict(os.environ):
            os.environ.pop("GEMINI_MODEL", None)
            self.assertEqual(DEFAULT_GEMINI_MODEL, "gemini-3.5-flash-lite")
            self.assertEqual(gemini_model(), "gemini-3.5-flash-lite")

    def test_gemini_model_environment_override(self) -> None:
        with mock.patch.dict(os.environ, {"GEMINI_MODEL": "gemini-2.5-flash"}):
            self.assertEqual(gemini_model(), "gemini-2.5-flash")

    def test_default_min_interval_is_between_4_5_and_5(self) -> None:
        with mock.patch.dict(os.environ):
            os.environ.pop("GEMINI_MIN_INTERVAL_SECONDS", None)
            interval = gemini_min_interval_seconds()
            self.assertEqual(interval, DEFAULT_GEMINI_MIN_INTERVAL_SECONDS)
            self.assertGreaterEqual(interval, 4.5)
            self.assertLessEqual(interval, 5.0)

    def test_min_interval_environment_override(self) -> None:
        with mock.patch.dict(os.environ, {"GEMINI_MIN_INTERVAL_SECONDS": "9.25"}):
            self.assertEqual(gemini_min_interval_seconds(), 9.25)


class GeminiRetryTests(unittest.TestCase):
    def setUp(self) -> None:
        reset_gemini_pacing()

    def tearDown(self) -> None:
        reset_gemini_pacing()

    def test_pacing_occurs_between_gemini_calls(self) -> None:
        clock = FakeClock()
        calls = {"n": 0}

        def generate() -> str:
            calls["n"] += 1
            return "ok"

        first = call_gemini_with_retry(
            generate,
            sleeper=clock.sleep,
            clock=clock.monotonic,
            min_interval=4.5,
        )
        second = call_gemini_with_retry(
            generate,
            sleeper=clock.sleep,
            clock=clock.monotonic,
            min_interval=4.5,
        )
        self.assertEqual(first, "ok")
        self.assertEqual(second, "ok")
        self.assertEqual(calls["n"], 2)
        self.assertEqual(clock.sleeps, [4.5])

    def test_http_429_retries_the_same_candidate(self) -> None:
        clock = FakeClock()
        calls: list[str] = []

        def generate() -> str:
            calls.append("lookout:rate-limit-test")
            if len(calls) == 1:
                raise FakeGeminiError(429, "RESOURCE_EXHAUSTED", details={"error": {"status": "RESOURCE_EXHAUSTED"}})
            return _good_payload()

        with self.assertLogs("scout.evaluate", level="WARNING") as logs:
            text = call_gemini_with_retry(
                generate,
                candidate_id="lookout:rate-limit-test",
                sleeper=clock.sleep,
                clock=clock.monotonic,
                min_interval=0.0,
            )
        self.assertEqual(calls, ["lookout:rate-limit-test", "lookout:rate-limit-test"])
        self.assertIn("NEW ENTRY", text)
        self.assertTrue(any("rate-limited" in line.lower() for line in logs.output))
        self.assertEqual(clock.sleeps, [GEMINI_RATE_LIMIT_FALLBACK_SECONDS])

    def test_returned_retry_delay_is_honored(self) -> None:
        clock = FakeClock()
        details = {
            "error": {
                "code": 429,
                "status": "RESOURCE_EXHAUSTED",
                "details": [
                    {
                        "@type": "type.googleapis.com/google.rpc.RetryInfo",
                        "retryDelay": "12s",
                    }
                ],
            }
        }
        calls = {"n": 0}

        def generate() -> str:
            calls["n"] += 1
            if calls["n"] == 1:
                raise FakeGeminiError(429, "RESOURCE_EXHAUSTED", details=details)
            return "ok"

        with self.assertLogs("scout.evaluate", level="WARNING") as logs:
            result = call_gemini_with_retry(
                generate,
                candidate_id="lookout:rate-limit-test",
                sleeper=clock.sleep,
                clock=clock.monotonic,
                min_interval=0.0,
            )
        self.assertEqual(result, "ok")
        self.assertEqual(calls["n"], 2)
        self.assertEqual(clock.sleeps, [12.0])
        self.assertTrue(any("waiting 12.0s" in line for line in logs.output))

    def test_http_503_uses_bounded_exponential_backoff(self) -> None:
        clock = FakeClock()
        calls = {"n": 0}

        def generate() -> str:
            calls["n"] += 1
            raise FakeGeminiError(503, "UNAVAILABLE", message="The service is currently unavailable")

        with self.assertLogs("scout.evaluate", level="WARNING"):
            with self.assertRaises(FakeGeminiError):
                call_gemini_with_retry(
                    generate,
                    candidate_id="lookout:rate-limit-test",
                    sleeper=clock.sleep,
                    clock=clock.monotonic,
                    min_interval=0.0,
                )
        self.assertEqual(calls["n"], GEMINI_MAX_ATTEMPTS)
        self.assertEqual(clock.sleeps, [2.0, 4.0, 8.0, 16.0])
        self.assertLessEqual(max(clock.sleeps), 32.0)

    def test_successful_retry_returns_normal_evaluation(self) -> None:
        clock = FakeClock()
        calls = {"n": 0, "models": []}

        def generate_text(prompt: str, api_key: str, model: str) -> str:
            calls["n"] += 1
            calls["models"].append(model)
            if calls["n"] == 1:
                raise FakeGeminiError(
                    429,
                    "RESOURCE_EXHAUSTED",
                    details={"error": {"retryDelay": "7s"}},
                )
            self.assertIn("County expands Flock cameras", prompt)
            self.assertEqual(api_key, "test-key")
            return _good_payload()

        with mock.patch.dict(os.environ):
            os.environ.pop("GEMINI_MODEL", None)
            with self.assertLogs("scout.evaluate", level="WARNING"):
                evaluation = evaluate_candidate(
                    _candidate(),
                    [],
                    api_key="test-key",
                    sleeper=clock.sleep,
                    clock=clock.monotonic,
                    min_interval=0.0,
                    generate_text=generate_text,
                )
        self.assertEqual(calls["n"], 2)
        self.assertEqual(calls["models"], ["gemini-3.5-flash-lite", "gemini-3.5-flash-lite"])
        self.assertEqual(evaluation.suggested_action, "NEW ENTRY")
        self.assertTrue(should_surface(evaluation))
        self.assertEqual(clock.sleeps, [7.0])

    def test_permanent_failures_do_not_retry(self) -> None:
        clock = FakeClock()
        calls = {"n": 0}

        def generate() -> str:
            calls["n"] += 1
            raise FakeGeminiError(401, "UNAUTHENTICATED", message="API key not valid")

        with self.assertRaises(FakeGeminiError):
            call_gemini_with_retry(
                generate,
                candidate_id="lookout:rate-limit-test",
                sleeper=clock.sleep,
                clock=clock.monotonic,
                min_interval=0.0,
            )
        self.assertEqual(calls["n"], 1)
        self.assertEqual(clock.sleeps, [])

    def test_configuration_errors_do_not_retry(self) -> None:
        clock = FakeClock()
        calls = {"n": 0}

        def generate() -> str:
            calls["n"] += 1
            raise RuntimeError("google-genai is not installed")

        with self.assertRaises(RuntimeError):
            call_gemini_with_retry(
                generate,
                sleeper=clock.sleep,
                clock=clock.monotonic,
                min_interval=0.0,
            )
        self.assertEqual(calls["n"], 1)
        self.assertEqual(clock.sleeps, [])
