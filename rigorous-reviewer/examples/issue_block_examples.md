# Issue Block Examples Across Six Domains

These examples demonstrate the required issue anatomy. Replace placeholders with
article-specific manuscript evidence and article-specific sources during real
reviews.

## Biology

- [Critical] Central mechanism is inferred without perturbation or rescue.
  具体问题：Figure 3 and the Discussion state that pathway X drives phenotype Y,
  but the evidence is correlative expression enrichment plus pathway annotation.
  No perturbation, rescue, temporal ordering, or orthogonal assay directly tests
  whether pathway X is necessary or sufficient for phenotype Y.
  为什么严重：This threatens the central biological mechanism claim. A pathway can
  be correlated with cell state, stress, batch, or disease severity without being
  causal. For a top-journal mechanism claim, descriptive association is not the
  same evidentiary category as perturbation or rescue.
  证据：
  - 稿件内部证据：Figure 3 shows enrichment and the Discussion makes a causal
    statement, but the Methods contain no perturbation/rescue experiment or
    independent validation assay.
  - 外部证据/标准：Use Nature Portfolio reporting standards for data/material/code
    transparency and an article-specific primary mechanism paper or field method
    benchmark as the evidence bar: https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards
  影响：The manuscript supports prioritizing pathway X as a candidate, but it
  does not yet support the stronger conclusion that pathway X drives phenotype Y.
  替代解释/漏洞：Cell composition, activation state, stress response, batch
  effect, reverse causality, or a parallel upstream regulator could produce the
  same enrichment pattern.
  解决：Add a loss-of-function or gain-of-function perturbation, rescue, and
  orthogonal readout in the relevant cell type or model system. If infeasible,
  narrow the claim to candidate pathway association.
  决定性 readout：The claim is supported if perturbing pathway X changes phenotype
  Y in the predicted direction and rescue restores it. The claim is weakened or
  must be narrowed if the phenotype persists after perturbation or disappears
  after adjusting for composition/batch/state.

## Chemistry

- [Major] Chemical identity and purity are insufficient for biological inference.
  具体问题：The manuscript attributes cellular activity to compound A, but the
  Methods report only supplier name and nominal concentration. The evidence does
  not document identity, purity, storage stability, or batch-to-batch consistency.
  为什么严重：A biological phenotype caused by impurity, degradation product, salt
  form, stereochemical mixture, or assay interference would invalidate target
  interpretation even if the cell assay is reproducible.
  证据：
  - 稿件内部证据：The compound section lacks NMR/LC-MS/HRMS/chromatography data,
    certificate of analysis, stability information, and replicate batch details.
  - 外部证据/标准：ACS research data guidance emphasizes transparent data sufficient
    for trained researchers to evaluate and reproduce the approach:
    https://researcher-resources.acs.org/publish/data_guidelines
  影响：The target-engagement and mechanism claims remain ambiguous because the
  active chemical species is not established.
  替代解释/漏洞：Impurity, degradation, aggregation, redox cycling, off-target
  activity, assay fluorescence interference, or concentration misestimation could
  explain the phenotype.
  解决：Provide identity and purity characterization, batch information, stability
  conditions, orthogonal target-engagement assay, and inactive/structural analog
  controls.
  决定性 readout：The claim is supported if independently characterized compound
  lots reproduce the phenotype and orthogonal engagement tracks activity. It is
  weakened if activity varies by batch, disappears after purification, or does
  not track target engagement.

## Physics

- [Major] Measurement uncertainty is incomplete and does not rule out systematics.
  具体问题：The manuscript reports a small effect size in Figure 2 but provides only
  standard error across repeated measurements. It does not present an uncertainty
  budget covering calibration, drift, background subtraction, alignment, detector
  response, or model-dependent corrections.
  为什么严重：When the claimed effect is comparable to plausible systematic error,
  statistical repeatability alone cannot establish the physical conclusion.
  证据：
  - 稿件内部证据：Figure 2 reports error bars, but the Methods do not separate
    statistical uncertainty from calibration and systematic uncertainty.
  - 外部证据/标准：NIST Technical Note 1297 provides official guidance on evaluating
    and expressing measurement uncertainty:
    https://www.nist.gov/pml/nist-technical-note-1297
  影响：The conclusion that the observed shift reflects a real physical effect,
  rather than measurement artifact, is not yet secure.
  替代解释/漏洞：Instrument drift, calibration offset, temperature dependence,
  finite-size effect, background model choice, or unmodeled detector nonlinearity
  could generate the apparent signal.
  解决：Add a full uncertainty budget, calibration records, null measurements,
  sensitivity to background/model choices, and an independent observable where
  feasible.
  决定性 readout：The claim is supported if the effect remains larger than the
  combined uncertainty across independent calibration and null tests. It is
  weakened if the effect overlaps the systematic uncertainty envelope or changes
  sign under reasonable correction models.

