# Six-Domain and Fusion-Field Review Standards

Use this file for every review. It defines top-journal-level evidence thresholds
for biology, chemistry, physics, mathematics, medicine, computer science, and
their fusion fields. The purpose is to force expert loophole finding rather than
generic peer-review comments.

## Contents

- Top-Journal Innovation Test
- Biology
- Chemistry
- Physics
- Mathematics
- Medicine
- Computer Science and AI
- Interdisciplinary Fusion Review
- Minimum External Support Rule

## Top-Journal Innovation Test

A claim is top-journal-level only if it passes all four checks:

1. **Conceptual delta:** the work changes a model, mechanism, theorem, method,
   treatment, measurement capability, benchmark standard, or field practice.
2. **Decisive evidence:** the central claim survives the strongest alternative
   explanation using field-appropriate proof, validation, controls, or benchmarks.
3. **External visibility:** a serious adjacent-field reader would understand why
   the result matters beyond a narrow technical variation.
4. **Reproducible basis:** data, code, materials, spectra, structures, proofs,
   protocols, cohorts, or benchmarks are sufficiently inspectable to audit the
   conclusion.

Treat "first in this exact setting" as insufficient unless it changes a field
model or enables a clearly new capability.

## Biology

### Evidence Threshold

- Mechanistic claims require perturbation, rescue or epistasis logic, time/dose
  structure where relevant, orthogonal readouts, and exclusion of toxicity,
  stress, developmental-stage, batch, sex, strain, or cell-state confounders.
- Omics claims require donor/animal replication, batch/doublet/ambient controls,
  multiple-testing control, annotation validation, sensitivity analysis, and
  public data/code sufficient to audit preprocessing.
- Lineage, origin, or trajectory claims require anchor populations, positive and
  negative lineage controls, sampling-depth analysis, false-positive modeling,
  and orthogonal validation.
- Animal work requires randomization/blinding where applicable, exact n, inclusion
  and exclusion criteria, sex/age/strain, experimental unit, effect sizes, and
  ethics approval.

### Loopholes to Hunt

- Cell-state similarity mistaken for lineage or causality.
- Marker expression treated as identity or function without validation.
- Pseudoreplication: cells or technical replicates treated as biological replicates.
- Missing negative controls for antibodies, perturbations, reporters, lineage labels,
  or imaging segmentation.
- Batch, dissociation, culture, stress, or sample-processing artifacts.
- Mouse-human translational overclaim without human validation.

### Anchor Standards

- Nature Portfolio life-science reporting summaries require statistics,
  randomization/blinding explanations, sample-size information, data availability,
  and code availability where applicable.
- ARRIVE 2.0 defines minimum reporting for animal research, including study design,
  sample size, inclusion/exclusion criteria, randomization, blinding, outcome
  measures, statistical methods, experimental animals, procedures, and results.

## Chemistry

### Evidence Threshold

- New compounds/materials require identity and purity evidence appropriate to the
  chemistry: NMR, MS/HRMS, IR, UV-vis, elemental analysis, chromatography, X-ray,
  CIF/checkCIF, spectroscopy, microscopy, thermal analysis, or other field-specific
  characterization.
- Reaction claims require controls, reproducible yields, selectivity, substrate
  scope with limitations, negative examples, stoichiometry, purity of reagents,
  catalyst lifetime/stability, kinetic or mechanistic evidence when mechanism is claimed.
- Computational chemistry claims require level of theory, basis sets, convergence,
  solvent/temperature assumptions, benchmark comparison, uncertainty, and
  experimental validation where the claim is empirical.
- Chemical biology/medicinal chemistry claims require target engagement,
  selectivity, orthogonal assays, off-target risk, PK/PD or exposure logic when
  biological conclusions depend on compound action.

### Loopholes to Hunt

- Structure assigned from insufficient spectra or missing purity evidence.
- Catalytic activity caused by impurities, leaching, degradation, support effects,
  or unrecognized phase changes.
