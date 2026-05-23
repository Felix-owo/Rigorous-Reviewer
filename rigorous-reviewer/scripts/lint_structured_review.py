#!/usr/bin/env python3
"""Validate a structured JSON Rigorous Reviewer report against the local schema.

The linter intentionally implements the small JSON Schema subset used by this
repository, so CI can run with only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SCHEMA_DIR = Path(__file__).resolve().parents[1] / "schemas"
DEFAULT_SCHEMA = SCHEMA_DIR / "review_report.schema.json"
SUPPORT_RE = re.compile(r"\b(support|supports|supporting|strengthen|strengthens|consistent with)\b|支持", re.I)
WEAKEN_RE = re.compile(r"\b(narrow|narrows|narrowing|weaken|weakens|refut|force narrowing)\b|削弱|反驳", re.I)
SOURCE_RE = re.compile(
    r"(doi|pmid|pmcid|arxiv|https?://|clinicaltrials|geo|sra|arrayexpress|"
    r"guideline|standard|benchmark|fixture:|synthetic:|dataset|accession|rrid|search target|manual|"
    r"chembl|bindingdb|chebi|cbioportal|civic|cellxgene|biostudies|alphafold|"
    r"pdb|uniprot|github|commit|zenodo|figshare|dryad|osf)",
    re.I,
)
COMPANION_IDENTIFIER_RE = re.compile(
    r"(doi:|pmid:|pmcid:|arxiv:|https?://|clinicaltrials|geo:|sra:|arrayexpress|"
    r"guideline|standard|benchmark:|fixture:|synthetic:|dataset|accession|rrid|manual|chembl|"
    r"bindingdb|chebi|cbioportal|civic|cellxgene|biostudies|alphafold|pdb|"
    r"uniprot|github|commit|zenodo|figshare|dryad|osf)",
    re.I,
)
VAGUE_IDENTIFIER_RE = re.compile(r"^(n/?a|none|unknown|not available|not found|unresolved|tbd|to be determined)$", re.I)
TRACEABILITY_FIELDS = {
    "artifact_ids",
    "manuscript_artifact_ids",
    "figure_id",
    "table_id",
    "method_id",
    "proof_step",
    "dataset_id",
    "code_artifact_id",
    "manuscript_location",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_ref(ref: str) -> dict[str, Any]:
    if "/" in ref or ref.startswith("#"):
        raise ValueError(f"unsupported schema reference: {ref}")
    return load_json(SCHEMA_DIR / ref)


def type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    return True


def validate_schema(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []

    if "$ref" in schema:
        schema = resolve_ref(schema["$ref"])

    expected_type = schema.get("type")
    if expected_type and not type_matches(value, expected_type):
        return [f"{path}: expected {expected_type}"]

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value must be one of {schema['enum']}")

    if isinstance(value, str) and "minLength" in schema and len(value.strip()) < schema["minLength"]:
        errors.append(f"{path}: string shorter than minLength {schema['minLength']}")

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: value below minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path}: value above maximum {schema['maximum']}")

    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing required field `{key}`")
        properties = schema.get("properties", {})
        for key, child_schema in properties.items():
            if key in value:
                errors.extend(validate_schema(value[key], child_schema, f"{path}.{key}"))

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path}: fewer than minItems {schema['minItems']}")
        item_schema = schema.get("items")
        if item_schema:
            for idx, item in enumerate(value):
                errors.extend(validate_schema(item, item_schema, f"{path}[{idx}]"))

    return errors


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def non_empty_string_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(non_empty_string(item) for item in value)


def issue_has_traceable_artifact(issue: dict[str, Any]) -> bool:
    for field in TRACEABILITY_FIELDS:
        value = issue.get(field)
        if non_empty_string(value) or non_empty_string_list(value):
            return True
    return False


def validate_strict_review(report: Any, schema: dict[str, Any]) -> list[str]:
    """Add review-specific checks beyond the portable schema subset."""
    if not isinstance(report, dict):
        return []

    errors: list[str] = []
    allowed_top_level = set(schema.get("properties", {}))
    unexpected = sorted(set(report) - allowed_top_level)
    if unexpected:
        errors.append(f"$: unexpected top-level fields in strict mode: {unexpected}")

    evidence_ledger = report.get("evidence_ledger", [])
    evidence_ids = {
        item.get("source_id")
        for item in evidence_ledger
        if isinstance(item, dict) and isinstance(item.get("source_id"), str)
    }

    claim_maturity_gate = report.get("claim_maturity_gate", [])
    claim_ids = {
        item.get("claim_id")
        for item in claim_maturity_gate
        if isinstance(item, dict) and isinstance(item.get("claim_id"), str)
    }

    contract_claims = report.get("pre_review_contract", {}).get("central_claim_dependency_map", [])
    contract_claim_ids = {
        item.get("claim_id")
        for item in contract_claims
        if isinstance(item, dict) and isinstance(item.get("claim_id"), str)
    }
    if claim_ids and contract_claim_ids:
        missing_from_contract = sorted(claim_ids - contract_claim_ids)
        if missing_from_contract:
            errors.append(f"$.claim_maturity_gate: claim_ids not present in pre_review_contract: {missing_from_contract}")

    issues = report.get("issues", [])
    critical_present = False
    if isinstance(issues, list):
        for idx, issue in enumerate(issues):
            if not isinstance(issue, dict):
                continue
            path = f"$.issues[{idx}]"
            severity = issue.get("severity")
            if severity == "Critical":
                critical_present = True

            source_ids = issue.get("source_ids")
            if not isinstance(source_ids, list) or not source_ids:
                errors.append(f"{path}: strict mode requires non-empty source_ids")
            elif evidence_ids:
                missing = [sid for sid in source_ids if sid not in evidence_ids]
                if missing:
                    errors.append(f"{path}: source_ids not present in evidence_ledger: {missing}")

            external_standard = str(issue.get("external_standard", ""))
            if not SOURCE_RE.search(external_standard):
                errors.append(f"{path}: external_standard needs an identifier, guideline, benchmark, or search target")

            decisive_readout = str(issue.get("decisive_readout", ""))
            if not SUPPORT_RE.search(decisive_readout):
                errors.append(f"{path}: decisive_readout lacks a support condition")
            if not WEAKEN_RE.search(decisive_readout):
                errors.append(f"{path}: decisive_readout lacks a weakening/refuting/narrowing condition")

            if severity in {"Critical", "Major"}:
                linked_claims = issue.get("linked_claims")
                if not non_empty_string_list(linked_claims):
                    errors.append(f"{path}: Critical/Major issues require non-empty linked_claims")
                elif claim_ids:
                    missing_claims = [claim for claim in linked_claims if claim not in claim_ids]
                    if missing_claims:
                        errors.append(f"{path}: linked_claims not present in claim_maturity_gate: {missing_claims}")
                if not issue_has_traceable_artifact(issue):
                    errors.append(
                        f"{path}: Critical/Major issues require a manuscript artifact trace "
                        "(manuscript_artifact_ids, figure_id, table_id, method_id, proof_step, "
                        "dataset_id, code_artifact_id, or manuscript_location)"
                    )

    companion_evidence = report.get("external_companion_evidence")
    if companion_evidence is not None:
        if not isinstance(companion_evidence, list):
            errors.append("$.external_companion_evidence: strict mode requires an array")
        else:
            for idx, item in enumerate(companion_evidence):
                path = f"$.external_companion_evidence[{idx}]"
                if not isinstance(item, dict):
                    errors.append(f"{path}: strict mode requires an object")
                    continue
                returned_identifier = str(item.get("returned_identifier", "")).strip()
                if VAGUE_IDENTIFIER_RE.match(returned_identifier):
                    errors.append(f"{path}: returned_identifier must not be vague or unresolved")
                elif not COMPANION_IDENTIFIER_RE.search(returned_identifier):
                    errors.append(
                        f"{path}: returned_identifier needs a concrete source, accession, DOI, URL, "
                        "repository, standard, benchmark, fixture, or database handle"
                    )

    recommendation = report.get("overall_recommendation")
    if critical_present and recommendation in {"Accept", "Minor Revision"}:
        errors.append("$: strict mode forbids Accept/Minor Revision when Critical issues remain")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_report", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--strict", action="store_true", help="Enable review-specific evidence and recommendation checks")
    args = parser.parse_args()

    try:
        report = load_json(args.json_report)
        schema = load_json(args.schema)
    except Exception as exc:
        print(f"Invalid JSON input: {exc}", file=sys.stderr)
        return 2

    errors = validate_schema(report, schema)
    if args.strict:
        errors.extend(validate_strict_review(report, schema))
    if errors:
        print("Structured review validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Structured review validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
