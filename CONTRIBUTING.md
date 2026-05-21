# Contributing

Contributions should improve the skill as a rigorous, auditable scientific reviewer rather than a generic writing assistant.

## Contribution rules

1. Preserve task boundaries: `rigorous-reviewer` reviews scientific claims; it should not become a general manuscript-writing or protocol-rewriting skill.
2. Do not add private manuscripts, unpublished user data, local paths, credentials, or copyrighted full-text papers to tests or benchmarks.
3. Public benchmark cases should use public-source case cards, short paraphrases, and source metadata rather than long quoted text.
4. Every new benchmark case must include expected findings, minimum severity, forbidden recommendations, and at least one source record.
5. Every new script must be local-first, deterministic, and safe to run in CI.

## Local validation

```bash
python -m py_compile rigorous-reviewer/scripts/*.py
python rigorous-reviewer/scripts/check_installable_skill.py --skill-dir rigorous-reviewer
python rigorous-reviewer/scripts/apply_trigger_keywords.py --skill-md rigorous-reviewer/SKILL.md --check
python rigorous-reviewer/scripts/score_benchmark.py --benchmark-root benchmarks/v1.0
python rigorous-reviewer/scripts/score_benchmark_semantic.py --benchmark-root benchmarks/v1.1-public
python -m unittest discover -s tests
```

Optional development stack:

```bash
python -m pip install -r requirements-dev.txt
pytest
ruff check .
```

## Pull request checklist

- [ ] `SKILL.md` metadata still parses and has a specific trigger boundary.
- [ ] Trigger keyword registry and embedded `SKILL.md` trigger block are synchronized.
- [ ] JSON files are valid.
- [ ] Python scripts compile on Python 3.10, 3.11, and 3.12.
- [ ] Markdown fixtures validate.
- [ ] Benchmark definitions validate.
- [ ] New benchmark cases contain no private or copyrighted full-text content.
- [ ] README or compatibility docs are updated if installation behavior changes.
