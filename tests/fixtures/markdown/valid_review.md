# Reviewer Report: Synthetic Causal Mechanism Manuscript

**Date:** 2026-05-21

**Target field / venue:** biology / computational biology

**Manuscript material reviewed:** synthetic abstract, figures, methods summary, and benchmark description

**Reviewer stance:** Comprehensive top-journal-level review.

## 1) Category Scores

- Top-Journal Novelty & Significance: 6/10 - The topic is relevant, but the novelty depends on whether association can be converted into mechanism.
- Domain-Specific Technical Validity: 5/10 - The model and assays are plausible, but the causal evidence layer is incomplete.
- Logic, Proof & Evidential Support: 5/10 - The manuscript supports prioritization rather than causal demonstration.
- Loophole / Alternative-Explanation Control: 4/10 - Batch, cell composition, and severity confounding remain viable.
- Literature, Frontier & Benchmark Awareness: 6/10 - The review needs better calibration against perturbation and leakage-control standards.
- Transparency, Reproducibility & Reporting: 5/10 - Code and preprocessing details are not sufficiently auditable.

## 2) Field Evidence Map

- Central claim under review: pathway X is a causal driver of phenotype Y.
- Domain and fusion map: biology plus machine learning.
- Classic anchors: perturbation/rescue mechanism papers, external-validation benchmarks, and leakage-control standards.
- Canonical methods and evidence thresholds: donor-level replication, perturbation/rescue, orthogonal validation, and leakage-free validation.
- Current frontier and provisional sources: synthetic fixture only; real reviews must replace targets with article-specific sources.
- Main loophole or false-positive risks: pseudoreplication, composition shift, batch structure, and post hoc feature interpretation.

## 3) Calibration Against Gold / Near-Gold Papers

- Anchor set: synthetic positive, cautionary, and boundary anchors.
- Closest positive anchors: mechanism papers with perturbation and rescue.
- Closest negative or cautionary anchors: benchmark leakage and pseudoreplication cautionary studies.
- Innovation calibration: potentially interesting but weaker than positive anchors.
- Method and logic calibration: weaker than anchors with independent validation.
- FNR/FPR estimate: qualitative only because this fixture has no real labeled anchor corpus.
- Confidence adjustment: Major Revision rather than Reject because claim narrowing is feasible.

## 4) Reviewer Panel Synthesis

- EIC: the paper is potentially publishable only if the mechanism claim is narrowed or decisively tested.
- Methods / Statistics Reviewer: the experimental unit and leakage checks are the central technical risks.
- Domain Reviewer: perturbation/rescue and orthogonal validation are missing.
- Interdisciplinary Reviewer: the model-to-mechanism bridge is asserted rather than directly validated.
- Devil's Advocate: disease severity or cell composition could generate the signal without pathway causality.
- Synthesizer: the central claim remains under-supported until the strongest false-positive routes are closed.

## 5) External Scientific Skills Used

- None; this fixture is synthetic and does not require external lookup.

## 6) Identified Issues

