#!/usr/bin/env python3
"""Check release metadata consistency for rigorous-reviewer.

This script intentionally validates only repository metadata that has drifted in
previous releases: README badges and install URLs, pyproject version/license,
changelog top entry, benchmark latest version, and root LICENSE.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = REPO_ROOT / "rigorous-reviewer"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def skill_version() -> str:
    text = read(SKILL_DIR / "SKILL.md")
    match = re.search(r'^  version:\s*"([^"]+)"', text, flags=re.MULTILINE)
    if not match:
        raise RuntimeError("metadata.version not found in SKILL.md")
    return match.group(1)


def main() -> int:
    errors: list[str] = []
    version = skill_version()
    tag = f"v{version}"

    skill_text = read(SKILL_DIR / "SKILL.md")
    if "license: MPL-2.0" not in skill_text:
        errors.append("SKILL.md license must be MPL-2.0")

    license_text = read(REPO_ROOT / "LICENSE")
    if not license_text.startswith("Mozilla Public License Version 2.0"):
        errors.append("Root LICENSE must contain MPL-2.0 text")

    for rel in ["README.md", "README.zh-CN.md"]:
        text = read(REPO_ROOT / rel)
        for required in ["License-MPL--2.0", "License: MPL-2.0", f"Version-{tag}", f"tree/{tag}/rigorous-reviewer"]:
            if required not in text:
                errors.append(f"{rel} missing {required!r}")
        for forbidden in ["License-MIT", "License: MIT", "tree/v2.1.3/rigorous-reviewer"]:
            if forbidden in text:
                errors.append(f"{rel} contains stale marker {forbidden!r}")

    pyproject = read(REPO_ROOT / "pyproject.toml")
    if f'version = "{version}"' not in pyproject:
        errors.append("pyproject.toml version does not match SKILL.md")
    if 'license = { text = "MPL-2.0" }' not in pyproject:
        errors.append("pyproject.toml license must be MPL-2.0")
    if "MIT License" in pyproject:
        errors.append("pyproject.toml still contains MIT classifier")

    changelog = read(REPO_ROOT / "CHANGELOG.md")
    if not re.search(rf"^##\s+{re.escape(tag)}\s*$", changelog, flags=re.MULTILINE):
        errors.append(f"CHANGELOG.md missing top-level entry for {tag}")

    benchmark = json.loads(read(REPO_ROOT / "benchmarks" / "benchmark_results.json"))
    if benchmark.get("latest_evaluated_version") != tag:
        errors.append("benchmarks/benchmark_results.json latest_evaluated_version does not match SKILL.md")

    contract = read(SKILL_DIR / "templates" / "review_contract_template.json")
    regression = read(SKILL_DIR / "examples" / "regression_fixtures" / "review_strong_sop_overclaimed_manuscript.json")
    expected = f"rigorous-reviewer {tag}"
    for rel, text in [
        ("templates/review_contract_template.json", contract),
        ("examples/regression_fixtures/review_strong_sop_overclaimed_manuscript.json", regression),
    ]:
        if expected not in text:
            errors.append(f"{rel} does not contain {expected!r}")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}", file=sys.stderr)
        return 1
    print(f"Release metadata consistency passed: rigorous-reviewer {tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
