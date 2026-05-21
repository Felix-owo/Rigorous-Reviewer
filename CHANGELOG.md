# Changelog

## v2.0.1

- Fixes `apply_trigger_keywords.py` so its default trigger registry follows the provided `SKILL.md` path and works from any current working directory.
- Adds bilingual Markdown issue-label validation and avoids false placeholder failures on mathematical comparison text.
- Adds strict structured-review linting for source IDs, evidence-ledger linkage, decisive-readout logic, external evidence handles, and unsafe recommendations with unresolved Critical issues.
- Reduces activation-time resource loading by moving rubric and templates to phase-gated loading.
- Updates CI, docs, tests, and benchmark metadata for the stricter validation path.

## v2.0.0

- Adds host-neutral English/Chinese trigger routing in `SKILL.md`, `references/trigger_keywords.md`, and `templates/trigger_keywords.json`.
- Replaces the older MCP capability note with a stricter `references/mcp_tool_use_policy.md` that keeps MCP tools as evidence-gathering helpers, not reviewer decision-makers.
- Adds public-source benchmark track `benchmarks/v1.1-public/` and deterministic semantic-lite scorer.
- Adds installable skill smoke checks, compatibility documentation, security policy, and contribution rules.
- Expands CI to validate Python 3.10, 3.11, and 3.12 with JSON, installability, trigger, fixture, schema, benchmark, and unit-test checks.

## v1.9.0

- Added schema-backed structured review validation, Markdown review fixtures, golden-output fixtures, and synthetic benchmark definitions.
- Added top-journal issue-block standards, reviewer-panel protocol, calibration protocol, and red-line failure-mode playbook.
