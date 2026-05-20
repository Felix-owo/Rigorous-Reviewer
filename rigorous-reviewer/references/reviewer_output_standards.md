# Reviewer Output Standards for Final Sections

Use this reference before drafting `Literature / Source Search Hints`,
`Revision Suggested Actions`, and `Overall Recommendation`.

## Contents

- Source Principles
- Literature / Source Search Hints Standard
- Revision Suggested Actions Standard
- Overall Recommendation Standard
- Professional Issue Block Standard
- Markdown Report and Evidence Ledger Standard
- Report Template Pointer

## Source Principles

The final sections should reflect recognized peer-review and reporting norms:

- Nature asks reviewers to assess key results, validity, originality/significance,
  data and methodology, statistics and uncertainty, robustness of conclusions,
  suggested improvements, references, clarity, and context:
  https://www.nature.com/nature/editorial-policies/peer-review
- Nature Portfolio reporting standards emphasize transparency and reproducibility
  across science, including data, materials, code, protocols, reporting summaries,
  and code/algorithm peer review when central:
  https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards
- Cell guidance emphasizes the manuscript's main take-home message, close
  technical judgment, broader conceptual judgment, and avoidance of unrealistic
  or shifting expectations: https://crosstalk.cell.com/blog/how-does-cell-select-reviewers
- Science/AAAS policies emphasize availability of materials, methods, and data
  needed to verify conclusions:
  https://www.science.org/content/page/science-journals-editorial-policies
- ACS Research Data Guidelines require data to be transparent and rigorous enough
  for trained researchers to reproduce experiments and evaluate the approach:
  https://researcher-resources.acs.org/publish/data_guidelines
- ACM artifact review and badging defines standards for artifacts evaluated,
  artifacts available, and results validated:
  https://www.acm.org/publications/policies/artifact-review-and-badging-current
- AMS Mathematical Reviews guidance says mathematical errors should be described
  precisely with evidence such as counterexamples or exact references:
  https://mathscinet.ams.org/mresubs/guide-reviewers.html
- Medical reporting standards should be used where relevant, including CONSORT,
  PRISMA, STROBE, ARRIVE, SPIRIT, and TRIPOD.
- COPE ethical guidance requires fair, confidential, evidence-based, conflict-free
  peer review: https://publicationethics.org/resources/guidelines-new/cope-ethical-guidelines-peer-reviewers

These sources should shape evidence discipline and structure, not be copied
stylistically.

## Literature / Source Search Hints Standard

Do not output a generic bibliography scavenger hunt. Each hint should help a
reviewer verify one decisive weak link.

Each hint must contain:

- **Evidence gap / claim tested:** exact claim, missing control, chemical
  characterization gap, physical systematic, theorem/proof gap, clinical
  validation gap, benchmark weakness, reporting standard, or fusion-field bridge.
- **Preferred sources:** primary paper, method paper, benchmark, reporting
  guideline, dataset, code artifact, spectra/structure repository, theorem
  source, clinical trial record, official venue policy, or provisional preprint.
- **Search strings:** two to four targeted queries with field, method, dataset,
  compound/material, theorem, cohort, benchmark, or control terms.
- **Decision-changing evidence:** what would strengthen, weaken, or narrow the
  review conclusion.
- **Citation target:** the issue or revision action the search supports.

Strong examples:

> Evidence gap / claim tested: Whether the model's claimed superiority survives
> leakage-free evaluation against current baselines.
> Preferred sources: benchmark papers, baseline implementations, ACM artifact
> guidance, NeurIPS/ICLR reproducibility guidance, and independent replications.
> Search strings: `arxiv leakage benchmark <task> baseline`; `ACM artifact review
> reproducibility benchmark machine learning`; `google scholar "<dataset>" "data
> leakage"`.
> Decision-changing evidence: independent leakage-free benchmarks with matching
> gains would strengthen the claim; contrary replications or leakage reports would
> require narrowing.
> Citation target: Critical issue on benchmark validity.

