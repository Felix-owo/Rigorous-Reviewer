# Changelog

## v2.3.0

- Clean replacement release built from the validated v2.1.3 baseline to avoid schema/validator drift introduced by partial hotfixes.
- Switches repository and skill metadata license to MPL-2.0.
- Adds scoped agent-behavior, issue-traceability, and final-verification reference modules.
- Synchronizes README, Chinese README, docs, benchmarks, templates, fixtures, pyproject metadata, and release metadata checks.
- Preserves the v2.1.3 strict Markdown validator, rich structured-review schema, strict JSON linter, benchmark validators, trigger overlay system, and unit-test suite.

## v2.1.3

- Adds Agent Skill package compliance checks for version consistency across
  `SKILL.md`, templates, and regression fixtures.
- Adds regression fixtures for the pre-review contract, claim-maturity gate, and
  cross-skill claim-readout handoff introduced after v2.1.0.
- Updates CI-facing validation so installability checks also execute the
  package version consistency gate.

## v2.1.0

- Expands `references/external_scientific_skills_bridge.md` into a general companion capability bridge covering K-Dense, official Life Science Research, bioinformatics, simulation, writing/output, design, and software-engineering companions.
- Adds optional structured `external_companion_evidence` schema support and strict linter checks so companion outputs must retain concrete source, database, repository, accession, or standard identifiers.
- Adds lookup-only negative routing terms and evidence-review weak triggers for database-backed, omics, variant, drug-target, and code-artifact review requests.
- Updates README companion ecosystem guidance, install links, benchmark metadata, and installability checks for the v2.1.0 release.

## v2.0.2

- Fixes the trigger keyword portability test so CI uses a cross-platform temporary directory instead of the macOS-only `/private/tmp` path.
- Supersedes v2.0.1, whose code changes were valid locally but whose CI test fixture was not portable to Ubuntu runners.

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
