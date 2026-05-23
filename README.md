# Rigorous Reviewer

[中文版](README.zh-CN.md)

[![License: MPL-2.0](https://img.shields.io/badge/License-MPL--2.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Standard-Agent_Skills-blueviolet.svg)](https://agentskills.io/specification)
[![Version](https://img.shields.io/badge/Version-v2.3.0-blue.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.10--3.12-3776AB.svg)](pyproject.toml)
[![Works with](https://img.shields.io/badge/Works_with-Codex_%7C_Claude_Code_%7C_Cursor-blue.svg)](docs/compatibility/agent_matrix.md)

`Rigorous Reviewer` is a portable Agent Skill for elite scientific peer review.
It turns a compatible agent host into a top-journal-style reviewer for
manuscripts, proposals, preprints, figures, methods, proofs, datasets, code
artifacts, models, and interdisciplinary scientific claims.

Codex is a validated host, but the installable skill folder is designed to work
with any agent runtime that supports the open
[Agent Skills](https://agentskills.io/specification) package format. The skill
is MCP-aware but does not require or bundle an MCP server.

## What's Included

This repository provides one installable skill package, `rigorous-reviewer/`,
plus release engineering assets that make the skill auditable and regression
resistant.

- **Top-journal review workflow**: six reviewer perspectives, claim dependency
  analysis, novelty calibration, decisive evidence thresholds, and final
  Accept / Minor Revision / Major Revision / Reject recommendation logic.
- **Six-domain coverage**: biology, chemistry, physics, mathematics, medicine,
  computer science / AI, and fusion fields such as bioinformatics, chemical
  biology, biophysics, medical AI, computational chemistry, materials AI, and
  physics-informed machine learning.
- **Professional issue blocks**: every substantive comment must state the
  specific problem, why it is serious, manuscript evidence, external support,
  impact, alternative explanations, fix, and decisive readout.
- **Progressive-disclosure resources**: compact `SKILL.md` instructions plus
  focused `references/`, `templates/`, `schemas/`, `scripts/`, `examples/`, and
  `agents/` resources.
- **MCP-backed skill policy**: optional host-provided MCP tools can support
  retrieval, parsing, computation, source verification, and validation while the
  skill remains the reviewer decision-maker.
- **Optional companion-skill bridge**: K-Dense, Life Science Research,
  bioinformatics, simulation, software-engineering, writing/output, and design
  companions can support bounded evidence gathering or transformations when
  installed separately.
- **Validation suite**: installability smoke test, trigger keyword checker,
  Markdown report validator, structured JSON linter, golden fixtures, unit
  tests, synthetic benchmark set, and public-source semantic-lite benchmark.
- **Security and contribution docs**: explicit private-data boundaries,
  benchmark content rules, and release validation checklist.

Each release should preserve:

- `SKILL.md` with valid Agent Skills frontmatter
- `references/` for domain standards and reviewer protocols
- `templates/` for issue blocks, search hints, and Markdown reports
- `scripts/` and `schemas/` for deterministic validation
- `examples/` for output shape and quality calibration
- `agents/openai.yaml` for host-facing display metadata

## Table of Contents

- [What's Included](#whats-included)
- [Why Use This?](#why-use-this)
- [Getting Started](#getting-started)
- [Security Notice](#security-notice)
- [Prerequisites](#prerequisites)
- [Quick Examples](#quick-examples)
- [Use Cases](#use-cases)
- [Skill Package](#skill-package)
- [MCP and Companion Skills](#mcp-and-companion-skills)
- [Validation and Benchmarks](#validation-and-benchmarks)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Citation](#citation)
- [Evidence Basis and Acknowledgements](#evidence-basis-and-acknowledgements)
- [License](#license)

## Why Use This?

### Stronger scientific review

- **Depth by default**: the skill performs comprehensive full-paper review, not
  quick review, partial review, or generic writing feedback.
- **Decisive readouts**: every major criticism must define what result would
  actually change the conclusion.
- **Panel synthesis**: EIC, methods/statistics, domain, interdisciplinary,
  Devil's Advocate, and editorial synthesis passes reduce single-perspective
  blind spots.

### Broader domain coverage

- **Experimental sciences**: controls, perturbation logic, orthogonal
  validation, characterization, calibration, uncertainty, and reproducibility.
- **Mathematics and theory**: assumptions, proof completeness, boundary cases,
  counterexamples, dependency on prior results, and sharpness.
- **Computer science and AI**: benchmark integrity, leakage, baselines,
  ablations, statistical testing, complexity, security, and artifact
  reproducibility.
- **Clinical and translational research**: endpoints, bias, external
  validation, calibration, safety, ethics, and reporting-guideline fit.

### Engineered for maintenance

- **Installability checks** guard against missing skill resources.
- **Schema and Markdown validators** keep outputs structured enough to audit.
- **Golden fixtures and benchmarks** detect regression and behavior drift.
- **CI-ready scripts** use local deterministic checks and avoid external
  services by default.

### Portable integration

- **Agent Skills format**: `rigorous-reviewer/` is self-contained and can be
  copied into compatible agent hosts.
- **Trigger routing**: English and Chinese trigger keywords help route requests
  such as `top-journal review`, `reviewer 2`, `顶刊审稿`, and `决定性证据`.
- **MCP-aware but MCP-optional**: hosts with MCP can provide tools; hosts without
  MCP can still run the core review workflow.

## Getting Started

### Option 1: Codex conversation install

Ask Codex:

```text
Use $skill-installer to install https://github.com/Felix-owo/Rigorous-Reviewer/tree/v2.3.0/rigorous-reviewer
```

Restart Codex after installation so the skill metadata is reloaded.

### Option 2: Command-line install through Codex skill-installer

```bash
python "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --url https://github.com/Felix-owo/Rigorous-Reviewer/tree/v2.3.0/rigorous-reviewer
```

Restart the agent host after installation.

### Option 3: Manual copy

Copy the full `rigorous-reviewer/` directory into the target host's skill
directory. Keep the folder intact so relative references, scripts, schemas,
templates, examples, and `agents/openai.yaml` remain available.

Validate the copied folder:

```bash
python rigorous-reviewer/scripts/check_installable_skill.py --skill-dir rigorous-reviewer
```

### Option 4: Other Agent Skills installers

If your host supports `npx skills add`, `gh skill`, or another Agent Skills
installer, follow that host's installer documentation and point it at this
repository or the `rigorous-reviewer/` subdirectory. The validated fallback is
manual copy or the Codex `$skill-installer` flow above.

### Version pinning

Use the release tag `v2.3.0` for reproducible installs. Use the `main` branch
only when you intentionally want unreleased changes:

```text
Use $skill-installer to install https://github.com/Felix-owo/Rigorous-Reviewer/tree/main/rigorous-reviewer
```

## Security Notice

> Skills can influence an agent's behavior and may instruct it to read files,
> run scripts, query services, or call host tools. Review what you install.

This repository is designed as a local-first review skill, but scientific review
often involves unpublished manuscripts, private data, confidential attachments,
local file paths, and embargoed results.

Security rules:

- Do not commit private manuscripts, unpublished user data, local paths,
  credentials, or copyrighted full-text papers.
- Do not send confidential manuscript text, private attachments, local paths, or
  unpublished data to networked MCP services unless the user explicitly
  approves that transfer.
- Treat MCP outputs as evidence inputs, not final reviewer judgment.
- Run benchmark and validation scripts locally by default.
- Review `SECURITY.md` before installing or modifying the skill.

## Prerequisites

- **Agent host**: Codex or another runtime that supports Agent Skills.
- **Python**: 3.10, 3.11, or 3.12 for local validators and benchmark scripts.
- **Network**: not required for core validation; optional for host-provided
  literature, database, DOI, or web checks.
- **MCP**: optional. No MCP server is required or bundled.
- **Companion skills**: optional. K-Dense skills can be installed separately for
  lookup and calibration support.

Optional development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

## Quick Examples

### Full manuscript review

**Goal**: Identify whether a manuscript is publishable at a top journal.

```text
Use $rigorous-reviewer to review this manuscript at Nature/Cell/Science level.
Focus on novelty, central claim dependency, decisive evidence gaps, hidden
alternative explanations, and the minimum revision package needed for a stronger
editorial decision.
```

### AI benchmark audit

**Goal**: Detect overclaiming, leakage, weak baselines, and non-reproducible
benchmark design.

```text
Use $rigorous-reviewer to review this AI paper. Check benchmark validity,
train-test leakage, baseline strength, ablations, statistical testing, compute
budget, code/data availability, and whether the claimed clinical or scientific
impact is supported.
```

### Mathematical proof review

**Goal**: Find hidden assumptions, incomplete proof steps, and counterexample
risks.

```text
Use $rigorous-reviewer to review this theorem and proof. Identify every
dependency on prior results, boundary condition, missing lemma, possible
counterexample family, and the minimum proof repair needed before publication.
```

### Clinical model review

**Goal**: Evaluate external validity and clinical overreach.

```text
Use $rigorous-reviewer to review this medical AI manuscript. Check cohort
selection, leakage, endpoint definition, calibration, external validation,
decision-curve utility, safety, reporting guideline fit, and unsupported
clinical deployment claims.
```

### Cross-disciplinary claim review

**Goal**: Test whether evidence from one domain truly supports conclusions in
another.

```text
Use $rigorous-reviewer to review this chemical biology manuscript. Separate
compound identity and target engagement evidence from biological mechanism
claims, and define decisive readouts for each bridge claim.
```

## Use Cases

### Biology and omics

- Mechanism papers, perturbation/rescue logic, lineage tracing, single-cell
  analysis, spatial omics, CRISPR screens, trajectory inference, and
  reproducibility of sample provenance.

### Chemistry and materials

- Synthetic methods, catalysis, structural characterization, purity,
  spectroscopy, target engagement, kinetics, computational chemistry, materials
  property claims, and stability controls.

### Physics

- Experimental calibration, uncertainty, systematic error, regime validity,
  simulation convergence, dimensional consistency, and independent observables.

### Mathematics

- Theorem novelty, assumptions, proof completeness, edge cases, counterexamples,
  dependence on prior results, and sharpness examples.

### Medicine and clinical AI

- Clinical trials, observational studies, diagnostic/prognostic models,
  external validation, calibration/discrimination, safety, ethics, and reporting
  standards.

### Computer science and AI

- Algorithms, systems papers, ML benchmarks, leakage, baseline fairness,
  ablations, complexity, code artifacts, reproducibility, and security/failure
  modes.

### Fusion fields

- Bioinformatics, computational biology, chemical biology, biophysics, medical
  AI, computational chemistry, materials AI, mathematical biology, and
  physics-informed machine learning.

## Skill Package

The installable package is the `rigorous-reviewer/` directory.

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
│   ├── mcp_tool_use_policy.md
│   ├── trigger_keywords.md
│   ├── article_specific_literature_mapping.md
│   ├── cns_reviewer_requirements.md
│   ├── reviewer_output_standards.md
│   └── rubric.json
├── scripts/
│   ├── validate_review_report.py
│   ├── lint_structured_review.py
│   ├── score_benchmark.py
│   ├── score_benchmark_semantic.py
│   ├── check_installable_skill.py
│   └── apply_trigger_keywords.py
├── schemas/
│   ├── review_report.schema.json
│   ├── issue.schema.json
│   ├── evidence_ledger.schema.json
│   ├── external_companion_evidence.schema.json
│   ├── trigger_keywords.schema.json
│   └── score.schema.json
└── templates/
    ├── comment_templates.json
    ├── review_report_template.md
    ├── trigger_keywords.json
    └── search_hints.json
```

Repository-level validation assets live outside the installable skill package:

```text
.github/workflows/validate.yml
tests/
benchmarks/v1.0/
benchmarks/v1.1-public/
docs/
├── README.md
├── compatibility/
│   └── agent_matrix.md
└── routing/
    └── trigger_keyword_support.md
SECURITY.md
CONTRIBUTING.md
CHANGELOG.md
```

## MCP and Companion Skills

### MCP-backed, not Skill-as-MCP

`rigorous-reviewer` remains the primary review logic. MCP tools are optional
evidence-gathering helpers only.

Use `references/mcp_tool_use_policy.md` when the host exposes capabilities such
as:

- PDF/document parsing
- PubMed, Europe PMC, Crossref, DOI, or web search
- Zotero or citation-library access
- Python/R computation
- public scientific database lookup
- filesystem/document handling
- GitHub/code artifact inspection
- benchmark or schema validation

MCP results must be recorded with provenance and must not replace the final
Markdown review, evidence ledger, issue-block logic, or recommendation.

### Optional companion ecosystem

Rigorous Reviewer can use external skills, official plugins, MCP tools, or
host-provided capabilities when they are visible in the current host. These
companions are optional and never replace the final reviewer judgment.

Recommended companions:

- ChatGPT Life Science Research: public life-science database evidence.
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills):
  paper/database/literature lookup and critical-thinking cross-checks.
- GPTomics/bioSkills: omics and bioinformatics workflow cross-checks.
- HeshamFS/materials-simulation-skills: simulation, numerical, convergence, and
  HPC reproducibility support.
- Yuan1z0825/nature-skills: rebuttal, paper polishing, citation, figure, and
  paper-to-PPT after scientific review.
- guizang-ppt-skill / open-design / taste-skill: slide deck, visual summary, or
  design output after conclusions are fixed.
- [mattpocock/skills](https://github.com/mattpocock/skills): code artifact,
  test strategy, debugging, and engineering handoff support when relevant.

Use `references/external_scientific_skills_bridge.md` for the exact invocation,
privacy, provenance, and conflict rules. K-Dense companions can be installed
separately with:

```text
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/paper-lookup
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/database-lookup
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/literature-review
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/scientific-critical-thinking
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/scholar-evaluation
```

Do not vendor companion code into this repository. Companion skills are
installed separately and remain under their own licenses.

## Validation and Benchmarks

Run the full local validation chain before publishing a release:

```bash
python -m py_compile rigorous-reviewer/scripts/*.py
python rigorous-reviewer/scripts/check_installable_skill.py --skill-dir rigorous-reviewer
python rigorous-reviewer/scripts/apply_trigger_keywords.py --skill-md rigorous-reviewer/SKILL.md --check
python rigorous-reviewer/scripts/validate_review_report.py tests/fixtures/markdown/valid_review.md --strict
python rigorous-reviewer/scripts/validate_review_report.py rigorous-reviewer/examples/full_review_example.md
python rigorous-reviewer/scripts/lint_structured_review.py tests/fixtures/json/valid_structured_review.json --strict
python rigorous-reviewer/scripts/score_benchmark.py --benchmark-root benchmarks/v1.0
python rigorous-reviewer/scripts/score_benchmark_semantic.py --benchmark-root benchmarks/v1.1-public
python -m unittest discover -s tests
```

Benchmark tracks:

- `benchmarks/v1.0/`: synthetic benchmark definitions for core reviewer failure
  modes.
- `benchmarks/v1.1-public/`: public-source case cards with source metadata and
  short paraphrases; no private manuscripts or copyrighted full-text articles.

CI runs the same categories of checks across Python 3.10, 3.11, and 3.12.

## Contributing

Contributions should improve the skill as a rigorous, auditable scientific
reviewer rather than a generic writing assistant.

Contribution rules:

1. Preserve task boundaries: this skill reviews scientific claims; it does not
   become a protocol-rewriting, copyediting, or figure-styling skill.
2. Follow the Agent Skills specification for `SKILL.md` metadata, package
   structure, and progressive disclosure.
3. Keep private manuscripts, unpublished user data, local paths, credentials,
   and copyrighted full-text papers out of tests and benchmarks.
4. Add or update validators, fixtures, benchmark expectations, and documentation
   when behavior changes.
5. Run the validation chain before opening a pull request.

See `CONTRIBUTING.md` for the full checklist.

## Troubleshooting

### Skill does not trigger

- Confirm the installed folder is named `rigorous-reviewer`.
- Confirm `rigorous-reviewer/SKILL.md` exists and has valid frontmatter.
- Restart the agent host after installation.
- Mention the skill explicitly: `Use $rigorous-reviewer ...`.
- Check `references/trigger_keywords.md` and
  `templates/trigger_keywords.json` for trigger phrases.

### Installable package check fails

- Run `python rigorous-reviewer/scripts/check_installable_skill.py --skill-dir rigorous-reviewer`.
- Confirm all required `references/`, `templates/`, `schemas/`, `scripts/`,
  `examples/`, and `agents/` files are present.
- Do not install only `SKILL.md`; copy the full folder.

### Output is too shallow

- Ask for a full `rigorous-reviewer` report and provide title, abstract, central
  claims, figures/tables, methods, data/code availability, target journal, and
  supplements when available.
- The expected issue-block logic is documented in
  `references/reviewer_rigor_contract.md`,
  `references/reviewer_output_standards.md`, and
  `examples/full_review_example.md`.

### MCP tools are unavailable

MCP is optional. The skill should continue with its built-in reviewer protocol,
search hints, calibration rules, examples, schemas, and validators. If MCP is
needed for a specific private file or external lookup, configure it in the host
and follow `references/mcp_tool_use_policy.md`.

### Companion skills are unavailable

K-Dense companion skills are optional. If they are not installed,
`rigorous-reviewer` falls back to built-in calibration, search hints, and
red-line audit rules.

## FAQ

**Q: Is this only for biology?**

A: No. It covers biology, chemistry, physics, mathematics, medicine, computer
science / AI, and interdisciplinary fields.

**Q: Does it install or require MCP servers?**

A: No. It is an MCP-aware skill, not an MCP server. MCP support is host-provided
and optional.

**Q: Can it produce a Markdown review file?**

A: Yes. The default output is Markdown in chat. A local `.md` report should be
created only when the user asks for a file, document, archive, or export.

**Q: Can it output structured JSON?**

A: Yes. Use `schemas/review_report.schema.json` and
`scripts/lint_structured_review.py` when machine-readable review output is
requested.

**Q: Does it replace expert peer review?**

A: No. It is an agent skill for structured critique, evidence mapping, and
failure-mode discovery. Final scientific and editorial decisions remain human
responsibilities.

## Citation

If you use this skill in a research workflow, cite the repository and version.

### BibTeX

```bibtex
@software{rigorous_reviewer_2026,
  author = {{Felix-owo}},
  title = {Rigorous Reviewer: A Portable Agent Skill for Scientific Peer Review},
  year = {2026},
  version = {2.3.0},
  url = {https://github.com/Felix-owo/Rigorous-Reviewer}
}
```

### Plain text

```text
Rigorous Reviewer v2.3.0. A portable Agent Skill for scientific peer review.
https://github.com/Felix-owo/Rigorous-Reviewer
```

## Evidence Basis and Acknowledgements

The review standards are anchored to established peer-review and reporting
guidance, including
[Nature peer-review criteria](https://www.nature.com/nature/editorial-policies/peer-review),
[Nature Portfolio reporting standards](https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards),
[ACS research data guidance](https://researcher-resources.acs.org/publish/data_guidelines),
[ACM artifact review and badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current),
[AMS Mathematical Reviews reviewer guidance](https://mathscinet.ams.org/mresubs/guide-reviewers.html),
[CONSORT](https://pubmed.ncbi.nlm.nih.gov/20346629/),
[PRISMA](https://www.prisma-statement.org/prisma-2020),
[STROBE](https://www.strobe-statement.org/fileadmin/Strobe/uploads/checklists/STROBE_checklist_v4_combined.pdf),
[ARRIVE](https://arriveguidelines.org/arrive-guidelines),
[SPIRIT](https://www.spirit-statement.org/spirit-statement/), and
[TRIPOD](https://www.bmj.com/content/350/bmj.g7594).

The README information architecture is adapted from
[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills):
overview, contents, table of contents, rationale, installation, security,
prerequisites, examples, use cases, package inventory, contribution guidance,
troubleshooting, FAQ, citation, and license.

The package design follows the public
[Agent Skills specification](https://agentskills.io/specification), which
defines `SKILL.md` frontmatter, optional `scripts/`, `references/`, and
`assets/` directories, and progressive disclosure. The optional tool-routing
policy follows the public
[Model Context Protocol specification](https://modelcontextprotocol.io/specification/2025-06-18),
which describes MCP resources, prompts, tools, and security principles around
consent, privacy, and tool safety.

This repository also references public skill repositories for comparative
design only:

- [mattpocock/skills](https://github.com/mattpocock/skills)
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
- [tanweai/pua](https://github.com/tanweai/pua)
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

No third-party skill code is copied into this repository. External repositories
remain under their own licenses.

## License

MPL-2.0. See `LICENSE`.