- [Critical] Causal mechanism is inferred from association.
  具体问题：The synthetic manuscript states that pathway X drives phenotype Y, but the provided evidence consists of feature ranking, pathway enrichment, and phenotype association. The exact problematic claim is the move from "pathway X predicts phenotype Y" to "pathway X causes phenotype Y" without a perturbation, rescue, temporal-ordering, or orthogonal-validation layer.
  为什么严重：This threatens the central claim because an associative model can learn disease severity, cell-state composition, batch structure, or downstream response markers without identifying a causal driver. For a top-journal mechanism claim, the decisive evidence threshold is not high prediction accuracy alone; the claim needs an intervention or equivalent causal design showing that pathway X is necessary or sufficient for phenotype Y.
  证据：
  - 稿件内部证据：The synthetic Figure 4 and Discussion use causal language, while the Methods summary reports no perturbation/rescue experiment, no donor-level replication of the causal effect, and no orthogonal assay in an independent biological system.
  - 外部证据/标准：Synthetic benchmark standard S1, DOI:10.0000/rr.synthetic.causal-standard, defines perturbation/rescue or an equivalent causal design as the decision-changing evidence for mechanism claims.
  影响：The manuscript can support candidate prioritization, but it cannot yet support a demonstrated causal mechanism. If unresolved, the abstract, title, and Discussion would overstate the evidential category of the result.
  替代解释/漏洞：Batch-condition confounding, cell-composition shifts, disease severity, stress response, marker correlation, and post hoc feature interpretation could explain the observed association without pathway X being causal.
  解决：Add a targeted perturbation of pathway X, rescue or epistasis logic, donor-level replication, and an orthogonal readout in an independent system. If this is outside scope, rewrite the central conclusion as a predictive prioritization claim rather than a mechanism claim.
  决定性 readout：The claim is supported if perturbing pathway X changes phenotype Y in the predicted direction and rescue restores the phenotype while batch/composition controls remain stable. The claim is weakened or must be narrowed if the effect disappears after donor-level modeling, if perturbation does not change phenotype Y, or if the signal is explained by composition or severity adjustment.

## 7) Literature / Source Search Hints

- Evidence gap / claim tested: whether pathway X has causal evidence for phenotype Y.
- Preferred sources: primary perturbation/rescue papers, benchmark leakage papers, and donor-level replication standards.
- Search strings: "pathway X perturbation rescue phenotype Y"; "single cell pseudoreplication donor level model"; "feature importance mechanism validation".
- Decision-changing evidence: independent perturbation/rescue evidence would strengthen the claim; null perturbation or donor-level loss of signal would narrow it.
- Citation target: Critical issue on causal overclaim.

## 8) Revision Suggested Actions

### Essential for supporting the main claim

- Target: Figure 4, Methods, Discussion.
- Required revision: add perturbation/rescue or explicitly narrow the claim.
- Minimum acceptable readout: donor-level replicated change in phenotype Y after pathway X perturbation and restoration after rescue.
- Rationale with evidence: the central claim depends on mechanism rather than association.
- Consequence if unresolved: the paper must remove causal wording or remain a Major Revision.

### Important but not decisive

- Target: code and preprocessing.
- Required revision: release feature-selection settings and donor-level model specification.
- Minimum acceptable readout: an expert can reproduce the direction of effect.
- Rationale with evidence: computational inference requires artifact-level audit.
- Consequence if unresolved: reproducibility remains limited.

### Wording/reporting only

- Replace "drives phenotype Y" with "prioritizes a candidate pathway associated with phenotype Y" unless decisive causal evidence is added.

## 9) Evidence Ledger

| ID | Source | Type | Supports / challenges | Decision role | Identifier / link |
| --- | --- | --- | --- | --- | --- |
| M1 | Synthetic Figure 4 and Discussion | manuscript-internal | causal overclaim issue | decisive | synthetic fixture |
| S1 | Synthetic causal-mechanism benchmark standard | benchmark | perturbation/rescue evidence threshold | decisive | DOI:10.0000/rr.synthetic.causal-standard |

## 10) Red-Line Self-Audit

- Citation support: pass with synthetic source identifier.
- Manuscript-internal evidence: pass.
- Decisive readouts: pass.
- Search-hint coverage: pass.
- Panel traceability: pass.
- Markdown/report validation: pass.

## 11) Overall Recommendation

- Major Revision
- Rationale: the manuscript is promising, but the central causal claim remains under-supported because the decisive perturbation/rescue layer is absent.
- Minimum bar for a stronger recommendation: donor-level replicated perturbation/rescue or rigorous claim narrowing.
- Required claim narrowing if the bar is not met: state association and candidate prioritization only.
- Residual risk after revision: even positive perturbation data may leave the exact causal path unresolved.
