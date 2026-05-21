#!/usr/bin/env python3
"""Validate a rigorous-reviewer Markdown report.

This script intentionally checks structure, not scientific truth. It catches the
common failure mode where a saved report loses the required reviewer issue
anatomy after drafting or editing.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "Category Scores",
    "Field Evidence Map",
    "Calibration Against Gold / Near-Gold Papers",
    "Reviewer Panel Synthesis",
    "External Scientific Skills Used",
    "Identified Issues",
    "Literature / Source Search Hints",
    "Revision Suggested Actions",
    "Evidence Ledger",
    "Red-Line Self-Audit",
    "Overall Recommendation",
]

REQUIRED_LABELS = [
    "具体问题",
    "证据",
    "影响",
    "替代解释/漏洞",
    "解决",
    "决定性 readout",
]

SEVERITY_RE = re.compile(r"^\s*[-*]\s*\[(Critical|Major|Minor)\]\s+(.+)$", re.MULTILINE)
HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)
SOURCE_RE = re.compile(
    r"(doi|pmid|pmcid|arxiv|https?://|clinicaltrials|geo|sra|arrayexpress|"
    r"guideline|standard|benchmark|dataset|accession|rrid|search target)",
    re.I,
)
RECOMMENDATIONS = ["Accept", "Minor Revision", "Major Revision", "Reject"]
VAGUE_PHRASES = [
    "more controls are needed",
    "needs more validation",
    "improve the analysis",
    "optimize as needed",
    "standard conditions",
    "appropriate amount",
]


def section_text(text: str, title: str) -> str:
    pattern = re.compile(rf"^##\s+\d+\)\s+{re.escape(title)}\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return ""
    start = match.end()
    next_heading = re.search(r"^##\s+\d+\)\s+", text[start:], re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(text)
    return text[start:end].strip()


def section_present(text: str, title: str) -> bool:
    pattern = re.compile(rf"^##\s+\d+\)\s+{re.escape(title)}\s*$", re.MULTILINE)
    return bool(pattern.search(text))


def extract_issue_blocks(text: str) -> list[tuple[str, str, str]]:
    blocks: list[tuple[str, str, str]] = []
    matches = list(SEVERITY_RE.finditer(text))
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        next_heading = HEADING_RE.search(text, match.end())
        if next_heading and next_heading.start() < end:
            end = next_heading.start()
        blocks.append((match.group(1), match.group(2).strip(), text[start:end].strip()))
    return blocks


def contains_any(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    for needle in needles:
        if needle.lower() in lowered:
            return True
    return False


def has_support_condition(text: str) -> bool:
    if "支持" in text:
        return True
    return bool(re.search(r"\b(support|supports|supporting|strengthen|strengthens|consistent with)\b", text, re.I))


def validate_issue_block(severity: str, title: str, block: str, strict: bool = False) -> list[str]:
    errors: list[str] = []
    for label in REQUIRED_LABELS:
        if f"{label}：" not in block and f"{label}:" not in block:
            errors.append(f"[{severity}] {title}: missing label `{label}`")

    if "为什么严重：" not in block and "为什么严重:" not in block:
        if "为什么重要：" not in block and "为什么重要:" not in block:
            errors.append(f"[{severity}] {title}: missing `为什么严重` or `为什么重要`")

    for evidence_label in ["稿件内部证据", "外部证据/标准"]:
        if evidence_label not in block:
            errors.append(f"[{severity}] {title}: missing evidence split `{evidence_label}`")

    if not has_support_condition(block):
        errors.append(f"[{severity}] {title}: decisive readout lacks a support condition")

    if not contains_any(block, ["削弱", "反驳", "narrow", "weaken", "refut", "force narrowing"]):
        errors.append(
            f"[{severity}] {title}: decisive readout lacks a weakening/refuting/narrowing condition"
        )

    if strict and severity in {"Critical", "Major"}:
        if len(block) < 700:
            errors.append(f"[{severity}] {title}: issue block is too short for strict mode")
        if not SOURCE_RE.search(block):
            errors.append(
                f"[{severity}] {title}: strict mode requires an external identifier, standard, benchmark, or search target"
            )

    return errors


def evidence_ledger_present(text: str) -> bool:
    return (
        "## 9) Evidence Ledger" in text
        and "| ID | Source | Type | Supports / challenges | Decision role | Identifier / link |" in text
    )


def validate(path: Path, strict: bool = False) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if not text.lstrip().startswith("# "):
        errors.append("report must start with a level-1 Markdown title")

    for section in REQUIRED_SECTIONS:
        if not section_present(text, section):
            errors.append(f"missing required section: {section}")

    issue_blocks = extract_issue_blocks(text)
    if not issue_blocks:
        errors.append("no `[Critical]`, `[Major]`, or `[Minor]` issue blocks found")
    else:
        for severity, title, block in issue_blocks:
            errors.extend(validate_issue_block(severity, title, block, strict=strict))

    if not evidence_ledger_present(text):
        errors.append("missing Evidence Ledger table with required columns")

    if strict:
        recommendation = section_text(text, "Overall Recommendation")
        if recommendation and not any(decision in recommendation for decision in RECOMMENDATIONS):
            errors.append("Overall Recommendation must include Accept, Minor Revision, Major Revision, or Reject")
        if any(severity == "Critical" for severity, _, _ in issue_blocks):
            if "Accept" in recommendation or "Minor Revision" in recommendation:
                errors.append("strict mode: report with Critical issues cannot recommend Accept or Minor Revision")
        lowered = text.lower()
        for phrase in VAGUE_PHRASES:
            if phrase in lowered:
                errors.append(f"strict mode: vague phrase found: `{phrase}`")

    if "<" in text and ">" in text:
        errors.append("report still appears to contain placeholder angle brackets")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="Markdown review report to validate")
    parser.add_argument("--strict", action="store_true", help="Enable stricter regression checks for CI fixtures")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable diagnostics")
    args = parser.parse_args()

    if not args.report.exists():
        print(f"ERROR: file not found: {args.report}", file=sys.stderr)
        return 2

    errors = validate(args.report, strict=args.strict)
    if args.json:
        print(json.dumps({"ok": not errors, "errors": errors}, indent=2, ensure_ascii=False))
        return 1 if errors else 0

    if errors:
        print("Review report validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Review report validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