> Evidence gap / claim tested: Whether a compound's biological phenotype is due
> to the claimed target rather than impurity or off-target activity.
> Preferred sources: ACS characterization guidance, spectra/structure data,
> target-engagement papers, and orthogonal assay benchmarks.
> Search strings: `ACS <compound class> characterization purity NMR HRMS`;
> `pubmed <target> chemical probe target engagement selectivity`; `google scholar
> <assay> orthogonal validation chemical biology`.
> Decision-changing evidence: complete characterization plus orthogonal target
> engagement would strengthen the claim; missing purity or selectivity would force
> claim narrowing.
> Citation target: Major issue on chemical identity and biological specificity.

> Evidence gap / claim tested: Whether a theorem excludes a boundary case that
> invalidates the claimed generality.
> Preferred sources: MathSciNet/zbMATH records, prior theorem sources,
> counterexample papers, and canonical monographs.
> Search strings: `MathSciNet <theorem/topic> <assumption>`; `google scholar
> "<theorem phrase>" counterexample`; `arxiv <topic> boundary case regularity`.
> Decision-changing evidence: a known counterexample would force theorem
> narrowing; a prior theorem with identical assumptions would reduce novelty.
> Citation target: Critical issue on proof assumptions and novelty.

## Revision Suggested Actions Standard

A responsible senior review gives authors a feasible path to a stronger
manuscript while protecting the literature from unsupported claims.

Group actions as:

1. **Essential for supporting the main claim:** required for acceptance or for
   preserving the strongest conclusion.
2. **Important but not decisive:** strengthens rigor, context, or reporting but
   does not determine whether the core claim survives.
3. **Wording/reporting only:** prevents overclaiming, improves reproducibility,
   clarifies figures/tables/proofs/benchmarks/materials, or fixes citations.

Each essential action must state:

- **Target:** exact figure, table, result, method, compound, structure, spectrum,
  cohort, model, theorem, proof step, algorithm, benchmark, or section.
- **Required revision:** exact experiment, analysis, control, characterization,
  benchmark, proof repair, validation cohort, statistical test, data/code release,
  calibration, external validation, or rewrite.
- **Minimum acceptable readout:** quantitative metric, control behavior,
  reproducibility threshold, proof standard, characterization standard, clinical
  validation threshold, robustness outcome, or explicit claim-narrowing language.
- **Rationale with evidence:** why the action is necessary and which literature,
  standard, guideline, theorem source, benchmark, or official policy sets the bar.
- **Consequence if unresolved:** what conclusion must be removed, narrowed, or
  labeled preliminary/speculative.

Do not ask for broad new projects unless the central claim requires them.

## Overall Recommendation Standard

The recommendation should read like an editorial decision summary, not a grade.

Include:

- **Decision:** Accept, Minor Revision, Major Revision, or Reject.
- **Central reason:** one or two sentences linking severity pattern to claim
  dependency, novelty, and loophole burden.
- **Minimum bar for a stronger recommendation:** smallest decisive revision package.
- **Required claim narrowing if unresolved:** exact claim to weaken, remove, or reframe.
- **Residual risk after revision:** main uncertainty that may remain.

Use this calibration:

- **Major Revision:** promising and potentially publishable, but central claims
  require additional analyses, controls, characterization, proof repair, stronger
  benchmarks, clinical external validation, reporting, or claim narrowing.
- **Reject:** central claim would require a fundamentally different study, proof,
  benchmark, validation cohort, characterization package, or experimental system;
  dominant loopholes cannot be resolved from available material; or claimed
  novelty is already established by stronger prior work.
- **Minor Revision:** evidence already supports the main claim and remaining
  changes are presentation, reporting, citation, or bounded non-decisive checks.

Good recommendation pattern:

> Major Revision. The central claim is potentially important, but the current
> evidence establishes plausibility rather than proof because the decisive
> benchmark/control/characterization/proof step does not rule out the strongest
> loophole. A stronger recommendation would require X, Y, and Z; if those cannot
> be provided, the manuscript should state only the narrower claim.

Bad recommendation pattern:

> Major Revision because more controls are needed and the paper would be stronger
> with more work.

## Professional Issue Block Standard

Issue blocks are the core of the review. They should read like detailed
professional reviewer comments, not checklist fragments. Each Critical, Major,
and Minor issue must be self-contained enough that an editor can understand
what claim is at risk, why the problem is serious, what evidence supports the
criticism, what revision is needed, and what result would change the decision.

