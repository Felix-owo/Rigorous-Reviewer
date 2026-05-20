# External Scientific Skills Bridge

This bridge lets the reviewer use K-Dense Scientific Agent Skills as optional
companion skills without making them hard dependencies. Use this only when the
companion skills are installed and visible in the current skills list.

## Contents

- Source Basis
- Invocation Rule
- Review-Time Routing
- Security and Provenance Guardrails
- Final Report Disclosure

## Source Basis

K-Dense Scientific Agent Skills is an MIT-licensed collection of research skills
for agent hosts including Codex. Its README describes broad coverage across
scientific databases, package skills, literature review, peer review, writing,
critical thinking, and scientific communication. Do not vendor or copy full
skills into this skill; keep provenance clear and invoke installed companion
skills only when useful.

Recommended companion skills:

- `$paper-lookup`: DOI/PMID/arXiv lookup, paper discovery, open-access lookup,
  citation graphs, Crossref/Semantic Scholar/OpenAlex/PubMed/arXiv searches.
- `$database-lookup`: public database checks for genes, proteins, variants,
  pathways, compounds, structures, materials, clinical trials, patents, and
  regulatory data.
- `$literature-review`: systematic or scoping literature search, search strategy,
  inclusion/exclusion framing, thematic synthesis, citation verification.
- `$scientific-critical-thinking`: GRADE-style evidence grading, Cochrane-style
  risk-of-bias thinking, validity, confounding, logical fallacies, and claim
  proportionality.
- `$scholar-evaluation`: dimension-based scoring cross-check for problem
  formulation, methods, analysis, writing, citations, and publication readiness.

Do not install K-Dense `$peer-review` as a default companion for this skill. It
overlaps with the core reviewer role and can create trigger ambiguity. Use this
skill as the primary peer-review engine and use companion skills only for
bounded lookup, calibration, database verification, or bias-analysis tasks.

## Invocation Rule

Before using a companion skill:

1. Check whether it is installed and listed as available in the current session.
2. Use it only for a bounded support task that improves the full review.
3. Report companion-skill outputs as evidence inputs, not as final judgment.
4. If the companion skill is not installed, do not claim it was used. Fall back
   to this skill's built-in search hints, evidence map, calibration protocol, and
   red-line audit.
5. Do not install third-party skills automatically during a manuscript review
   unless the user explicitly asks for installation.

## Review-Time Routing

Use these optional routes when available:

### Literature and Gold-Anchor Search

Use `$paper-lookup` or `$literature-review` when:

- calibrating gold, near-gold, negative, and boundary anchors,
- checking whether a claim is already established,
- finding contrary evidence, failed replications, retractions, or cautionary
  benchmark papers,
- verifying DOI/PMID/arXiv metadata,
- expanding citation chains around a canonical paper.

Minimum output to bring back into the review:

```text
Companion skill used:
Query / database:
Returned anchors:
Why each anchor is comparable:
How it changes novelty, evidence threshold, or severity:
Citation identifiers:
```

### Public Database Verification

Use `$database-lookup` when the manuscript makes checkable claims about:

- genes, proteins, variants, pathways, expression datasets, structures, or cell
  atlases;
- compounds, targets, bioactivity, ADMET, drug labels, adverse events, or
  clinical trials;
- materials structures, crystallography, band gaps, phase data, or physical
  constants;
- patents, regulatory records, public datasets, or database accession IDs.

Bring back:

```text
Database queried:
Endpoint or source:
Identifier checked:
Result summary:
Manuscript claim affected:
Issue or revision action supported:
```

### Critical-Thinking Cross-Check

Use `$scientific-critical-thinking` when judging:

- causal claims from observational or correlational data,
- risk of bias, confounding, selection bias, measurement bias, attrition, or
  missing data,
- GRADE-style confidence in clinical or biomedical evidence,
- logical fallacies in discussion, significance framing, or mechanistic claims,
- whether confidence is proportional to evidence.

Use the result to sharpen the issue logic chain. Do not replace manuscript-
specific evidence or citations with generic bias labels.

### Scholar-Evaluation Cross-Check

Use `$scholar-evaluation` only as a secondary scoring sanity check. If its
dimension scores disagree with this skill's rubric, explain the discrepancy and
prefer the score tied more directly to claim dependency and decisive evidence.

## Security and Provenance Guardrails

- Treat external skills as optional third-party dependencies.
- Prefer installing only the specific companion skills needed, not the full
  collection.
- Read a companion `SKILL.md` before relying on it for a review.
- Do not run external scripts that install packages, call paid APIs, or transmit
  manuscript text unless the user has approved that workflow.
- When a companion skill uses API keys, hosted search, or third-party backends,
  state that manuscript/query text may leave the local machine.

## Final Report Disclosure

If companion skills were used, add a short disclosure:

```text
External Scientific Skills Used:
- <skill>: <task performed, databases/tools used, evidence brought back>
- Limitations: <missing API keys, inaccessible full text, no direct database match, etc.>
```

If none were used, do not add this section unless relevant to explain a limitation.
