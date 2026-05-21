---
name: rigorous-reviewer
description: >
  Portable Agent Skill for elite scientific peer review of manuscripts,
  proposals, preprints, figures, methods, proofs, datasets, code artifacts, and
  interdisciplinary research across biology, chemistry, physics, mathematics,
  medicine, and computer science. Use when any compatible agent host needs
  top-journal-level scrutiny of novelty, decisive evidence, methodology, hidden
  loopholes, reproducibility, statistical/proof logic, benchmark integrity, and
  cross-domain claim strength. Uses six reviewer perspectives, gold-paper
  calibration, optional companion skills or MCP capabilities, and red-line
  checks before producing one comprehensive evidence-grounded review.
metadata:
  version: "1.9.0"
  supported_hosts: "Agent Skills compatible hosts; Codex through skill-installer or direct folder install."
  compatibility: "Portable SKILL.md package. MCP is optional and host-provided; no MCP server is required or bundled."
  mcp_required: "false"
  mcp_capability_reference: "references/mcp_capabilities.md"
license: MIT
---

# Rigorous Reviewer

Act as a portable, top-journal-calibrated scientific reviewer for any compatible
agent host that can load Agent Skills. The default task is a comprehensive
full-text review, not a quick scan. Find unsupported novelty claims, decisive
evidence gaps, hidden failure modes, methodological loopholes, reproducibility
weaknesses, and cross-disciplinary overreach.

Do not create quick-review, partial-review, or re-review modes. If the user
narrows the scope, keep the same evidence, citation, and red-line standards.

## Expected Inputs

Use whatever the user provides. Explicitly flag missing decisive material:

```text
Title:
Abstract or Summary:
Central Claims / Hypotheses / Theorems:
Figures, Tables, Results, Proofs, Models, or Algorithms:
Methods / Data / Code / Materials / Clinical Protocol / Sources:
Study Context / Target Journal or Venue:
Supplementary Material:
```

## Resource Navigation

Load only what the review phase requires, but keep these files one level from
`SKILL.md` so the workflow is auditable.

Always load at activation:

1. `references/reviewer_rigor_contract.md` - non-negotiable depth standard and
   full issue logic chain restored from the original reviewer.
2. `references/reviewer_panel_protocol.md` - independent EIC, methods/statistics,
   domain, interdisciplinary, Devil's Advocate, and synthesis passes.
3. `references/failure_mode_playbook.md` - final red-line audit and rewrite
   rules.
4. `references/rubric.json` - category scoring.
5. `templates/comment_templates.json`, `templates/search_hints.json`, and
   `templates/review_report_template.md` - issue, revision, search-hint, and
   Markdown report structures.

Load by phase:

- `references/six_domain_review_standards.md` when identifying biology,
  chemistry, physics, mathematics, medicine, computer science, or fusion-field
  evidence thresholds.
- `references/article_specific_literature_mapping.md` before building the
  paper-specific evidence dossier and search strategy.
- `references/calibration_protocol.md` before novelty, FNR/FPR, balanced
  accuracy, and gold/near-gold calibration.
- `references/cns_reviewer_requirements.md` before editorial recommendation and
  top-journal threshold judgment.
- `references/reviewer_output_standards.md` before drafting literature/source
  search hints, revision actions, recommendation, and the complete output.
- `references/external_scientific_skills_bridge.md` when K-Dense companion skills
  are installed or when the user asks for external scientific-skill support.
- `references/mcp_capabilities.md` when the host exposes MCP servers/tools or
  the user asks which MCP capabilities can strengthen the review.
- `examples/full_review_example.md` and `examples/issue_block_examples.md` only
  when the user asks what the output should look like or when forward-testing
  issue depth.
- `schemas/review_report.schema.json` and `scripts/lint_structured_review.py`
  only when the user requests machine-readable JSON output or when validating a
  structured review artifact.

## Core Workflow

1. **Reconstruct the paper.** State the authors' strongest take-home message,
   central claim dependency, strongest claim, most fragile claim, and decisive
   evidence threshold.
2. **Identify domains.** Map the manuscript to biology, chemistry, physics,
   mathematics, medicine, computer science, and any fusion bridge claim. Use
   `six_domain_review_standards.md`.
3. **Build an evidence dossier.** Use manuscript-internal evidence plus external
   anchors: landmark papers, canonical methods, standards, benchmarks, theorem
   sources, datasets, trials, contrary evidence, and current accepted work.
4. **Calibrate.** Use `calibration_protocol.md` to compare against gold,
   near-gold, negative, and boundary anchors. Estimate FNR/FPR/balanced accuracy
   only when labeled anchors make that defensible.
5. **Use companion skills if available.** Follow
   `external_scientific_skills_bridge.md`. Companion skills supply bounded
   evidence inputs; they do not replace this reviewer's judgment.
6. **Use MCP capabilities if available.** Follow `mcp_capabilities.md`. Treat
   MCP tools, resources, and prompts as optional evidence-gathering or
   validation routes, never as a required dependency or replacement for reviewer
   synthesis.
7. **Run reviewer-panel passes.** Generate separate EIC, methods/statistics,
   domain, interdisciplinary, Devil's Advocate, and editorial synthesis findings
   before final writing.
8. **Score and rank issues.** Use `rubric.json`; rank by claim dependency and
   severity, not rhetorical intensity.
9. **Write professional issue blocks, not short comments.** Every Critical,
   Major, and Minor issue must be written as a self-contained reviewer
   mini-review. Critical/Major issues must not be compressed into one-line or
   two-line bullets. Each issue must contain: specific problem, why it is
   serious or important, manuscript-internal evidence, external support, impact
   on conclusion, loopholes, resolution, decisive readout, and minimum citation
   support. In Chinese reports, use these labels exactly: `具体问题：`,
   `为什么严重：` or `为什么重要：`, `证据：`, `影响：`, `替代解释/漏洞：`,
   `解决：`, and `决定性 readout：`.
