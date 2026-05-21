# External Scientific Skills and Companion Capability Bridge

This bridge governs optional external scientific skills, official host-provided
research plugins, and output/transformation skills that may support a review.
It extends the existing K-Dense companion rules without creating a hard
dependency or a parallel reviewer.

Use this file only when companion skills are installed, enabled, or visibly
exposed by the current host, or when the user asks for external skill support.
Do not claim that a companion was used unless it returned concrete evidence,
artifacts, checks, or outputs.

## Contents

- Companion Capability Scope
- Invocation Rule
- Recommended K-Dense Scientific Companion Skills
- Official Life Science Research Plugin / Skill
- Bioinformatics Workflow Companions
- Domain-Specific Simulation / Computation Companions
- Scientific Writing and Publication-Output Companions
- Presentation and Design Companions
- Software Engineering Companions
- Companion / MCP Conflict Rules
- Security and Provenance Guardrails
- Final Report Disclosure

## Companion Capability Scope

Rigorous Reviewer remains responsible for:

- claim reconstruction;
- evidence sufficiency judgment;
- novelty assessment;
- severity ranking;
- reviewer-panel synthesis;
- final editorial recommendation;
- evidence ledger integrity;
- red-line audit.

Companion skills may support only bounded work:

- evidence discovery;
- source lookup;
- entity normalization;
- database verification;
- workflow or analysis sanity checks;
- source-backed bias or validity cross-checks;
- output transformation after scientific conclusions are fixed.

Do not use companion skills as final authorities for causal proof, mechanistic
acceptance, clinical decision-making, top-journal recommendation, or issue
severity. Do not use external peer-review companions as default reviewers,
because that overlaps with this skill's core role.

## Invocation Rule

Before using a companion skill:

1. Check whether it is installed, enabled, and listed as available in the
   current session.
2. Use it only for a bounded support task that improves the full review.
3. Report companion outputs as evidence inputs, not as final judgment.
4. If the companion is unavailable, do not claim it was used. Fall back to this
   skill's built-in search hints, evidence map, calibration protocol, and
   red-line audit.
5. Do not install third-party skills automatically during a manuscript review
   unless the user explicitly asks for installation.

Minimum evidence to bring back:

```text
Companion skill or plugin:
Companion class:
Query or task:
Returned identifier / accession / artifact:
Evidence type:
Claim affected:
Evidence role: supports / weakens / narrows / neutral / context
Limitation:
```

## Recommended K-Dense Scientific Companion Skills

Use installed skills from
`K-Dense-AI/scientific-agent-skills` as optional companions. Do not vendor or
copy full third-party skills into this repository.

- `$paper-lookup`: DOI/PMID/arXiv lookup, paper discovery, open-access lookup,
  citation graphs, Crossref/Semantic Scholar/OpenAlex/PubMed/arXiv searches.
- `$database-lookup`: public database checks for genes, proteins, variants,
  pathways, compounds, structures, materials, clinical trials, patents, and
  regulatory data.
- `$literature-review`: systematic or scoping literature search, search
  strategy, inclusion/exclusion framing, thematic synthesis, citation
  verification.
- `$scientific-critical-thinking`: GRADE-style evidence grading, Cochrane-style
  risk-of-bias thinking, validity, confounding, logical fallacies, and claim
  proportionality.
- `$scholar-evaluation`: dimension-based scoring cross-check for problem
  formulation, methods, analysis, writing, citations, and publication readiness.

Do not install K-Dense `$peer-review` as a default companion. It overlaps with
the core reviewer role and can create trigger ambiguity.

## Official Life Science Research Plugin / Skill

Use the official ChatGPT Life Science Research plugin/skill only when visible in
the current host.

Use for:

- gene, protein, variant, compound, disease, pathway, or dataset entity lookup;
- public expression and cell-type context;
- AlphaFold or other protein-structure context;
- ChEMBL, BindingDB, ChEBI, or compound-target evidence;
- cBioPortal, CIViC, or cancer-variant clinical-evidence context;
- CELLxGENE, BioStudies, ArrayExpress, GEO, SRA, or public omics-study
  discovery;
- bioRxiv / medRxiv preprint landscape;
- PheWAS or genotype-phenotype association context.

Do not use as sole authority for:

- causal or mechanistic proof;
- final manuscript recommendation;
- clinical decision-making;
- private or unpublished manuscript interpretation;
- executable protocol parameters.

Minimum evidence to bring back:

