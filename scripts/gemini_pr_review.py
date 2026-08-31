#!/usr/bin/env python3
"""Review tracker pull requests with Gemini and maintain one PR comment."""

from __future__ import annotations

import os
import subprocess
import sys

import requests
from google import genai

# Workflow smoke-test note: changing this comment does not affect runtime behavior.
MARKER = "<!-- gemini-tracker-review -->"


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def get_diff(base: str, head: str) -> str:
    return subprocess.check_output(
        ["git", "diff", "--no-ext-diff", f"{base}...{head}"],
        text=True,
        errors="replace",
    )


def upsert_comment(repo: str, pr_number: str, token: str, body: str) -> None:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    comments_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    response = requests.get(comments_url, headers=headers, timeout=30)
    response.raise_for_status()

    existing = next(
        (
            item
            for item in response.json()
            if MARKER in item.get("body", "")
            and item.get("user", {}).get("login") == "github-actions[bot]"
        ),
        None,
    )

    payload = {"body": f"{MARKER}\n### Gemini tracker review\n\n{body}"}
    if existing:
        url = f"https://api.github.com/repos/{repo}/issues/comments/{existing['id']}"
        result = requests.patch(url, headers=headers, json=payload, timeout=30)
    else:
        result = requests.post(comments_url, headers=headers, json=payload, timeout=30)
    result.raise_for_status()


def main() -> int:
    api_key = require_env("GEMINI_API_KEY")
    github_token = require_env("GITHUB_TOKEN")
    repo = require_env("REPO")
    pr_number = require_env("PR_NUMBER")
    base = require_env("BASE_SHA")
    head = require_env("HEAD_SHA")

    diff = get_diff(base, head)
    if not diff.strip():
        print("No PR diff found; skipping Gemini review.")
        return 0

    diff = diff[:50000]
    prompt = f"""You are reviewing a pull request for a public-interest Tennessee digital-rights tracker.

Your job is REVIEW ONLY. Do not claim that you changed files and do not recommend an automatic merge.

Prioritize these checks:
1. Repository compliance: required headings/frontmatter, internal consistency, and obvious structural problems.
2. Evidence quality: whether claims appear stronger than the cited or described evidence supports.
3. Legal-status precision: distinguish proposed, enacted, effective, stayed, enjoined, appealed, vacated, remanded, preliminary, and final actions.
4. Attribution: distinguish direct authorship/influence from mere alignment or similarity.
5. Uncertainty: flag assertions that should be narrowed or qualified.
6. Privacy/civil-rights framing: identify overlooked data-collection, anonymity, identity-verification, surveillance, access, or disparate-impact concerns.
7. Source hygiene: flag missing primary sources or overreliance on commentary where a primary source is expected.

Important boundaries:
- Treat factual, legal, policy, medical, and civil-rights substance as human-reviewed material.
- Never invent facts, citations, case holdings, dates, quotations, or source contents.
- If the diff does not give enough evidence to verify something, say so explicitly.
- Be concise. Separate findings into: Blocking concerns, Review notes, and Looks good.

Pull request diff:
```diff
{diff}
```
"""

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    review = (response.text or "Gemini returned no review text.").strip()
    upsert_comment(repo, pr_number, github_token, review)
    print("Gemini tracker review posted or updated.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Gemini tracker review failed: {exc}", file=sys.stderr)
        raise
