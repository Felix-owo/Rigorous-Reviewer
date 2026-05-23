#!/usr/bin/env python3
"""Validate a Rigorous Reviewer pre-review contract.

This checks structure and anti-drift fields. It does not judge scientific truth.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = [
    "review_id",
    "skill_version",
    "contract_status",
    "material_basis",
    "central_claim_dependency_map",
    "decisive_evidence_thresholds",
    "mandatory_reviewer_dimensions",
    "failure_conditions",
    "evidence_that_changes_recommendation",
    "prohibited_post_hoc_standard_shifts",
]
ALLOWED_STATUS = {"draft", "locked", "partial_material_contract", "amended"}
ALLOWED_SEVERITY_FLOOR = {"Minor Revision", "Major Revision", "Reject"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(contract: Any) -> list[str]:
    if not isinstance(contract, dict):
        return ["contract must be a JSON object"]

    errors: list[str] = []
    for key in REQUIRED_TOP_LEVEL:
        if key not in contract:
            errors.append(f"missing required field `{key}`")

    status = contract.get("contract_status")
    if status not in ALLOWED_STATUS:
        errors.append(f"contract_status must be one of {sorted(ALLOWED_STATUS)}")

    material_basis = contract.get("material_basis")
    if not isinstance(material_basis, dict):
        errors.append("material_basis must be an object")
    else:
        for key in ["materials_available", "missing_decisive_material"]:
            if not isinstance(material_basis.get(key), list):
                errors.append(f"material_basis.{key} must be an array")
        if status == "partial_material_contract" and not material_basis.get("missing_decisive_material"):
            errors.append("partial_material_contract requires missing_decisive_material")

    claims = contract.get("central_claim_dependency_map")
    claim_ids: set[str] = set()
    if not isinstance(claims, list) or not claims:
        errors.append("central_claim_dependency_map must be a non-empty array")
    else:
        for idx, claim in enumerate(claims):
            path = f"central_claim_dependency_map[{idx}]"
            if not isinstance(claim, dict):
                errors.append(f"{path} must be an object")
                continue
            claim_id = claim.get("claim_id")
            if not non_empty_string(claim_id):
                errors.append(f"{path}.claim_id is required")
            else:
                claim_ids.add(claim_id)
            for key in ["claim", "decisive_evidence_needed"]:
                if not non_empty_string(claim.get(key)) or len(claim[key].strip()) < 8:
                    errors.append(f"{path}.{key} must be a substantive string")

    thresholds = contract.get("decisive_evidence_thresholds")
    if not isinstance(thresholds, list) or not thresholds:
        errors.append("decisive_evidence_thresholds must be a non-empty array")
    else:
        for idx, threshold in enumerate(thresholds):
            path = f"decisive_evidence_thresholds[{idx}]"
            if not isinstance(threshold, dict):
                errors.append(f"{path} must be an object")
                continue
            claim_id = threshold.get("claim_id")
            if claim_ids and claim_id not in claim_ids:
                errors.append(f"{path}.claim_id does not match a central claim")
            for key in ["support_condition", "weakening_or_refuting_condition", "claim_narrowing_condition"]:
                if not non_empty_string(threshold.get(key)) or len(threshold[key].strip()) < 8:
                    errors.append(f"{path}.{key} must be a substantive string")

    dimensions = contract.get("mandatory_reviewer_dimensions")
    if not isinstance(dimensions, list) or len(dimensions) < 3:
        errors.append("mandatory_reviewer_dimensions must contain at least 3 dimensions")

    failures = contract.get("failure_conditions")
    if not isinstance(failures, list) or not failures:
        errors.append("failure_conditions must be a non-empty array")
    else:
        for idx, condition in enumerate(failures):
            path = f"failure_conditions[{idx}]"
            if not isinstance(condition, dict):
                errors.append(f"{path} must be an object")
                continue
            if condition.get("severity_floor") not in ALLOWED_SEVERITY_FLOOR:
                errors.append(f"{path}.severity_floor must be one of {sorted(ALLOWED_SEVERITY_FLOOR)}")
            if claim_ids and condition.get("affected_claim_id") not in claim_ids:
                errors.append(f"{path}.affected_claim_id does not match a central claim")
            if not non_empty_string(condition.get("condition")) or len(condition["condition"].strip()) < 8:
                errors.append(f"{path}.condition must be a substantive string")

    changes = contract.get("evidence_that_changes_recommendation")
    if not isinstance(changes, dict):
        errors.append("evidence_that_changes_recommendation must be an object")
    else:
        for key in ["strengthen", "weaken", "force_claim_narrowing"]:
            if not isinstance(changes.get(key), list):
                errors.append(f"evidence_that_changes_recommendation.{key} must be an array")

    shifts = contract.get("prohibited_post_hoc_standard_shifts")
    if not isinstance(shifts, list) or not shifts:
        errors.append("prohibited_post_hoc_standard_shifts must be a non-empty array")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        contract = load_json(args.contract)
    except Exception as exc:
        print(f"Invalid JSON input: {exc}", file=sys.stderr)
        return 2

    errors = validate(contract)
    if args.json:
        print(json.dumps({"ok": not errors, "errors": errors}, indent=2, ensure_ascii=False))
    elif errors:
        print("Review contract validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
    else:
        print("Review contract validation passed.")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
