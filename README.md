# Rigorous Reviewer Portable Agent Skill

[中文版](README.zh-CN.md)

This repository contains a portable Agent Skill named `rigorous-reviewer`.
Codex is a supported host, but the installable skill folder is designed to be
usable by any agent runtime that supports the Agent Skills `SKILL.md` package
format.

It is designed for top-journal-level scientific peer review across six core
domains:

- Biology
- Chemistry
- Physics
- Mathematics
- Medicine
- Computer science / AI

It also focuses on interdisciplinary and fusion fields, including bioinformatics,
computational biology, chemical biology, medicinal chemistry, biophysics,
medical AI, computational chemistry, materials AI, mathematical biology, and
physics-informed machine learning.

## What It Does

`rigorous-reviewer` reviews manuscripts, proposals, preprints, figures,
methods, proofs, datasets, code artifacts, clinical models, algorithms, and
interdisciplinary claims.

It emphasizes:

- top-journal novelty and conceptual advance
- six-perspective reviewer-panel synthesis
- calibration against gold, near-gold, negative, and boundary papers
- optional bridge to K-Dense Scientific Agent Skills for paper lookup,
  database verification, literature review, and scientific critical thinking
- optional MCP capability routing for host-provided paper search, public
  database lookup, local document handling, GitHub/code inspection, and
  benchmark/evaluation tools
- decisive evidence thresholds by field
- hidden loophole and alternative-explanation detection
- professional issue blocks that force each reviewer comment to state the
  specific problem, seriousness, evidence, impact, loopholes, fix, and decisive
  readout
- Markdown report output with an evidence ledger and optional local `.md`
  validation when the user asks for a document
- schema-backed structured JSON validation when machine-readable review output
  is requested
- unit tests, golden fixtures, CI, and a synthetic versioned benchmark set for
  regression checks
- red-line failure checks against uncited, generic, duplicate, or non-decisive criticism
- Critical / Major / Minor severity grading
- article-specific field evidence maps
- reproducibility and auditability checks
- discipline-specific standards for experiments, proofs, chemistry
  characterization, physical measurement, clinical validation, benchmarks, and
  code/data artifacts

## Compatibility

The installable skill is the `rigorous-reviewer/` directory. It contains:

- `SKILL.md` with required name/description metadata and the core workflow
- `references/` for progressive-disclosure domain guidance
- `templates/` for review report and issue formatting
- `scripts/` and `schemas/` for deterministic validation
- `examples/` and `agents/openai.yaml` for host-facing examples and UI metadata

Other agent hosts can install this repository by copying or importing the
`rigorous-reviewer/` folder as a self-contained skill package. Host-specific
install commands vary; keep the full folder together so references, templates,
schemas, scripts, and examples remain available.

## Install In Codex

### Codex Conversation Install

For the stable release, ask Codex:

```text
Use $skill-installer to install https://github.com/Felix-owo/Rigorous-Reviewer/tree/v1.9.0/rigorous-reviewer
```

For the latest development version on `main`, ask:

```text
Use $skill-installer to install https://github.com/Felix-owo/Rigorous-Reviewer/tree/main/rigorous-reviewer
```

Then restart Codex so the skill is picked up.

### Command-Line Install

If you want to run the installed skill-installer helper directly:

```bash
python "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --url https://github.com/Felix-owo/Rigorous-Reviewer/tree/v1.9.0/rigorous-reviewer
```

Then restart Codex.

Use the `main` URL only if you want the newest unreleased changes.

### Slash-Command Note

Some Codex interfaces expose slash-command style launchers. This repository does
not define a custom `/install` command. If your client supports slash commands,
open the command launcher and run the equivalent skill-installer request above.
The reliable install mechanism is `$skill-installer` or its helper script.

## Repository Layout

```text
rigorous-reviewer/
├── agents/
│   └── openai.yaml
├── examples/
│   ├── full_review_example.md
│   └── issue_block_examples.md
├── SKILL.md
├── references/
│   ├── six_domain_review_standards.md
│   ├── reviewer_rigor_contract.md
│   ├── reviewer_panel_protocol.md
│   ├── calibration_protocol.md
│   ├── failure_mode_playbook.md
│   ├── external_scientific_skills_bridge.md
│   ├── mcp_capabilities.md
│   ├── article_specific_literature_mapping.md
│   ├── cns_reviewer_requirements.md
│   ├── reviewer_output_standards.md
│   └── rubric.json
├── scripts/
│   ├── validate_review_report.py
│   ├── lint_structured_review.py
│   └── score_benchmark.py
├── schemas/
│   ├── review_report.schema.json
│   ├── issue.schema.json
│   ├── evidence_ledger.schema.json
│   └── score.schema.json
└── templates/
    ├── comment_templates.json
    ├── review_report_template.md
    └── search_hints.json
```

