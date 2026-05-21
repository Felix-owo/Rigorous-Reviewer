#!/usr/bin/env python3
"""Patch rigorous-reviewer/SKILL.md with explicit trigger keywords.

This script is deterministic and offline-only. It does not call network
services and does not modify files outside the provided SKILL.md path.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

START = "<!-- RR_TRIGGER_KEYWORDS_START -->"
END = "<!-- RR_TRIGGER_KEYWORDS_END -->"

def load_trigger_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("skill_name") != "rigorous-reviewer":
        raise ValueError(f"Unexpected skill_name in {path}")
    return data


def bullet_list(items: list[str], max_items: int | None = None) -> str:
    selected = items if max_items is None else items[:max_items]
    return "\n".join(f"- {item}" for item in selected)


def build_section(data: dict[str, Any]) -> str:
    strong = data.get("strong_trigger_keywords", [])
    chinese = data.get("chinese_trigger_keywords", [])
    negative = data.get("negative_routing_keywords", [])
    rules = data.get("routing_rules", [])

    rules_md = "\n".join(
        f"{idx}. **Condition:** {rule['condition']}\n   **Action:** {rule['action']}"
        for idx, rule in enumerate(rules, start=1)
    )

    return f"""{START}
## Trigger Keywords and Routing

Use this skill when the user asks for rigorous scientific peer review, claim stress-testing, evidence sufficiency assessment, novelty evaluation, hidden-loophole detection, or journal-level recommendation for manuscripts, preprints, proposals, datasets, figures, proofs, computational models, benchmarks, or code artifacts.

### Strong English triggers

{bullet_list(strong, 32)}

### Strong Chinese triggers

{bullet_list(chinese, 28)}

### Negative routing hints

Do **not** trigger `rigorous-reviewer` by default when the task is only about:

{bullet_list(negative, 18)}

### Routing precedence

{rules_md}

The complete trigger registry is stored in `templates/trigger_keywords.json`; the human-readable routing guide is `references/trigger_keywords.md`.
{END}
"""


def has_standard_multiline_frontmatter(text: str) -> bool:
    return text.startswith("---\n") and "\n---\n" in text[4:]


def find_section_insert_pos(text: str) -> int:
    """Prefer inserting after the H1 title; otherwise after frontmatter."""
    h1 = "# Rigorous Reviewer"
    h1_idx = text.find(h1)
    if h1_idx != -1:
        line_end = text.find("\n", h1_idx)
        return len(text) if line_end == -1 else line_end + 1

    if has_standard_multiline_frontmatter(text):
        close_idx = text.find("\n---\n", 4)
        if close_idx != -1:
            return close_idx + len("\n---\n")

    return 0


def add_or_replace_trigger_section(text: str, section: str) -> str:
    if START in text and END in text:
        start_idx = text.index(START)
        end_idx = text.index(END, start_idx) + len(END)
        replacement = section.strip()
        return text[:start_idx].rstrip() + "\n\n" + replacement + "\n\n" + text[end_idx:].lstrip()

    pos = find_section_insert_pos(text)
    return text[:pos].rstrip() + "\n\n" + section.strip() + "\n\n" + text[pos:].lstrip()


def patch_skill_text(text: str, trigger_data: dict[str, Any]) -> str:
    section = build_section(trigger_data)
    return add_or_replace_trigger_section(text, section)


def check_skill_text(text: str) -> list[str]:
    errors: list[str] = []
    required_terms = [
        START,
        END,
        "Trigger Keywords and Routing",
        "rigorous scientific peer review",
        "decisive evidence",
        "alternative explanation",
        "negative routing",
        "templates/trigger_keywords.json",
        "references/trigger_keywords.md",
    ]
    lower = text.lower()
    for term in required_terms:
        if term.lower() not in lower:
            errors.append(f"SKILL.md missing trigger routing term: {term}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-md", type=Path, default=Path("rigorous-reviewer/SKILL.md"))
    parser.add_argument("--trigger-json", type=Path, default=Path("rigorous-reviewer/templates/trigger_keywords.json"))
    parser.add_argument("--check", action="store_true", help="Check whether SKILL.md already contains trigger keywords.")
    parser.add_argument("--dry-run", action="store_true", help="Print the patched SKILL.md without writing.")
    args = parser.parse_args()

    if not args.skill_md.is_file():
        print(f"[ERROR] SKILL.md not found: {args.skill_md}", file=sys.stderr)
        return 2
    if not args.trigger_json.is_file():
        print(f"[ERROR] trigger keyword registry not found: {args.trigger_json}", file=sys.stderr)
        return 2

    text = args.skill_md.read_text(encoding="utf-8")
    if args.check:
        errors = check_skill_text(text)
        for error in errors:
            print(f"[ERROR] {error}", file=sys.stderr)
        return 1 if errors else 0

    trigger_data = load_trigger_json(args.trigger_json)
    patched = patch_skill_text(text, trigger_data)

    if args.dry_run:
        print(patched)
        return 0

    args.skill_md.write_text(patched, encoding="utf-8")
    errors = check_skill_text(patched)
    for error in errors:
        print(f"[ERROR] {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"Patched trigger keywords into {args.skill_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