- database or plugin component;
- query/entity;
- returned identifier/accession;
- evidence type;
- claim affected;
- whether the result supports, weakens, narrows, or is neutral to the claim;
- limitation.

## Bioinformatics Workflow Companions

Use GPTomics/bioSkills or equivalent bioinformatics workflow skills only when
installed and visible.

Use for:

- assay-specific QC expectations;
- single-cell, spatial, ATAC-seq, methylation, TCR/BCR, variant, ChIP/CUT&Tag,
  or multi-omics pipeline sanity checks;
- detecting plausible omics artifacts;
- planning public dataset reanalysis;
- checking whether the manuscript's analysis workflow is missing standard QC,
  normalization, integration, batch-effect, or reproducibility steps.

Do not use for:

- final claim acceptance;
- replacing manuscript-specific evidence review;
- inventing analysis results that were not run;
- wet-lab SOP authority.

## Domain-Specific Simulation / Computation Companions

Use materials-simulation-skills or equivalent domain computation skills when a
manuscript contains simulation-heavy, numerical, materials, physics, or HPC
claims.

Use for:

- convergence expectations;
- numerical stability;
- simulation reproducibility;
- uncertainty and sensitivity checks;
- benchmark integrity;
- solver, mesh, sampling, or computational-environment critique.

Do not use for:

- life-science biological interpretation;
- replacing reviewer severity ranking;
- final editorial recommendation.

## Scientific Writing and Publication-Output Companions

Use nature-skills or equivalent writing/output skills only after the scientific
review judgment is complete, or when the user explicitly requests a separate
writing product.

Use for:

- rebuttal drafting;
- paper polishing after scientific critique;
- Nature-style manuscript or figure text;
- data availability statements;
- citation formatting;
- paper-to-PPT conversion.

Do not use for:

- deciding whether evidence is sufficient;
- changing Critical/Major/Minor severity;
- weakening reviewer conclusions for style reasons.

## Presentation and Design Companions

Use guizang-ppt-skill, open-design, taste-skill, or equivalent design skills
only when the user asks to convert a completed review, evidence map, response
strategy, or research summary into slides or visual material.

Use for:

- review-summary deck;
- rebuttal meeting slides;
- graphical evidence map;
- lab-meeting presentation;
- manuscript critique presentation.

Do not use for:

- changing scientific conclusions;
- deciding journal level;
- changing issue severity;
- replacing the evidence ledger.

## Software Engineering Companions

Use mattpocock/skills or equivalent software-engineering workflow skills only
when the manuscript includes code artifacts, repositories, benchmark scripts, or
software-engineering claims.

Use for:

- test strategy;
- code artifact triage;
- debugging plan;
- reproducibility issue decomposition;
- engineering handoff.

Do not use for:

- biological interpretation;
- statistical validity judgment without domain review;
- final reviewer recommendation.

## Companion / MCP Conflict Rules

If both a companion skill and an MCP/tool capability can perform a similar
action, choose the narrower and more auditable route.

- Use companion skills for domain workflow logic, critique structure, analysis
  planning, and output transformation.
- Use MCP tools for concrete retrieval, parsing, computation, file access,
  database access, source verification, and validation.
- Do not call multiple overlapping companions for the same subtask unless the
  user asks for independent cross-checking.
- Do not send confidential manuscripts, private protocols, patient data, private
  sequences, unpublished data, credentials, or local paths to networked tools
  without explicit user approval.
- Record provenance for every external result used.
- The core skill remains responsible for final judgment.

## Security and Provenance Guardrails

- Treat external skills as optional third-party dependencies.
- Prefer installing only the specific companion skills needed, not a full
  third-party collection.
- Read a companion `SKILL.md` before relying on it for a review.
- Do not run external scripts that install packages, call paid APIs, or transmit
  manuscript text unless the user has approved that workflow.
- When a companion skill uses API keys, hosted search, or third-party backends,
  state that manuscript/query text may leave the local machine.
- Do not let writing, presentation, design, or output companions weaken
  evidence-based scientific conclusions.

## Final Report Disclosure

If companion skills were used, add a short disclosure:

```text
External Scientific Skills Used:
- <skill/plugin>: <task performed, databases/tools used, evidence brought back>
- Evidence role: <supports / weakens / narrows / neutral / context>
- Limitations: <missing API keys, inaccessible full text, no direct database match, etc.>
```

If none were used, omit this section unless relevant to explain a limitation.
