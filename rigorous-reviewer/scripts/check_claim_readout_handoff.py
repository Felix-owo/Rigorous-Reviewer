#!/usr/bin/env python3
"""Validate a cross-skill claim-readout handoff artifact."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_ROLES = {"decisive", "supporting", "contextual", "exploratory"}
ALLOWED_AUTHORITY = {
    "original",
    "local_validated",
    "external_benchmark",
    "vendor_manual",
    "institutional_sop",
    "recommended_unvalidated",
    "unresolved",
    "not_applicable",
}
ALLOWED_ACTIONS = {
    "add_control",
    "add_validation",
    "add_qc_gate",
    "narrow_claim",
    "mark_preliminary",
    "author_input_needed",
    "no_action_needed",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def substantive(value: Any, min_len: int = 4) -> bool:
    return isinstance(value, str) and len(value.strip()) >= min_len


def validate(data: Any) -> list[str]:
    if not isinstance(data, dict):
        return ["handoff must be a JSON object"]
    errors: list[str] = []
    if not substantive(data.get("handoff_id"), 3):
        errors.append("handoff_id must be a substantive string")
    if data.get("skill_context") not in {"rigorous-reviewer", "biological-protocol-reviewer", "cross-skill"}:
        errors.append("skill_context is invalid")
    items = data.get("claim_readout_map")
    if not isinstance(items, list) or not items:
        errors.append("claim_readout_map must be a non-empty array")
        return errors
    for idx, item in enumerate(items):
        path = f"claim_readout_map[{idx}]"
        if not isinstance(item, dict):
            errors.append(f"{path} must be an object")
            continue
        for key in [
            "claim_id",
            "claim_text",
            "readout_id",
            "readout_supports",
            "protocol_step_or_method",
            "qc_gate",
            "failure_mode",
            "manuscript_impact",
        ]:
            if not substantive(item.get(key), 2 if key in {"claim_id", "readout_id"} else 8):
                errors.append(f"{path}.{key} must be substantive")
        if item.get("evidence_role") not in ALLOWED_ROLES:
            errors.append(f"{path}.evidence_role is invalid")
        if item.get("parameter_authority") not in ALLOWED_AUTHORITY:
            errors.append(f"{path}.parameter_authority is invalid")
        if item.get("revision_action") not in ALLOWED_ACTIONS:
            errors.append(f"{path}.revision_action is invalid")
        if not isinstance(item.get("source_ids"), list) or not item["source_ids"]:
            errors.append(f"{path}.source_ids must be a non-empty array")
        if item.get("evidence_role") == "decisive":
            if item.get("parameter_authority") in {"recommended_unvalidated", "unresolved"}:
                if item.get("revision_action") not in {"add_validation", "add_qc_gate", "narrow_claim", "author_input_needed"}:
                    errors.append(f"{path}: decisive unresolved/unvalidated readout needs validation, QC, claim narrowing, or author input")
            if "control" not in str(item.get("qc_gate", "")).lower() and "对照" not in str(item.get("qc_gate", "")):
                errors.append(f"{path}: decisive readout qc_gate should name control logic")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("handoff", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        data = load_json(args.handoff)
    except Exception as exc:
        print(f"Invalid JSON input: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if args.json:
        print(json.dumps({"ok": not errors, "errors": errors}, indent=2, ensure_ascii=False))
    elif errors:
        print("Claim-readout handoff validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
    else:
        print("Claim-readout handoff validation passed.")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
