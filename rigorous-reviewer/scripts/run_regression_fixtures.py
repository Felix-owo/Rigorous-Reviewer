#!/usr/bin/env python3
"""Run Rigorous Reviewer regression fixtures."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "examples" / "regression_fixtures"


def run(cmd: list[str]) -> int:
    print("$ " + " ".join(cmd))
    result = subprocess.run(cmd, text=True)
    return result.returncode


def main() -> int:
    if not FIXTURES.exists():
        print(f"No regression fixtures found: {FIXTURES}")
        return 0
    failures = 0
    for path in sorted(FIXTURES.glob("*.json")):
        if path.name.startswith("handoff_"):
            failures += run([sys.executable, str(ROOT / "scripts" / "check_claim_readout_handoff.py"), str(path)])
        elif path.name.startswith("contract_"):
            failures += run([sys.executable, str(ROOT / "scripts" / "check_review_contract.py"), str(path)])
        elif path.name.startswith("review_"):
            failures += run([sys.executable, str(ROOT / "scripts" / "lint_structured_review.py"), str(path)])
        else:
            print(f"Skipping unrecognized fixture: {path.name}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
