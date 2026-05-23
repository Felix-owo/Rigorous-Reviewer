# Final Verification Contract

Run this checklist before returning a rigorous-reviewer output or release artifact.

## Scientific Review Output

- The pre-review contract is locked before final recommendation.
- Every Critical/Major issue contains specific problem, seriousness, manuscript evidence, external standard/support, impact, loophole, resolution, and decisive readout.
- The evidence ledger maps source IDs to issues or revision actions.
- The recommendation is compatible with unresolved Critical/Major issues.
- No placeholder, invented citation, unsupported companion output, or generic review cliché remains.

## Package / File Output

If a package, template, fixture, or schema is modified, run the applicable local validators:

```bash
python -m py_compile rigorous-reviewer/scripts/*.py
python rigorous-reviewer/scripts/check_installable_skill.py --skill-dir rigorous-reviewer
python rigorous-reviewer/scripts/check_version_consistency.py
python rigorous-reviewer/scripts/apply_trigger_keywords.py --skill-md rigorous-reviewer/SKILL.md --check
python rigorous-reviewer/scripts/validate_review_report.py tests/fixtures/markdown/valid_review.md --strict
python rigorous-reviewer/scripts/lint_structured_review.py tests/fixtures/json/valid_structured_review.json --strict
python rigorous-reviewer/scripts/check_release_metadata.py
python -m unittest discover -s tests
```

Do not publish a release tag until the local checks and the GitHub Actions matrix pass.