- Mechanistic schemes inferred from correlation without kinetic/isotopic/control
  evidence.
- Selective reporting of successful substrate scope without failure classes.
- Computational energies overinterpreted without uncertainty or validation.

### Anchor Standards

- ACS Research Data Guidelines state that data should be transparent and rigorous
  enough to allow trained researchers to reproduce experiments and evaluate the
  approach.
- ACS/JACS author guidance requires crystallographic data files and validation
  materials for new small-molecule structures where relevant.

## Physics

### Evidence Threshold

- Experimental claims require calibration, uncertainty budget, systematic error
  model, background subtraction logic, instrument limits, controls/null tests,
  independent observables, and comparison to known physical constraints.
- Theoretical claims require stated approximations, dimensional consistency,
  regime of validity, boundary/initial conditions, limiting cases, conservation
  laws, and comparison to prior theory or experiment.
- Simulation claims require numerical convergence, resolution/mesh/time-step
  sensitivity, boundary conditions, parameter uncertainty, code availability where
  central, and validation against analytic limits or benchmark experiments.

### Loopholes to Hunt

- Statistical significance reported without systematics.
- Model fitted with too many free parameters or non-identifiable parameters.
- Experimental regime differs from the theory's assumptions.
- Simulation artifacts from discretization, boundary conditions, finite-size
  effects, initialization, or unphysical parameter choices.
- Incremental performance over known limits framed as conceptual breakthrough.

### Anchor Standards

- Nature Portfolio physical-sciences reporting standards emphasize transparency
  and reproducibility across science, including characterization, analytical
  design, data sharing, code/algorithm review when central, and code availability.

## Mathematics

### Evidence Threshold

- Theorem statements must specify all assumptions, domains, regularity,
  quantifiers, constants, boundary cases, and dependencies on prior results.
- Proofs must close every implication, compactness/limit/interchange step,
  measurability/integrability condition, existence/uniqueness assumption,
  algorithmic termination claim, and edge case.
- Novelty must be assessed against strongest prior theorems, not terminology
  changes or a special case hidden by notation.
- Examples should test sharpness, necessity of assumptions, and boundary cases;
  counterexamples must be considered for broadened claims.
- Computational or experimental mathematics must include reproducible code/data
  and distinguish conjectural evidence from proof.

### Loopholes to Hunt

- Hidden regularity, boundedness, compactness, independence, or genericity assumptions.
- Invalid exchange of limits, sums, integrals, derivatives, expectations, or
  optimization operators.
- A theorem that is a corollary of known work but is framed as new.
- Proof of a weaker statement than the abstract claims.
- Missing edge cases: zero, infinity, singularity, non-compactness, degenerate
  parameters, adversarial examples, or equality cases.

### Anchor Standards

- AMS Mathematical Reviews guidance says mathematical reviews should sketch proof
  ideas where feasible, connect work to related approaches, and describe errors
  precisely with evidence such as a counterexample or exact reference.

## Medicine

### Evidence Threshold

- Clinical trial claims require prespecified endpoints, trial registration,
  protocol/SAP access, allocation concealment, randomization/blinding where
  applicable, CONSORT/SPIRIT-style reporting, intention-to-treat logic, harms,
  missing data handling, clinically meaningful effect size, and generalizability.
- Observational claims require clear target population, exposure/outcome
  definitions, confounder model, missingness, sensitivity analyses, negative or
  falsification controls where possible, and STROBE-style reporting.
- Diagnostic/prognostic model claims require external validation, calibration,
  discrimination, decision-curve or clinical utility analysis, subgroup
  performance, and TRIPOD/TRIPOD+AI-style reporting where relevant.
- Systematic reviews require transparent eligibility, search strategy, screening,
  risk of bias, synthesis method, and PRISMA-style reporting.

### Loopholes to Hunt