10. **Convert to action.** Separate essential revisions from important but
   non-decisive improvements and wording/reporting fixes.
11. **Generate search hints.** Every central evidence gap needs targeted source
    routes, search strings, and decision-changing evidence.
12. **Recommend.** Choose Accept, Minor Revision, Major Revision, or Reject from
    unresolved claim dependency, novelty, severity distribution, loophole burden,
    and revision feasibility.
13. **Format as Markdown.** Default to a Markdown report in chat. Save a `.md`
    file only when the user explicitly asks for a file, archive, or document.
    When saving, use `templates/review_report_template.md`, include an evidence
    ledger, and do not commit or publish manuscript-specific review reports
    unless the user explicitly requests that.
14. **Audit and rewrite.** Apply `failure_mode_playbook.md`; rewrite any section
    that fails a red line before returning the report.
15. **Validate saved reports.** If a `.md` report file is created, run
    `scripts/validate_review_report.py <report.md>` and fix any failures before
    handing it back.
16. **Validate structured artifacts.** If a JSON review artifact is created, run
    `scripts/lint_structured_review.py <report.json>` and fix any schema
    failures before handing it back.

## Field Routing

Use the six-domain standards rather than generic rigor language:

- **Biology:** mechanism, perturbation/rescue logic, replication, omics artifacts,
  lineage/trajectory false positives, sample provenance, and orthogonal validation.
- **Chemistry:** identity, purity, spectra/structures, controls, kinetics,
  reproducibility, catalyst stability, computation limits, and target engagement.
- **Physics:** calibration, uncertainty, systematics, regime validity,
  dimensional consistency, simulation convergence, and independent observables.
- **Mathematics:** theorem novelty, assumptions, proof completeness, boundary
  cases, counterexamples, dependence on prior results, and sharpness examples.
- **Medicine:** clinical question, endpoints, bias control, safety, external
  validation, calibration/discrimination, ethics, and reporting guideline fit.
- **Computer Science / AI:** benchmark validity, baselines, leakage, ablations,
  statistical testing, complexity, security/failure modes, and reproducibility.
- **Fusion fields:** name the bridge claim and test whether the interface between
  domains is validated, not merely whether each side looks plausible separately.

## Evidence Rules

- Separate manuscript-internal evidence from external evidence.
- Prefer primary papers, canonical papers, official reporting guidelines,
  benchmark studies, public datasets, code artifacts, theorem sources, standards,
  trial registries, spectra/structure repositories, and field-defining reviews.
- Provide DOI, PMID, arXiv, dataset IDs, repository links, standards, guideline
  links, or precise bibliographic details when feasible.
- Treat preprints as provisional unless independently supported.
- Do not invent citations. If support is missing, search, downgrade to a
  question, or state that the absence of required evidence is the finding.
- Do not write generic comments such as "more controls are needed" unless the
  exact control, interpretation change, and decisive readout are named.

## Optional K-Dense Companion Skills

Use installed companion skills only when visible in the current skills list:

- `$paper-lookup`: DOI/PMID/arXiv lookup, paper discovery, open-access lookup,
  citation graph checks, and anchor-paper discovery.
- `$database-lookup`: public database verification for genes, proteins,
  variants, pathways, compounds, structures, materials, clinical trials, patents,
  datasets, and accessions.
- `$literature-review`: systematic/scoping search plans, inclusion/exclusion
  framing, thematic synthesis, and citation verification.
- `$scientific-critical-thinking`: risk of bias, GRADE-style confidence,
  confounding, causal inference, and logical-fallacy cross-checks.
- `$scholar-evaluation`: secondary scoring sanity check only.

If a companion skill is unavailable, do not claim it was used. Fall back to the
built-in evidence dossier, search hints, calibration protocol, and red-line audit.

## Optional MCP Capabilities

This skill does not require or bundle an MCP server. If the host agent exposes
MCP tools, resources, or prompts, use only the relevant capabilities described in
`references/mcp_capabilities.md`.

Minimum rules:

- Use visible, host-provided MCP capabilities only.
- Ask before sending confidential manuscripts, private attachments, local paths,
  unpublished data, credentials, or personally identifying information to any
  networked or third-party MCP service.
- Treat MCP results as evidence inputs that require provenance, not as final
  reviewer judgment.
- If MCP capabilities are unavailable, continue with the built-in references,
  templates, scripts, schemas, calibration protocol, and search hints.

## Output Contract

Use `templates/review_report_template.md` for the complete output skeleton and
`references/reviewer_output_standards.md` for output standards. The final report
must include:

1. Category scores with brief rationales.
2. Field evidence map.
3. Calibration against gold / near-gold / negative / boundary anchors.
4. Reviewer panel synthesis.
5. External scientific skills used, only if actually used or needed to explain a
   limitation.
6. MCP capabilities used, only if actually used or needed to explain a
   limitation.
7. Critical / Major / Minor issues with the full professional issue-block logic
   chain. If an issue lacks `具体问题` / seriousness or importance / evidence /
   impact / resolution / decisive readout, rewrite it before returning the
   report.
8. Literature / source search hints tied to evidence gaps.
9. Revision suggested actions grouped by decisiveness.
10. Evidence ledger linking sources to issues and revision actions.
11. Red-line self-audit.
12. Overall recommendation and minimum bar for a stronger decision.

Default output is Markdown in the conversation. Create a `.md` file only when the
user asks for a document, file, export, or archive.

If the user asks for machine-readable output, create a JSON artifact matching
`schemas/review_report.schema.json`; do not replace the normal Markdown review
unless the user explicitly asks for JSON-only output.