Use the user's language. For Chinese reports, use these labels exactly:

```text
- [Critical/Major/Minor] <short title>
  具体问题：<name the exact claim, figure, table, method, proof step, benchmark,
  cohort, dataset, code artifact, or interpretation that is problematic.>
  为什么严重：<for Critical/Major issues, explain why this threatens the central
  claim, novelty, causal logic, proof logic, benchmark validity, clinical
  validity, reproducibility, or cross-domain bridge. For Minor issues, use
  为什么重要： instead when the point is mainly clarity/reporting.>
  证据：
  - 稿件内部证据：<figure/panel/table/method/proof/data/code/source or stated
    omission. If evidence is absent, state that the omission is the internal
    evidence.>
  - 外部证据/标准：<primary paper, guideline, benchmark, theorem source, dataset,
    official policy, protocol, DOI/PMID/arXiv/link, or clearly labeled search
    target.>
  影响：<state which conclusion becomes unsupported, overclaimed, ambiguous,
  non-novel, non-reproducible, or vulnerable to false positive interpretation.>
  替代解释/漏洞：<name plausible confounders, artifacts, hidden assumptions,
  leakage routes, systematics, impurity/off-target explanations, boundary cases,
  cohort shift, or cross-domain mismatches.>
  解决：<specific experiment, analysis, control, benchmark, proof repair,
  characterization, external validation, data/code release, reporting addition,
  or claim-narrowing rewrite.>
  决定性 readout：<define the result that would support the authors' claim and
  the result that would weaken/refute it or force claim narrowing.>
```

Density requirements:

- Critical issues should normally be 150-300 words each unless the manuscript is
  very short. Major issues should normally be 100-220 words each. Minor issues
  can be shorter but must still name the exact target and fix.
- `证据` must separate manuscript-internal evidence from external evidence or a
  targeted search route. Do not hide an uncited field-standard claim inside
  `为什么严重`.
- `解决` must specify the minimum sufficient revision, not a broad wish list.
- `决定性 readout` must contain both a support condition and a weakening,
  refuting, or claim-narrowing condition.
- If two issue blocks share the same evidence, impact, and readout, merge them
  rather than repeating the same criticism.

## Markdown Report and Evidence Ledger Standard

Default final reviews should be valid Markdown, whether returned in chat or
saved as a `.md` file. Do not save a manuscript-specific `.md` file unless the
user asks for a file, document, archive, or export.

When a file is requested:

- Use `templates/review_report_template.md` as the report scaffold.
- Use a conservative filename such as
  `review_<short-title-or-doi>_<YYYY-MM-DD>.md`.
- Keep manuscript-specific reports local unless the user explicitly asks to push
  or publish them.
- After writing the file, run
  `scripts/validate_review_report.py <report.md>` and fix any failures.

Every full review should include an **Evidence Ledger**. The ledger makes the
review auditable by mapping sources to exact issues and decisions.

Evidence ledger columns:

- **ID:** stable source handle, for example `S1`, `S2`, `G1`, `B1`, `D1`.
- **Source:** paper, guideline, benchmark, dataset, theorem source, official
  policy, trial registry, spectra/structure repository, code repository, or
  manuscript location.
- **Type:** manuscript-internal, primary paper, guideline, benchmark, dataset,
  theorem/proof source, clinical registry, artifact/code, or standard.
- **Supports / challenges:** exact claim, issue, revision action, calibration
  anchor, or recommendation.
- **Decision role:** decisive, supporting, cautionary, context only, or search
  target.
- **Identifier / link:** DOI, PMID, arXiv, accession, URL, registry ID,
  repository URL, section/table/figure, or exact bibliographic detail.

Ledger quality rules:

- Every Critical/Major issue must map to at least one manuscript-internal ledger
  item and at least one external ledger item or explicit search target.
- Search targets are allowed only when the source is genuinely missing; they must
  include the query path that would change the decision.
- Do not pad the ledger with unrelated citations. Each source must support a
  stated claim, issue, action, or calibration judgment.

## Report Template Pointer

The canonical full-report skeleton lives in
`templates/review_report_template.md`. Do not duplicate that skeleton here. Use
this file for standards and the template file for report layout.
