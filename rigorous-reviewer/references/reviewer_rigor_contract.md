# Reviewer Rigor Contract

This file defines the non-negotiable depth standard. It intentionally avoids
duplicating domain thresholds, issue templates, report skeletons, or search-hint
schemas; use the specialized files listed below as the canonical sources.

## Canonical Sources

- `six_domain_review_standards.md`: biology, chemistry, physics, mathematics,
  medicine, computer science, and fusion-field evidence thresholds.
- `reviewer_output_standards.md`: issue-block, evidence-ledger, revision-action,
  search-hint, and recommendation standards.
- `reviewer_panel_protocol.md`: independent EIC, methods/statistics, domain,
  interdisciplinary, Devil's Advocate, and synthesizer passes.
- `calibration_protocol.md`: gold/near-gold/negative/boundary calibration and
  FNR/FPR/balanced-accuracy guardrails.
- `failure_mode_playbook.md`: final red-line audit and rewrite triggers.
- `templates/comment_templates.json`: machine-readable issue and revision fields.
- `templates/review_report_template.md`: canonical Markdown report scaffold.
- `templates/search_hints.json`: machine-readable search-hint structure.

## Purpose

The reviewer must produce a real referee report, not a checklist. A strong
review reconstructs the authors' strongest claim, identifies the evidence chain
needed for that claim to survive, tests the most dangerous loopholes, and gives
authors a precise revision path.

## Mandatory Claim Reconstruction

Before writing issues, reconstruct:

1. **Take-home message:** the one sentence the authors want the field to believe.
2. **Claim dependency:** which figures, proofs, assays, compounds, datasets,
   cohorts, benchmarks, simulations, or algorithms must be true for that message.
3. **Strongest claim:** the conclusion that would matter most if true.
4. **Most fragile claim:** the conclusion most vulnerable to false positives,
   hidden assumptions, leakage, confounding, weak characterization, poor
   calibration, missing validation, or cross-domain mismatch.
5. **Decisive evidence threshold:** what a specialist would require before
   accepting the strongest claim.

If the manuscript material is insufficient to reconstruct this chain, state that
explicitly and limit the review to the provided evidence.

## Mandatory Field Evidence Dossier

Before judging claims, build an article-specific dossier. It must not be generic.

- **Classic anchors:** landmark papers, canonical theories, standard assays,
  proof sources, clinical trials, benchmarks, structures, or reporting standards.
- **Canonical methods:** accepted controls, baselines, proof assumptions,
  characterization, measurement standards, clinical endpoints, or benchmark
  protocols.
- **Current frontier:** recent accepted papers and relevant preprints, clearly
  labeled as provisional when not peer-reviewed.
- **Contrary evidence:** papers, failed replications, counterexamples,
  alternative mechanisms, negative controls, or benchmark limitations that would
  narrow the claim.
- **False-positive model:** the most plausible way the authors could obtain the
  result without the claim being true.
- **Decisive test:** the smallest experiment, proof repair, validation cohort,
  benchmark redesign, characterization package, or analysis that would settle the
  issue.

## Original-Depth Regression Checklist

Use this checklist to preserve the seriousness of the original biological
reviewer while extending it across all six domains. A review is not complete
until it has done all of the following:

1. Load the rubric, issue template, search-hint template, article-specific
   literature mapping, elite-journal requirements, domain standards, and output
   standards before drafting final comments.
2. Build a paper-specific dossier of canonical papers, landmark experiments or
   theorems, gold-standard methods, current accepted work, relevant preprints,
   contrary evidence, and decisive validation standards.
3. Assign 0-10 scores with one-sentence rationales for every rubric category.
4. Rank claims by dependency and start with the claim whose failure would
   collapse the paper's take-home message.
5. For each central claim, map discovery evidence, validation evidence, controls,
   alternative explanations, decisive tests, and claim-narrowing language.
6. Label issues as Critical, Major, or Minor using claim dependency rather than
   rhetorical intensity.
7. Write every Critical/Major issue using the professional issue block defined in
   `reviewer_output_standards.md` and `templates/comment_templates.json`.
8. Audit every issue for citation, benchmark, guideline, theorem, standard,
   dataset, code, or manuscript-internal support before presenting it as a
   finding.
9. Remove, search again, or downgrade any unsupported criticism to a question.
10. Generate search hints only for real evidence gaps, using
    `templates/search_hints.json`.
11. Convert findings into an editorial action plan grouped as essential,
    important but not decisive, and wording/reporting only.
12. Define the minimum acceptable readout for each essential revision and the
    consequence if authors cannot produce it.
13. Make the recommendation from severity pattern, claim dependency, weighted
    score, novelty threshold, loophole burden, and feasibility of decisive
    revision.
14. State the minimum bar for a stronger recommendation and the exact claim that
    must be narrowed if that bar is not met.
15. Run `failure_mode_playbook.md`; rewrite any section that fails a red line.

## Non-Negotiable Output Constraints

- Every Critical/Major issue must identify manuscript-internal evidence and
  external support or an explicit search target.
- Every issue must name a decisive readout: what would support the authors'
  claim and what would weaken, refute, or force narrowing.
- Generic comments such as "more controls are needed" are invalid unless the
  exact control, interpretation change, and decisive readout are named.
- The final report must include an evidence ledger mapping sources to issues,
  revision actions, calibration anchors, or recommendation.
