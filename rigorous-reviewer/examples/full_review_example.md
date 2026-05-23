# Full Review Example

This is a compact example of the expected section order. Real reviews should be
longer, cite the actual manuscript locations and article-specific sources, and
write every issue as a professional issue block with an evidence ledger.

```markdown
# Reviewer Report: Example Multi-Omics Mechanism Manuscript

**Date:** 2026-05-19

**Target field / venue:** biology / computational biology

**Manuscript material reviewed:** main text, figures, methods, and stated code availability

**Reviewer stance:** Comprehensive top-journal-level review.

## 1) Category Scores
- Top-Journal Novelty & Significance: 6/10 - The claimed bridge between a new
  predictive model and causal biological mechanism is interesting, but the
  manuscript has not shown that the model changes mechanistic understanding
  beyond known pathway-level associations.
- Domain-Specific Technical Validity: 5/10 - The study uses a plausible
  multi-omics design, but replication, batch control, and perturbation logic are
  insufficient for the causal claim.
- Logic, Proof & Evidential Support: 5/10 - The evidence supports association
  and prioritization, not mechanism.
- Loophole / Alternative-Explanation Control: 4/10 - Disease severity, cell-type
  composition, and dataset leakage remain viable false-positive routes.
- Literature, Frontier & Benchmark Awareness: 6/10 - The paper cites core
  benchmarks but misses cautionary studies on external validation.
- Transparency, Reproducibility & Reporting: 5/10 - Code is promised but not
  linked; preprocessing and hyperparameter search are underspecified.

## 2) Pre-Review Contract Snapshot
- Contract status: locked.
- Material basis: main text, figures, methods, and stated code availability.
- Central claim dependency: C1, model-selected features identify a causal
  disease mechanism.
- Decisive evidence threshold: leakage-free external validation plus
  perturbation/rescue or an equivalent orthogonal mechanism test.
- Failure condition: predictive performance without causal validation keeps the
  mechanistic claim at Major Revision or forces claim narrowing.
- Prohibited post-hoc shift: do not replace mechanism evidence with polished
  interpretation of feature importance.

## 3) Claim Maturity Gate
| Claim | Current maturity | Evidence basis | Blocking loophole | Upgrade readout | Required narrowing |
| --- | ---: | --- | --- | --- | --- |
| C1: model-selected features identify a causal disease mechanism | 2 | Predictive association and feature ranking are present, but orthogonal mechanism evidence is missing. | Cohort leakage, disease severity, cell composition, and batch structure can explain the signal. | Independent cohort validation plus perturbation/rescue changes the phenotype in the predicted direction. | Narrow to candidate prioritization if mechanism validation is absent. |

## 4) Field Evidence Map
- Central claim under review: model-selected features identify a causal disease
  mechanism.
- Domain and fusion map: computational biology, machine learning, disease
  mechanism.
- Classic anchors: external-validation studies, perturbation/rescue mechanism
  studies, leakage-control benchmarks.
- Canonical methods and evidence thresholds: leakage-free validation,
  perturbation/rescue, orthogonal readouts, reproducible preprocessing.
- Current frontier and provisional sources: article-specific accepted studies
  plus clearly labeled preprints.
- Main loophole or false-positive risks: cohort leakage, cell composition,
  disease severity, batch effects, and post hoc pathway interpretation.

## 5) Assumption Ledger
| Assumption | Source / absence of source | Possible bias direction | Evidence that would update conclusion |
| --- | --- | --- | --- |
| The example has no source data or code audit. | Stated code availability only. | May understate or overstate reproducibility risk. | Public code, data, and rerun logs that reproduce the main results. |
| No exact field-specific source is bundled in this compact example. | Search targets are used as placeholders for real article review. | May make external standard severity less precise. | Article-specific accepted papers, guidelines, or benchmark sources. |

## 6) Calibration Against Gold / Near-Gold Papers
- Anchor set: 8 anchors, including 4 accepted benchmark/method papers, 2
  cautionary leakage studies, and 2 external-validation papers.
- Innovation calibration: similar to accepted applied-method papers, weaker than
  positive anchors that include prospective or perturbational validation.
- Method calibration: weaker than anchors requiring external cohort validation.
- FNR/FPR estimate: qualitative only; there are not enough labeled positive and
  negative anchors to compute numeric FNR/FPR.
- Confidence adjustment: maintain Major Revision rather than Reject because the
  claim can be narrowed to predictive prioritization if mechanism is not proven.

## 7) Reviewer Panel Synthesis
- EIC: topic is potentially broad, but central mechanism claim is not yet
  top-journal level.
- Methods / Statistics Reviewer: benchmark split and external validation are the
  highest-risk technical gaps.
- Domain Reviewer: perturbation or orthogonal biological validation is needed for
  mechanism.
- Interdisciplinary Reviewer: the computational-to-biological bridge is asserted
  rather than directly validated.
- Devil's Advocate: cell composition or cohort leakage could explain the signal
  without a new mechanism.
- Synthesizer: central claim should be narrowed unless external validation and
  perturbational evidence support the bridge.

## 8) External Scientific Skills Used
- Not applicable in this compact example.

## 9) Identified Issues
- [Critical] Mechanistic claim is not established by predictive performance.
  具体问题：The abstract and Figure 4 interpret model-selected features as a
  causal disease mechanism, but the evidence shown is model association and
  feature ranking rather than perturbational mechanism. The problematic target is
  not the predictive model itself; it is the manuscript's transfer from
  "predicts phenotype" to "explains disease mechanism."
  为什么严重：This is central because a high-performing classifier can learn
  cohort structure, disease severity, cell-state composition, or batch-specific
  signals without identifying a causal biological mechanism. If the manuscript's
  main advance is mechanistic, predictive performance alone does not meet the
  evidentiary bar for a top-journal biological claim.
  证据：
  - 稿件内部证据：Figure 4 and the Discussion state a mechanistic interpretation,
    but the example manuscript provides no perturbation, rescue, orthogonal
    assay, temporal ordering, or independent biological system that tests the
    proposed mechanism.
  - 外部证据/标准：Use external-validation and leakage-control standards for
    predictive modeling plus a domain-specific perturbation/rescue or orthogonal
    validation source for biological mechanism. If exact sources are not yet
    available, add a targeted search hint rather than leaving the field-standard
    claim uncited.
  影响：The data can support candidate mechanism prioritization, but not a
  demonstrated disease mechanism. Without narrowing, the abstract and Discussion
  overstate what the evidence establishes.
  替代解释/漏洞：Cohort leakage, disease severity, cell-type composition, batch
  effects, correlated pathway activation, and post hoc pathway interpretation
  could all generate the observed model signal without a new causal mechanism.
  解决：Add leakage-free external cohort validation and at least one orthogonal
  mechanism test such as perturbation/rescue, independent assay validation, or a
  pre-specified negative-control pathway. If these are infeasible, rewrite the
  claim as predictive prioritization rather than mechanism discovery.
  决定性 readout：The claim is strengthened if the same feature/module predicts
  the phenotype in an independent cohort and perturbing the proposed mechanism
  changes the phenotype in the predicted direction. The claim is weakened or
  must be narrowed if performance drops under leakage-free validation, if the
  association disappears after composition/severity adjustment, or if
  perturbation does not affect the phenotype.

## 10) Literature / Source Search Hints
- Evidence gap / claim tested: whether model feature importance can support the
  stated mechanistic conclusion.
- Preferred sources: primary method papers, external-validation benchmarks,
  biological perturbation standards.
- Search strings:
  - "feature importance mechanistic interpretation biological validation"
  - "medical AI external validation leakage biomarker model"
  - "disease model perturbation rescue mechanism validation"
- Decision-changing evidence: accepted anchors with perturbational validation
  strengthen the requested bar; accepted predictive-only papers support claim
  narrowing.
- Citation target: Critical issue on mechanism overclaim.

## 11) Revision Suggested Actions
### Essential for supporting the main claim
- Target: Figure 4, Methods, Discussion.
- Required revision: external validation plus orthogonal perturbation/rescue or
  explicit narrowing to candidate prioritization.
- Minimum acceptable readout: reproducible direction of effect in an
  independent cohort and perturbation consistent with the claimed mechanism.
- Rationale with evidence: required because the central claim transfers from
  prediction to biological mechanism.
- Consequence if unresolved: remove or narrow the mechanistic claim.

### Important but not decisive
- Target: code and preprocessing documentation.
- Required revision: release preprocessing scripts, feature-selection settings,
  and hyperparameter search ranges.
- Minimum acceptable readout: an expert can rerun the model and reproduce the
  main result direction.
- Rationale with evidence: computational claims require artifact-level audit.
- Consequence if unresolved: reproducibility remains limited.

### Wording/reporting only
- Replace mechanism-discovery wording with candidate-prioritization wording if
  no perturbation/rescue is added.

## 12) Evidence Ledger
| ID | Source | Type | Supports / challenges | Decision role | Identifier / link |
| --- | --- | --- | --- | --- | --- |
| M1 | Figure 4 and Discussion | manuscript-internal | Critical issue on mechanism overclaim | decisive | Figure 4; Discussion |
| M2 | Methods code availability statement | manuscript-internal | reproducibility action | supporting | Methods |
| S1 | External-validation and leakage-control literature | search target | Critical issue on predictive-to-mechanistic bridge | decisive search target | query in section 7 |
| S2 | Biological perturbation/rescue standard | search target | required mechanism validation | decisive search target | query in section 7 |

## 13) Red-Line Self-Audit
- Citation support: fixed with source targets; real reviews should replace
  search targets with article-specific citations.
- Manuscript-internal evidence: pass.
- Decisive readouts: pass.
- Search-hint coverage: pass.
- Panel traceability: pass.
- Markdown/report validation: pass for structure.

## 14) Overall Recommendation
- Major Revision
- Rationale: The work is promising as a predictive and hypothesis-generating
  study, but the central mechanistic claim remains unsupported until the
  computational-to-biological bridge is directly validated.
- Minimum bar for a stronger recommendation: external validation, leakage audit,
  and one decisive orthogonal mechanism test.
- Required claim narrowing if the bar is not met: frame results as candidate
  mechanism prioritization rather than demonstrated mechanism.
- Residual risk after revision: even after validation, the exact causal path may
  remain unresolved without temporal or epistatic evidence.
```
