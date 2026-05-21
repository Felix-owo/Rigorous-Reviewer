#!/usr/bin/env python3
"""Alias-aware semantic-lite scorer for Rigorous Reviewer benchmark outputs.

This scorer is deterministic and local-first. It does not call external embedding APIs.
It complements keyword scoring by allowing each expected concept to define aliases,
required evidence, and severity expectations.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

VALID_SEVERITIES = {"Critical": 3, "Major": 2, "Minor": 1}
VALID_RECOMMENDATIONS = {"Accept", "Minor Revision", "Major Revision", "Reject"}
DECISIVE_READOUT_TERMS = [
    "decisive experiment",
    "decisive readout",
    "orthogonal validation",
    "rescue experiment",
    "independent validation",
    "external validation",
    "ablation",
    "calibration",
    "replication",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9+/-]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def contains_phrase(text_norm: str, phrase: str) -> bool:
    phrase_norm = normalize(phrase)
    if not phrase_norm:
        return False
    return f" {phrase_norm} " in f" {text_norm} "


def parse_concept(raw: str | dict[str, Any]) -> tuple[str, list[str]]:
    if isinstance(raw, str):
        return raw, [raw]
    concept = str(raw.get("concept", "")).strip()
    aliases = [concept] + [str(a) for a in raw.get("aliases", [])]
    return concept, [a for a in aliases if a]


def score_concepts(text: str, must_detect: list[str | dict[str, Any]]) -> list[dict[str, Any]]:
    text_norm = normalize(text)
    scores: list[dict[str, Any]] = []
    for raw in must_detect:
        concept, aliases = parse_concept(raw)
        matched_aliases = [alias for alias in aliases if contains_phrase(text_norm, alias)]
        scores.append({"concept": concept, "matched": bool(matched_aliases), "matched_aliases": matched_aliases})
    return scores


def severity_ok(text: str, minimum_severity: str) -> bool:
    text_norm = normalize(text)
    required_rank = VALID_SEVERITIES[minimum_severity]
    return any(
        contains_phrase(text_norm, severity) and rank >= required_rank
        for severity, rank in VALID_SEVERITIES.items()
    )


def forbidden_recommendations(text: str, forbidden: list[str]) -> list[str]:
    text_norm = normalize(text)
    return [rec for rec in forbidden if contains_phrase(text_norm, rec)]


def has_decisive_readout(text: str) -> bool:
    text_norm = normalize(text)
    return any(contains_phrase(text_norm, term) for term in DECISIVE_READOUT_TERMS)


def score_output(text: str, spec: dict[str, Any], weights: dict[str, float]) -> dict[str, Any]:
    concept_scores = score_concepts(text, spec.get("must_detect", []))
    concept_recall = (
        sum(1 for score in concept_scores if score["matched"]) / len(concept_scores)
        if concept_scores else 1.0
    )
    sev_ok = severity_ok(text, spec.get("minimum_severity", "Minor"))
    forbidden = forbidden_recommendations(text, spec.get("forbidden_recommendations", []))
    decisive_ok = has_decisive_readout(text) if spec.get("requires_decisive_readout", True) else True

    score = (
        weights.get("concept_recall", 0.60) * concept_recall
        + weights.get("severity_calibration", 0.20) * float(sev_ok)
        + weights.get("decisive_readout", 0.10) * float(decisive_ok)
        + weights.get("recommendation_safety", 0.10) * float(not forbidden)
    )
    threshold = float(spec.get("pass_threshold", 0.80))
    return {
        "score": round(score, 4),
        "pass_threshold": threshold,
        "pass": score >= threshold,
        "concept_recall": round(concept_recall, 4),
        "concepts": concept_scores,
        "severity_ok": sev_ok,
        "decisive_readout_ok": decisive_ok,
        "forbidden_recommendations_found": forbidden,
    }


def check_definitions(root: Path) -> list[str]:
    errors: list[str] = []
    expected_path = root / "expected_findings.json"
    rubric_path = root / "scoring_rubric.json"
    cases_dir = root / "cases"
    sources_path = root / "sources.json"
    if not expected_path.exists():
        return [f"Missing {expected_path}"]
    if not rubric_path.exists():
        return [f"Missing {rubric_path}"]
    if not cases_dir.is_dir():
        return [f"Missing {cases_dir}"]
    expected = load_json(expected_path)
    rubric = load_json(rubric_path)
    weights = rubric.get("score_components", {})
    if not weights or abs(sum(float(v) for v in weights.values()) - 1.0) > 0.001:
        errors.append("scoring_rubric.json score_components must sum to 1.0")
    sources = load_json(sources_path) if sources_path.exists() else {}
    for case_id, spec in expected.items():
        if not (cases_dir / f"{case_id}.md").exists():
            errors.append(f"{case_id}: missing benchmark case file")
        if not spec.get("must_detect"):
            errors.append(f"{case_id}: must_detect must be non-empty")
        if spec.get("minimum_severity") not in VALID_SEVERITIES:
            errors.append(f"{case_id}: invalid minimum_severity")
        for recommendation in spec.get("forbidden_recommendations", []):
            if recommendation not in VALID_RECOMMENDATIONS:
                errors.append(f"{case_id}: invalid forbidden recommendation {recommendation}")
        if case_id not in sources:
            errors.append(f"{case_id}: missing public source record in sources.json")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--benchmark-root", type=Path, default=Path("benchmarks/v1.1-public"))
    parser.add_argument("--outputs-dir", type=Path, help="Directory containing .md model outputs to score")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    errors = check_definitions(args.benchmark_root)
    if errors:
        for error in errors:
            print(f"[ERROR] {error}", file=sys.stderr)
        return 1

    if not args.outputs_dir:
        print("Semantic benchmark definitions are valid.")
        return 0

    expected = load_json(args.benchmark_root / "expected_findings.json")
    weights = load_json(args.benchmark_root / "scoring_rubric.json").get("score_components", {})
    results = {}
    for case_id, spec in expected.items():
        output_path = args.outputs_dir / f"{case_id}.md"
        if not output_path.exists():
            results[case_id] = {"pass": False, "error": "missing output file"}
            continue
        results[case_id] = score_output(output_path.read_text(encoding="utf-8"), spec, weights)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for case_id, result in results.items():
            status = "PASS" if result.get("pass") else "FAIL"
            print(f"{status} {case_id}: score={result.get('score')} details={result}")
    return 0 if all(result.get("pass") for result in results.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
