# Multi-Agent Compatibility Matrix

This matrix records installability and behavior expectations for the `rigorous-reviewer/` skill folder.

| Host / installer | Status | Install path or command | Expected behavior | Smoke-test evidence |
|---|---|---|---|---|
| Codex `$skill-installer` | Supported | `Use $skill-installer to install https://github.com/Felix-owo/Rigorous-Reviewer/tree/v2.0.2/rigorous-reviewer` | Host imports `SKILL.md`, references, templates, schemas, scripts, examples, and agent metadata. | Run `check_installable_skill.py` locally before release. |
| Manual copy | Supported | Copy `rigorous-reviewer/` into the host skill directory. | The folder remains self-contained; relative references resolve. | Run `check_installable_skill.py --skill-dir rigorous-reviewer`. |
| Claude Code | Expected compatible | Copy/import `rigorous-reviewer/` as an Agent Skill folder. | Host uses `name` and `description` frontmatter to trigger full skill loading. | Manual host test recommended before release badge. |
| OpenCode | Expected compatible | Copy/import `rigorous-reviewer/` as an Agent Skill folder. | Same `SKILL.md` package semantics; scripts remain optional. | Manual host test recommended. |
| Cursor | Expected compatible | Import folder if the host supports open agent skills or custom skill folders. | Use as a prompt/resource package; scripts may be unavailable. | Manual host test recommended. |
| `npx skills add` | Candidate | `npx skills add Felix-owo/Rigorous-Reviewer --skill rigorous-reviewer` if recognized by the CLI. | Installer should find the `rigorous-reviewer/` folder and copy bundled resources. | Add once the installer recognizes repo layout. |
| MCP-capable hosts | Optional support | Host-specific MCP configuration. | MCP tools provide bounded evidence inputs only; final reviewer judgment remains local to the skill. | Verify no private data is sent without user consent. |

## Compatibility invariants

A host is considered compatible if:

1. it can read `rigorous-reviewer/SKILL.md`;
2. it can preserve the full folder with `references/`, `templates/`, `schemas/`, `scripts/`, `examples/`, and `agents/`;
3. it treats scripts as optional enhancements, not mandatory runtime dependencies;
4. it respects the skill description as the trigger boundary;
5. it does not send private manuscripts or local paths to networked tools without explicit user approval.

## Release checklist

- [ ] Run `python rigorous-reviewer/scripts/check_installable_skill.py --skill-dir rigorous-reviewer`.
- [ ] Install in Codex via `$skill-installer`.
- [ ] Manually verify `SKILL.md` trigger and references load.
- [ ] Test at least one Markdown report validation.
- [ ] Test at least one structured JSON report validation.
- [ ] Document unsupported hosts explicitly rather than assuming compatibility.


## Trigger keyword compatibility

`rigorous-reviewer` now includes host-neutral trigger hints in three layers:

1. `SKILL.md` Markdown section: works with hosts that only load the main skill instructions.
2. `templates/trigger_keywords.json`: works with installers, validation scripts, or future host-specific metadata generators.
3. `references/trigger_keywords.md`: works with progressive-disclosure agents and human maintainers.

The trigger list intentionally includes both English and Chinese phrases because many high-value review requests are bilingual or use mixed terminology such as `CNS审稿`, `reviewer 2`, `central claim`, and `决定性证据`.
