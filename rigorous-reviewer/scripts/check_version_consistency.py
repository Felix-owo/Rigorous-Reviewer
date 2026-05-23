#!/usr/bin/env python3
"""Check rigorous-reviewer version consistency across package files."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "rigorous-reviewer"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []
    skill_md = read(ROOT / "SKILL.md")
    match = re.search(r"^  version:\s*\"([^\"]+)\"", skill_md, flags=re.MULTILINE)
    version = match.group(1) if match else None
    if not version:
        errors.append("Could not find metadata.version in SKILL.md")
        version = "UNKNOWN"

    expected = f"{SKILL_NAME} v{version}"
    for relpath in [
        "templates/review_contract_template.json",
        "examples/regression_fixtures/review_strong_sop_overclaimed_manuscript.json",
        "examples/regression_fixtures/contract_valid_claim_dependency.json",
    ]:
        if expected not in read(ROOT / relpath):
            errors.append(f"{relpath} does not contain {expected!r}")

    stale_markers = ["2.1.2"]
    for path in ROOT.rglob("*"):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        if path.name == "check_version_consistency.py":
            continue
        if path.suffix in {".pyc", ".png", ".jpg", ".jpeg", ".pdf"}:
            continue
        text = read(path)
        for marker in stale_markers:
            if marker in text:
                errors.append(f"stale marker {marker!r} found in {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}", file=sys.stderr)
        return 1
    print(f"Version consistency passed: {SKILL_NAME} v{version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