Repository-level engineering checks live outside the installable skill folder:

```text
.github/workflows/validate.yml
tests/
benchmarks/v1.0/
```

The benchmark cases are synthetic and must not contain private manuscripts,
attachments, local paths, or user research material.

The `references/` and `templates/` files are part of the skill and should be
kept with `SKILL.md`.

The skill performs comprehensive full-paper review by default. It does not add
quick-review, partial-review, or re-review modes. The skill directory keeps only
agent-facing resources needed for the review workflow.

Markdown review reports are returned in chat by default. If a manuscript-specific
`.md` report is saved locally, it should remain local unless the user explicitly
asks to publish or push it.

## Optional MCP Capabilities

MCP support is optional and host-provided. This repository does not bundle or
require an MCP server. When an agent runtime exposes MCP tools, resources, or
prompts, `rigorous-reviewer` can use them through
`references/mcp_capabilities.md` for bounded support tasks:

- paper and citation search
- public scientific database verification
- web/search checks for official guidelines and public standards
- local filesystem/document parsing for PDFs, supplements, figures, code, and
  saved reports
- GitHub/code artifact inspection
- citation manager or bibliography normalization
- local benchmark, schema, and golden-fixture evaluation
- clinical/regulatory, math/proof, chemistry, and materials checks

MCP results are evidence inputs, not final reviewer judgment. The skill should
ask before sending confidential manuscripts, private attachments, local paths,
unpublished data, credentials, or personally identifying information to any
networked or third-party MCP service.

## Optional K-Dense Companion Skills

This skill can optionally call installed skills from
[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
through `references/external_scientific_skills_bridge.md`. This is an optional
bridge, not a hard dependency.

Recommended companion skills:

```text
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/paper-lookup
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/database-lookup
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/literature-review
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/scientific-critical-thinking
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/scholar-evaluation
```

When installed, these can support paper discovery, DOI/PMID/arXiv lookup,
public scientific database verification, GRADE/risk-of-bias thinking, and
secondary scoring checks. If they are not installed, `rigorous-reviewer`
uses its built-in search hints, calibration protocol, and red-line audit.

The K-Dense `peer-review` skill is not recommended as a default companion here
because it overlaps with this repository's core reviewer role and may create
trigger ambiguity. Use `rigorous-reviewer` as the primary peer-review
engine and the K-Dense skills above as bounded lookup or calibration helpers.

## Evidence Basis

The skill's review standards are anchored to established peer-review and
reporting guidance, including [Nature peer-review criteria](https://www.nature.com/nature/editorial-policies/peer-review),
[Nature Portfolio reporting standards for data/materials/code/protocols](https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards),
[ACS research data guidance](https://researcher-resources.acs.org/publish/data_guidelines),
[ACM artifact review and badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current),
[AMS Mathematical Reviews reviewer guidance](https://mathscinet.ams.org/mresubs/guide-reviewers.html),
and biological/medical reporting standards such as [CONSORT](https://pubmed.ncbi.nlm.nih.gov/20346629/),
[PRISMA](https://www.prisma-statement.org/prisma-2020),
[STROBE](https://www.strobe-statement.org/fileadmin/Strobe/uploads/checklists/STROBE_checklist_v4_combined.pdf),
[ARRIVE](https://arriveguidelines.org/arrive-guidelines),
[SPIRIT](https://www.spirit-statement.org/spirit-statement/), and
[TRIPOD](https://www.bmj.com/content/350/bmj.g7594).

The packaging and optional tool-routing design follows public Agent Skills and
MCP concepts: skills are distributed as `SKILL.md` folders with bundled
resources, while MCP separately exposes host-provided resources, prompts, and
tools for data access and actions.

## References and Acknowledgements

This repository was improved with reference to several public skill repositories:

- [mattpocock/skills](https://github.com/mattpocock/skills): repository
  structure inspiration, especially concise `SKILL.md` entrypoints, progressive
  disclosure, and task-focused supporting files.
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills):
  optional companion-skill ecosystem for paper lookup, database verification,
  literature review, and scientific critical thinking. Companion skills are
  installed separately and are not vendored into this repository.
- [tanweai/pua](https://github.com/tanweai/pua) and
  [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills):
  comparative references for agent-skill packaging and academic workflow
  presentation.

No third-party skill code is copied into this repository. External repositories
remain under their own licenses and should be installed or cited from their
original sources when used.

## License

MIT
