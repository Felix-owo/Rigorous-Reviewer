#!/usr/bin/env python3
"""Check release metadata consistency for rigorous-reviewer.

This script validates repository metadata that has drifted in previous releases:
README badges and install URLs, pyproject version/license, changelog top entry,
benchmark latest version, documentation references, validation report, agent
metadata, and synthetic fixture version/identifier hygiene.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = REPO_ROOT / "rigorous-reviewer"
VERSIONED_TEXT_FILES = [
    "README.md",
    "README.zh-CN.md",
    "docs/compatibility/agent_matrix.md",
    "docs/routing/trigger_keyword_support.md",
    "VALIDATION_REPORT.md",
]
FORBIDDEN_RELEASE_MARKERS = [
    "License-MIT",
    "License: MIT",
    "tree/v2.1.3/rigorous-reviewer",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def skill_version() -> str:
    text = read(SKILL_DIR / "SKILL.md")
    match = re.search(r'^  version:\s*"([^"]+)"', text, flags=re.MULTILINE)
    if not match:
        raise RuntimeError("metadata.version not found in SKILL.md")
    return match.group(1)


def require_contains(errors: list[str], rel: str, text: str, markers: list[str]) -> None:
    for marker in markers:
        if marker not in text:
            errors.append(f"{rel} missing {marker!r}")


def reject_contains(errors: list[str], rel: str, text: str, markers: list[str]) -> None:
    for marker in markers:
        if marker in text:
            errors.append(f"{rel} contains stale marker {marker!r}")


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
        require_contains(
            errors,
            rel,
            text,
            ["License-MPL--2.0", "License: MPL-2.0", f"Version-{tag}", f"tree/{tag}/rigorous-reviewer"],
        )
        reject_contains(errors, rel, text, FORBIDDEN_RELEASE_MARKERS)

    for rel in VERSIONED_TEXT_FILES:
        text = read(REPO_ROOT / rel)
        if tag not in text:
            errors.append(f"{rel} must mention current tag {tag}")

    agent = read(SKILL_DIR / "agents" / "openai.yaml")
    for required in ["Rigorous Reviewer", "pre-review contract", "claim maturity gate", "evidence ledger"]:
        if required not in agent:
            errors.append(f"agents/openai.yaml missing expected metadata phrase {required!r}")

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
    if not any(item.get("version") == tag for item in benchmark.get("results", [])):
        errors.append(f"benchmarks/benchmark_results.json missing result row for {tag}")

    leaderboard = read(REPO_ROOT / "benchmarks" / "leaderboard.md")
    if f"| {tag} |" not in leaderboard:
        errors.append(f"benchmarks/leaderboard.md missing row for {tag}")

    expected = f"rigorous-reviewer {tag}"
    for rel in [
        "templates/review_contract_template.json",
        "examples/regression_fixtures/review_strong_sop_overclaimed_manuscript.json",
        "examples/regression_fixtures/contract_valid_claim_dependency.json",
    ]:
        text = read(SKILL_DIR / rel)
        if expected not in text:
            errors.append(f"{rel} does not contain {expected!r}")

    claim_fixture = json.loads(read(REPO_ROOT / "benchmarks" / "fixtures" / "claim_strength_fixture.json"))
    if claim_fixture.get("skill_version") != expected:
        errors.append("benchmarks/fixtures/claim_strength_fixture.json skill_version does not match SKILL.md")
    if "DOI:10.0000" in json.dumps(claim_fixture):
        errors.append("claim_strength_fixture.json still contains a fake DOI handle")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}", file=sys.stderr)
        return 1
    print(f"Release metadata consistency passed: rigorous-reviewer {tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
