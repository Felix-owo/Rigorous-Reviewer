#!/usr/bin/env python3
"""Check release metadata consistency for Rigorous Reviewer."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "rigorous-reviewer" / "SKILL.md"
README = ROOT / "README.md"
README_ZH = ROOT / "README.zh-CN.md"
PYPROJECT = ROOT / "pyproject.toml"
CHANGELOG = ROOT / "CHANGELOG.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def skill_version() -> str:
    text = read(SKILL)
    m = re.search(r'version:\s*["\']([^"\']+)["\']', text)
    if not m:
        raise SystemExit("Could not find SKILL.md metadata.version")
    return m.group(1)


def main() -> int:
    version = skill_version()
    expected_tag = f"v{version}"
    errors: list[str] = []

    for path in [README, README_ZH, PYPROJECT, CHANGELOG]:
        if not path.exists():
            errors.append(f"Missing release metadata file: {path}")
            continue
        text = read(path)
        if "License-MIT" in text or "License: MIT" in text or "MIT。见 `LICENSE`" in text or "MIT. See `LICENSE`" in text:
            errors.append(f"Old MIT license text remains in {path}")
        if "v2.1.3" in text and path.name != "CHANGELOG.md":
            errors.append(f"Old v2.1.3 user-facing metadata remains in {path}")

    pyproject = read(PYPROJECT)
    if f'version = "{version}"' not in pyproject:
        errors.append("pyproject.toml version does not match SKILL.md")
    if 'license = { text = "MPL-2.0" }' not in pyproject:
        errors.append("pyproject.toml license is not MPL-2.0")
    if "Mozilla Public License 2.0" not in pyproject:
        errors.append("pyproject.toml classifier is not MPL-2.0")

    for path in [README, README_ZH, CHANGELOG]:
        if expected_tag not in read(path):
            errors.append(f"{expected_tag} missing from {path}")

    if errors:
        for error in errors:
            print("Error:", error, file=sys.stderr)
        return 1
    print(f"Release metadata checker: PASS ({expected_tag}, MPL-2.0)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
