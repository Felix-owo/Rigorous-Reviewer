# Trigger Keyword Support

This overlay adds explicit trigger-keyword routing for `rigorous-reviewer`.

## Files added

- `rigorous-reviewer/templates/trigger_keywords.json` — machine-readable trigger registry.
- `rigorous-reviewer/references/trigger_keywords.md` — human-readable activation and negative-routing guide.
- `rigorous-reviewer/schemas/trigger_keywords.schema.json` — static schema for the registry.
- `rigorous-reviewer/scripts/apply_trigger_keywords.py` — deterministic patcher for `SKILL.md`.
- `tests/test_trigger_keywords.py` — unit tests for the registry and patcher.

## Maintain in v2.0.0

After editing trigger terms, run:

```bash
python rigorous-reviewer/scripts/apply_trigger_keywords.py --skill-md rigorous-reviewer/SKILL.md
```

Then verify:

```bash
python rigorous-reviewer/scripts/apply_trigger_keywords.py --skill-md rigorous-reviewer/SKILL.md --check
python rigorous-reviewer/scripts/check_installable_skill.py --skill-dir rigorous-reviewer
python -m unittest discover -s tests
```

## Why both JSON and Markdown?

Different agent hosts consume different metadata. The JSON file is suitable for installers, validators, and future host-specific metadata generation. The Markdown file is suitable for progressive disclosure and human review. The `SKILL.md` section makes the trigger rules visible to agents that only read the main skill file.
