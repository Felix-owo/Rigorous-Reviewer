#!/usr/bin/env python3
"""Lightweight validator for Rigorous Reviewer Markdown reports."""
from __future__ import annotations
import argparse, sys, re
from pathlib import Path

REQUIRED = [
    "Executive", "Pre-Review Contract", "Central Claim", "Critical", "Major",
    "Evidence", "Recommendation", "Self-Audit"
]

FORBIDDEN_WEAK = [
    "more controls are needed", "needs further validation", "additional experiments would strengthen"
]

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("report")
    args = p.parse_args()
    text = Path(args.report).read_text(encoding="utf-8")
    missing = [x for x in REQUIRED if x.lower() not in text.lower()]
    weak = [x for x in FORBIDDEN_WEAK if x in text.lower()]
    if missing:
        print("Missing required sections/terms:", ", ".join(missing), file=sys.stderr)
        return 1
    if weak:
        print("Generic weak phrases detected:", ", ".join(weak), file=sys.stderr)
        return 1
    print("Rigorous Reviewer report validator: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