- Surrogate endpoints framed as clinical benefit without validation.
- Retrospective subgroup or post-hoc endpoint fishing.
- Leakage between training and validation cohorts in medical AI.
- No external validation despite general clinical claims.
- Statistically significant but clinically trivial effects.
- Safety, harms, missingness, and population exclusions buried or underpowered.

### Anchor Standards

- CONSORT provides reporting guidance for randomized trials; PRISMA 2020 provides
  systematic-review checklist guidance; STROBE defines checklist items for
  observational studies; SPIRIT defines protocol content for clinical trials;
  TRIPOD supports reporting of diagnostic/prognostic prediction models.

## Computer Science and AI

### Evidence Threshold

- Algorithmic claims require clear problem definition, assumptions, complexity,
  baseline comparison, ablations, hyperparameter and seed reporting, statistical
  testing, robustness, and failure cases.
- ML/AI claims require leakage-free train/validation/test separation, benchmark
  relevance, strong current baselines, data provenance, annotation quality,
  evaluation metric justification, uncertainty, compute budget, and limitations.
- Systems claims require workload representativeness, scalability, reliability,
  tail behavior, security/fault assumptions, deployment constraints, and
  reproducible artifact or detailed implementation.
- Theoretical CS claims require formal statements, complete proofs, assumptions,
  reductions, lower/upper bound tightness, and relation to known results.

### Loopholes to Hunt

- Data leakage, benchmark contamination, prompt/test overlap, duplicate examples,
  or tuning on test sets.
- Weak or outdated baselines.
- Cherry-picked datasets, seeds, workloads, or metrics.
- Ablations that do not isolate the claimed mechanism.
- Claimed generality from narrow benchmark families.
- Missing code, environment, dependencies, hardware, or evaluation scripts.

### Anchor Standards

- ACM artifact review and badging defines standards for artifacts being evaluated,
  available, and results validated.
- ICLR author guidance emphasizes reproducibility statements, source code,
  assumptions, proofs, datasets, and data-processing details.
- NeurIPS paper checklist guidance targets reproducibility, transparency, ethics,
  limitations, and broader impacts.
- IEEE reproducibility guidance emphasizes enough methodological detail, data
  sharing, and code sharing for independent researchers to obtain the same results.

## Interdisciplinary Fusion Review

### Bridge Claim Audit

For every cross-domain manuscript, name the bridge claim explicitly:

- Biology plus CS: "This model captures biological mechanism or improves biological inference."
- Chemistry plus AI: "This model learns chemical structure-property or reaction rules."
- Physics plus ML: "This model respects or discovers physical law."
- Math plus biology/physics/CS: "This theorem or model applies to the empirical system."
- Medicine plus AI/omics: "This computational signal improves clinically meaningful decisions."

Then ask:

1. Does each domain's evidence standard pass independently?
2. Is the mapping between domains validated, not assumed?
3. Are units, scales, data-generating processes, and assumptions compatible?
4. Would a reviewer from either domain identify a failure invisible to the other?
5. Is novelty in the fusion itself, or merely use of a familiar tool on a new dataset?

### Fusion Loopholes

- A mathematically correct model applied outside its assumptions.
- A high-performing AI model with no biological/chemical/clinical interpretability
  or validation matching the paper's mechanistic claim.
- A physical simulation whose parameters are fitted to match biology but are not
  identifiable or experimentally constrained.
- Medical AI validated only on internal retrospective data.
- Computational chemistry predictions without experimental confirmation for the
  claimed chemical conclusion.
- Bioinformatics discovery without wet-lab or independent cohort validation.

## Minimum External Support Rule

Every Critical or Major issue must cite at least one of:

- a primary paper or landmark theorem,
- an official reporting guideline or society/publisher policy,
- a benchmark or dataset paper,
- a standards document,
- an official clinical trial/model reporting guideline,
- a repository/artifact standard,
- a field-defining review used only for framing.

If no such source is available, label the point as a question rather than a
finding.
