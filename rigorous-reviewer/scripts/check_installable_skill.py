#!/usr/bin/env python3
"""Smoke-test the installable rigorous-reviewer skill folder.

This checker verifies that the installable skill directory is self-contained
enough for cross-agent installation. It intentionally performs static checks
only and does not call network services.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_DIRS = ["references", "templates", "scripts", "schemas", "examples", "agents"]

REQUIRED_FILES = [
    "SKILL.md",
    "references/rubric.json",
    "references/reviewer_rigor_contract.md",
    "references/trigger_keywords.md",
    "references/mcp_tool_use_policy.md",
    "templates/review_report_template.md",
    "templates/trigger_keywords.json",
    "scripts/validate_review_report.py",
    "scripts/lint_structured_review.py",
    "scripts/score_benchmark.py",
    "scripts/score_benchmark_semantic.py",
    "scripts/apply_trigger_keywords.py",
    "scripts/check_installable_skill.py",
    "schemas/review_report.schema.json",
    "schemas/issue.schema.json",
    "schemas/evidence_ledger.schema.json",
    "schemas/trigger_keywords.schema.json",
    "agents/openai.yaml",
]

DESCRIPTION_TRIGGER_TERMS = ["review", "manuscript", "claim", "evidence", "novelty"]


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        raise ValueError("SKILL.md must start with YAML frontmatter delimiter '---'")

    if text.startswith("---\n"):
        close_idx = text.find("\n---\n", 4)
        if close_idx == -1:
            raise ValueError("SKILL.md frontmatter must be closed by a second '---' delimiter")
        header = text[4:close_idx]
    else:
        h1_idx = text.find("# Rigorous Reviewer")
        header = text[:h1_idx] if h1_idx != -1 else text[:1000]

    data: dict[str, str] = {}
    for line in header.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            key, value = match.groups()
            data[key] = value.strip().strip('"\'')
    if data.get("description") in {"", ">", "|"}:
        desc_match = re.search(
            r"^description:\s*[>|]?\s*\n(?P<body>(?:^[ \t]+.*\n?)+)",
            header,
            flags=re.MULTILINE,
        )
        if desc_match:
            data["description"] = re.sub(r"\s+", " ", desc_match.group("body")).strip()
    if "name" not in data:
        inline = re.search(r"---\s*name:\s*([A-Za-z0-9_-]+)", header)
        if inline:
            data["name"] = inline.group(1)
    if "description" not in data:
        inline = re.search(r"description:\s*>?\s*(.+?)(?:\s+metadata:|\s+---|$)", header, re.DOTALL)
        if inline:
            data["description"] = re.sub(r"\s+", " ", inline.group(1)).strip()
    return data


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    if not skill_dir.exists():
        return [f"Skill directory does not exist: {skill_dir}"]

    for dirname in REQUIRED_DIRS:
        if not (skill_dir / dirname).is_dir():
            errors.append(f"Missing required directory: {dirname}")

    for filename in REQUIRED_FILES:
        if not (skill_dir / filename).is_file():
            errors.append(f"Missing required file: {filename}")

    skill_md = skill_dir / "SKILL.md"
    if skill_md.exists():
        text = skill_md.read_text(encoding="utf-8")
        try:
            meta = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(str(exc))
        else:
            if meta.get("name") != "rigorous-reviewer":
                errors.append("SKILL.md frontmatter name must be 'rigorous-reviewer'")
            description = meta.get("description", "")
            if len(description) < 80:
                errors.append("SKILL.md description is too short for reliable trigger routing")
            missing_terms = [term for term in DESCRIPTION_TRIGGER_TERMS if term not in description.lower()]
            if missing_terms:
                errors.append(f"SKILL.md description lacks trigger terms: {missing_terms}")

        trigger_required = [
            "Trigger Keywords and Routing",
            "decisive evidence",
            "alternative explanation",
            "templates/trigger_keywords.json",
            "references/trigger_keywords.md",
        ]
        missing_trigger_terms = [term for term in trigger_required if term.lower() not in text.lower()]
        if missing_trigger_terms:
            errors.append(
                "SKILL.md is missing trigger keyword routing section. "
                "Run: python rigorous-reviewer/scripts/apply_trigger_keywords.py --skill-md rigorous-reviewer/SKILL.md. "
                f"Missing: {missing_trigger_terms}"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-dir", type=Path, default=Path("rigorous-reviewer"))
    args = parser.parse_args()

    errors = validate_skill(args.skill_dir)
    if errors:
        for error in errors:
            print(f"[ERROR] {error}", file=sys.stderr)
        return 1

    print(f"Installable skill smoke test passed: {args.skill_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
