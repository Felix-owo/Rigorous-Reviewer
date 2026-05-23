#!/usr/bin/env python3
"""Validate the claim-strength calibration fixture.

The fixture is intentionally synthetic. This checker prevents it from becoming a
static, untested asset or from using fake citation-looking DOI handles.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_MD = REPO_ROOT / "rigorous-reviewer" / "SKILL.md"
VALID_SEVERITY_FLOORS = {"Minor Revision", "Major Revision", "Reject"}
SYNTHETIC_IDENTIFIER_RE = re.compile(r"^(benchmark|fixture|synthetic):[A-Za-z0-9_.:-]+$")
FAKE_DOI_RE = re.compile(r"\bDOI:10\.0000/", re.I)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def skill_version() -> str:
    text = SKILL_MD.read_text(encoding="utf-8")
    match = re.search(r'^  version:\s*"([^"]+)"', text, flags=re.MULTILINE)
    if not match:
        raise RuntimeError("metadata.version not found in SKILL.md")
    return f"rigorous-reviewer v{match.group(1)}"


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_fixture(fixture: Any, path: Path) -> list[str]:
    if not isinstance(fixture, dict):
        return ["fixture must be a JSON object"]

    errors: list[str] = []
    for key in [
        "fixture_id",
        "skill",
        "skill_version",
        "purpose",
        "central_claim",
        "available_evidence",
        "blocking_loopholes",
        "expected_reviewer_action",
    ]:
        if key not in fixture:
            errors.append(f"missing required field `{key}`")

    if fixture.get("skill") != "rigorous-reviewer":
        errors.append("skill must be rigorous-reviewer")

    expected_version = skill_version()
    if fixture.get("skill_version") != expected_version:
        errors.append(f"skill_version must be {expected_version!r}")

    raw_text = path.read_text(encoding="utf-8")
    if FAKE_DOI_RE.search(raw_text):
        errors.append("synthetic fixtures must not use fake DOI:10.0000 identifiers")

    central_claim = fixture.get("central_claim")
    if not isinstance(central_claim, dict):
        errors.append("central_claim must be an object")
    else:
        for key in ["claim_id", "text", "claimed_strength", "supported_strength"]:
            if not non_empty_string(central_claim.get(key)):
                errors.append(f"central_claim.{key} must be a non-empty string")

    evidence = fixture.get("available_evidence")
    source_ids: set[str] = set()
    if not isinstance(evidence, list) or not evidence:
        errors.append("available_evidence must be a non-empty array")
    else:
        for idx, item in enumerate(evidence):
            item_path = f"available_evidence[{idx}]"
            if not isinstance(item, dict):
                errors.append(f"{item_path} must be an object")
                continue
            source_id = item.get("source_id")
            if not non_empty_string(source_id):
                errors.append(f"{item_path}.source_id must be a non-empty string")
            else:
                source_ids.add(source_id)
            for key in ["source_type", "description"]:
                if not non_empty_string(item.get(key)):
                    errors.append(f"{item_path}.{key} must be a non-empty string")
            identifier = item.get("identifier")
            if identifier is not None and not SYNTHETIC_IDENTIFIER_RE.search(str(identifier)):
                errors.append(
                    f"{item_path}.identifier must use benchmark:, fixture:, or synthetic: for synthetic sources"
                )

    loopholes = fixture.get("blocking_loopholes")
    if not isinstance(loopholes, list) or len(loopholes) < 3:
        errors.append("blocking_loopholes must contain at least 3 loopholes")

    action = fixture.get("expected_reviewer_action")
    if not isinstance(action, dict):
        errors.append("expected_reviewer_action must be an object")
    else:
        if action.get("severity_floor") not in VALID_SEVERITY_FLOORS:
            errors.append(f"expected_reviewer_action.severity_floor must be one of {sorted(VALID_SEVERITY_FLOORS)}")
        for key in [
            "required_narrowing",
            "decisive_support_readout",
            "decisive_weakening_readout",
        ]:
            if not non_empty_string(action.get(key)):
                errors.append(f"expected_reviewer_action.{key} must be a non-empty string")

    if {"M1", "S1"} - source_ids:
        errors.append("available_evidence should include both manuscript-internal M1 and benchmark S1 sources")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        fixture = load_json(args.fixture)
    except Exception as exc:
        print(f"Invalid JSON input: {exc}", file=sys.stderr)
        return 2

    errors = validate_fixture(fixture, args.fixture)
    if args.json:
        print(json.dumps({"ok": not errors, "errors": errors}, indent=2, ensure_ascii=False))
    elif errors:
        print("Claim-strength fixture validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
    else:
        print("Claim-strength fixture validation passed.")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