## Mathematics

- [Critical] A proof step appears to use a stronger assumption than stated.
  具体问题：The proof of Theorem 1 applies Lemma 2 as if uniform boundedness holds
  on the full domain, but the theorem statement assumes only local boundedness.
  The manuscript does not justify the extension or exclude boundary cases.
  为什么严重：A hidden strengthening of assumptions can invalidate the claimed
  theorem generality and reduce novelty if the correct result is a known special
  case.
  证据：
  - 稿件内部证据：The transition from Eq. 7 to Eq. 8 invokes the bound globally, but
    the assumptions before Theorem 1 do not state a global bound.
  - 外部证据/标准：AMS Mathematical Reviews guidance asks reviewers to identify
    mathematical errors precisely with evidence such as exact references or
    counterexamples: https://mathscinet.ams.org/mresubs/guide-reviewers.html
  影响：The theorem may hold only under stronger assumptions, and the stated
  generality may be unsupported.
  替代解释/漏洞：A boundary counterexample, noncompact domain, discontinuity,
  failure of convergence exchange, or missing regularity condition could break
  the proof.
  解决：Either prove the missing bound from the stated assumptions, add the
  stronger assumption and narrow the theorem, or provide a counterexample search
  and boundary-case analysis showing the step is valid.
  决定性 readout：The claim is supported if the authors derive the needed bound
  from existing assumptions or give a valid replacement argument. It is weakened
  if a boundary case violates the step or the theorem must be restated as a
  known special case.

## Medicine

- [Critical] The clinical claim lacks external validation and calibration.
  具体问题：The manuscript claims clinical readiness for a diagnostic/prognostic
  model, but reports only internal cross-validation. It does not provide external
  validation, calibration assessment, decision-curve analysis, or prespecified
  handling of missingness and threshold selection.
  为什么严重：Internal performance can be optimistic under cohort-specific case
  mix, site effects, preprocessing choices, and threshold tuning. Clinical claims
  require evidence that discrimination and calibration survive outside the
  development data.
  证据：
  - 稿件内部证据：The Results show internal AUROC only; the Methods do not describe
    external cohort validation, calibration slope/intercept, or threshold
    prespecification.
  - 外部证据/标准：TRIPOD reporting standards define expectations for transparent
    prediction model reporting: https://www.bmj.com/content/350/bmj.g7594
  影响：The model may be hypothesis-generating, but the claim of clinical utility
  or readiness is unsupported.
  替代解释/漏洞：Spectrum bias, site leakage, treatment-era differences, missing
  data artifacts, optimistic threshold choice, or poor calibration in a new
  population could explain apparent utility.
  解决：Add external validation, calibration plots and metrics, decision-curve
  analysis, threshold rationale, missingness analysis, and safety/clinical
  workflow constraints. Narrow the claim if external validation is unavailable.
  决定性 readout：The claim is supported if discrimination, calibration, and
  decision-curve benefit remain acceptable in an independent cohort. It is
  weakened if calibration fails, net benefit disappears, or performance drops
  under prespecified thresholds.

## Computer Science / AI

- [Critical] Benchmark gains may be caused by leakage or weak baselines.
  具体问题：The manuscript claims state-of-the-art performance, but the benchmark
  split is not audited for leakage and baseline implementations appear to use
  older hyperparameters or weaker training budgets than the proposed method.
  为什么严重：A benchmark result does not establish algorithmic advance if test
  examples leak into training, if preprocessing uses future labels, or if
  baselines are under-tuned. This directly threatens both novelty and technical
  validity.
  证据：
  - 稿件内部证据：The Methods describe a random split but do not report
    entity-level grouping, deduplication, leakage checks, baseline search budget,
    or independent reimplementation details.
  - 外部证据/标准：ACM artifact review and badging defines expectations for
    available, evaluated, and validated computational artifacts:
    https://www.acm.org/publications/policies/artifact-review-and-badging-current
  影响：The claimed superiority may reflect evaluation design rather than a real
  method improvement.
  替代解释/漏洞：Duplicate leakage, subject/entity overlap, preprocessing leakage,
  hyperparameter asymmetry, unreported failed baselines, or random-seed
  instability could explain the result.
  解决：Use leakage-free grouped splits, deduplication, matched baseline tuning
  budgets, ablations, seed confidence intervals, and public code/configs for
  reproduction.
  决定性 readout：The claim is supported if gains persist under leakage-free
  splits, matched baselines, ablations, and independent reruns. It is weakened or
  must be narrowed if gains vanish after deduplication/grouping or under matched
  baseline tuning.
