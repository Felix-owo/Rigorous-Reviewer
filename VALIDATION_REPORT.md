# Validation Report for Rigorous Reviewer v2.3.1 Validation Hardening Patch

This package was derived from the validated v2.3.0 clean replacement and hardened as v2.3.1.

## Included optimization targets

- `rigorous-reviewer/references/agent_behavior_core.md`
- `rigorous-reviewer/references/issue_traceability_and_scope_discipline.md`
- `rigorous-reviewer/references/final_verification_contract.md`
- `rigorous-reviewer/templates/review_report_template.md`
- `rigorous-reviewer/schemas/review_report.schema.json`
- `rigorous-reviewer/scripts/validate_review_report.py`
- `rigorous-reviewer/scripts/run_regression_fixtures.py`
- `benchmarks/fixtures/claim_strength_fixture.json`

## Expected local validation commands

```bash
python -m py_compile rigorous-reviewer/scripts/*.py
python rigorous-reviewer/scripts/check_installable_skill.py --skill-dir rigorous-reviewer
python rigorous-reviewer/scripts/check_version_consistency.py
python rigorous-reviewer/scripts/run_regression_fixtures.py
python rigorous-reviewer/scripts/apply_trigger_keywords.py --skill-md rigorous-reviewer/SKILL.md --check
python rigorous-reviewer/scripts/validate_review_report.py tests/fixtures/markdown/valid_review.md --strict
python rigorous-reviewer/scripts/validate_review_report.py rigorous-reviewer/examples/full_review_example.md
python rigorous-reviewer/scripts/lint_structured_review.py tests/fixtures/json/valid_structured_review.json --strict
python rigorous-reviewer/scripts/check_release_metadata.py
python rigorous-reviewer/scripts/check_claim_strength_fixture.py benchmarks/fixtures/claim_strength_fixture.json
python rigorous-reviewer/scripts/score_benchmark.py --benchmark-root benchmarks/v1.0
python rigorous-reviewer/scripts/score_benchmark_semantic.py --benchmark-root benchmarks/v1.1-public
python -m unittest discover -s tests
```

## Release note

Use this package as `v2.3.1`. It preserves the v2.3.0 clean replacement baseline and adds machine-checkable hardening for contract, claim-strength, traceability, and metadata drift.
