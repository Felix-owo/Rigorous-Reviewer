#!/usr/bin/env python3
"""Markdown validator for Rigorous Reviewer review reports.

This validator intentionally remains lightweight and dependency-free. It is used
by CI both for a strict golden Markdown fixture and for compact example reports.
The --strict flag tightens section and issue-block checks without rejecting
shorter non-strict examples.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BASE_REQUIRED = [
    "Pre-Review Contract",
    "Central claim",
    "Critical",
    "Evidence",
    "Recommendation",
    "Self-Audit",
]

STRICT_REQUIRED = [
    "Category Scores",
    "Claim Maturity Gate",
    "Field Evidence Map",
    "Reviewer Panel Synthesis",
    "Identified Issues",
    "Literature / Source Search Hints",
    "Revision Suggested Actions",
    "Evidence Ledger",
    "Overall Recommendation",
]

FORBIDDEN_WEAK = [
    "more controls are needed",
    "needs further validation",
    "additional experiments would strengthen",
]

STRICT_ISSUE_LABELS = [
    "具体问题：",
    "为什么严重：",
    "证据：",
    "影响：",
    "替代解释/漏洞：",
    "解决：",
    "决定性 readout：",
]

SEVERITY_RE = re.compile(r"\[(Critical|Major|Minor)\]", re.IGNORECASE)


def contains_term(text: str, term: str) -> bool:
    return term.lower() in text.lower()


def validate_report(path: Path, *, strict: bool = False) -> list[str]:
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    errors: list[str] = []

    required = BASE_REQUIRED + (STRICT_REQUIRED if strict else [])
    missing = [term for term in required if not contains_term(text, term)]
    if missing:
        errors.append("Missing required sections/terms: " + ", ".join(missing))

    weak = [phrase for phrase in FORBIDDEN_WEAK if phrase in lower]
    if weak:
        errors.append("Generic weak phrases detected: " + ", ".join(weak))

    if strict:
        if not SEVERITY_RE.search(text):
            errors.append("Strict mode requires at least one severity-tagged issue: [Critical], [Major], or [Minor].")
        missing_labels = [label for label in STRICT_ISSUE_LABELS if label not in text]
        if missing_labels:
            errors.append("Strict mode missing issue-block labels: " + ", ".join(missing_labels))
        if "稿件内部证据" not in text and "manuscript-internal" not in lower:
            errors.append("Strict mode requires manuscript-internal evidence traceability.")
        if "决定性 readout" not in text and "decisive readout" not in lower:
            errors.append("Strict mode requires a decisive readout statement.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Rigorous Reviewer Markdown report.")
    parser.add_argument("report", help="Path to a Markdown review report")
    parser.add_argument("--strict", action="store_true", help="Enable stricter checks for golden review fixtures.")
    args = parser.parse_args()

    path = Path(args.report)
    if not path.exists():
        print(f"Report not found: {path}", file=sys.stderr)
        return 2

    errors = validate_report(path, strict=args.strict)
    if errors:
        for error in errors:
            print("Error:", error, file=sys.stderr)
        return 1

    mode = "strict" if args.strict else "standard"
    print(f"Rigorous Reviewer report validator: PASS ({mode})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
