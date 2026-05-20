# Article-Specific Evidence and Literature Mapping

Use this reference for every review. Its purpose is to prevent generic comments
by forcing the reviewer to build a dossier tailored to the article's exact
field, central claims, methods, data, proofs, materials, clinical context,
benchmarks, and evidence standards.

## Contents

- Required Dossier
- Six-Domain Source Routes
- Fusion-Field Source Routes
- Query Patterns
- Evidence Threshold Patterns
- Output Expectations

## Required Dossier

Before writing the review, build an article-specific dossier:

1. **Claim Map**
   - Central claim, secondary claims, and which claim is the foundation for all
     others.
   - Domain map: biology, chemistry, physics, mathematics, medicine, computer
     science, or a fusion of these.
   - Claim type: mechanism, compound/material, measurement, theorem, clinical
     inference, algorithm/system, benchmark, dataset, or cross-domain bridge.

2. **Classic Anchors**
   - Landmark papers, canonical theories, field-defining experiments, standard
     datasets, benchmark suites, clinical trials, mathematical theorems,
     chemical structures, measurement standards, or official reporting guidelines.
   - Reviews may orient the field, but issue-level criticism should prefer
     primary work, official standards, direct data, or theorem sources.

3. **Canonical Methods and Evidence Thresholds**
   - Gold-standard methods, controls, assumptions, characterization packages,
     proof standards, measurement uncertainty, clinical validation, benchmark
     design, robustness checks, and reproducibility expectations.
   - Known artifacts, false positives, confounders, data leakage risks, hidden
     assumptions, model misspecification, impurity, systematic error, and common
     overreach patterns.

4. **Current Frontier**
   - Recent peer-reviewed or accepted literature.
   - Relevant arXiv, bioRxiv, medRxiv, conference, or working-paper sources when
     the field is fast-moving.
   - Label provisional sources clearly; use them as frontier context, not settled
     consensus unless independently supported.
   - Include contrary or narrowing evidence, not only supportive literature.

5. **Evidence Gap Table**
   - For each central claim: required evidence, evidence provided, missing
     evidence, strongest loophole, plausible alternative explanation, and decisive test.

## Six-Domain Source Routes

Choose the route that matches the manuscript:

- **Biology:** PubMed, Europe PMC, Nature/Cell/Science and specialist journals,
  method papers, public omics repositories, BioStudies/GEO/SRA/ArrayExpress,
  protocol papers, ARRIVE/MDAR/BioSharing/EQUATOR guidance, bioRxiv as provisional.
- **Chemistry:** ACS/RSC/Elsevier/Wiley journals, CCDC/CSD, wwPDB where relevant,
  NMR/MS/crystallography data, ACS Research Data Guidelines, IUPAC standards,
  reaction databases, computational chemistry benchmarks.
- **Physics:** APS/AIP/IOP/Nature Physics journals, arXiv as frontier context,
  instrument standards, calibration references, simulation benchmarks, uncertainty
  and systematic-error literature, public experimental datasets where available.
- **Mathematics:** MathSciNet, zbMATH, arXiv, journal archives, theorem sources,
  monographs, prior lemmas, counterexamples, proof techniques, and canonical
  examples testing sharpness.
- **Medicine:** PubMed, ClinicalTrials.gov/WHO ICTRP, EQUATOR guidelines,
  CONSORT, PRISMA, STROBE, SPIRIT, TRIPOD/TRIPOD+AI, ICMJE guidance, trial
  protocols/SAPs, cohort datasets, medRxiv as provisional.
- **Computer Science / AI:** ACM/IEEE/USENIX/NeurIPS/ICML/ICLR/CVPR/ACL venues,
  arXiv as provisional, benchmark leaderboards, dataset cards/model cards,
  code repositories, ACM artifact review standards, NeurIPS/ICLR/AAAI
  reproducibility checklists.

## Fusion-Field Source Routes

- **Bioinformatics / computational biology:** pair biological literature and
  assay standards with CS/AI benchmark, leakage, and reproducibility standards.
- **Medical AI:** combine TRIPOD/CONSORT/STROBE/DECIDE-AI-style clinical reporting
  with ML external validation, calibration, leakage, and subgroup robustness.
- **Chemical biology / medicinal chemistry:** combine chemical identity/purity and
  target-engagement standards with biological specificity and disease-model rigor.
- **Biophysics:** combine physical measurement/calibration/uncertainty with
  biological perturbation and physiological relevance.
- **Computational chemistry / materials AI:** combine chemical/physical
  validation, quantum/classical assumptions, benchmark splits, uncertainty, and
  experimental confirmation.
- **Mathematical biology / physics-informed ML:** combine theorem assumptions,
  identifiability, stability, boundary conditions, and empirical validation.

## Query Patterns

Use domain-specific substitutions:

- `"<central claim>" <domain> <method> validation controls`
- `"<method/model/assay>" benchmark baseline ablation reproducibility`
- `"<compound/material>" characterization purity NMR MS X-ray`
- `"<physical phenomenon>" measurement uncertainty calibration systematic error`
- `"<theorem/result>" counterexample assumption sharpness`
- `"<clinical claim>" external validation calibration endpoint trial`
- `"<AI method>" data leakage benchmark contamination ablation`
- `"<fusion claim>" <domain1> <domain2> validation`
- `site:arxiv.org <method> <benchmark or limitation>`
- `site:biorxiv.org OR site:medrxiv.org <biomedical claim> validation controls`

## Evidence Threshold Patterns

- **Biological mechanism:** perturbation, rescue/epistasis, orthogonal readouts,
  alternative-mechanism exclusion, biological replication.
- **Chemical structure/activity:** identity, purity, full characterization,
  controls, reproducible yields, selectivity, kinetics/mechanism where claimed.
- **Physical discovery/measurement:** uncertainty budget, systematics, calibration,
  null tests, independent observables, theory-regime validity.
- **Mathematical theorem:** exact assumptions, complete proof, boundary cases,
  relationship to prior work, counterexamples and sharpness.
- **Clinical/medical claim:** endpoint validity, bias control, registration,
  independent validation, harms, clinical utility, reporting guideline compliance.
- **Computer science/AI claim:** benchmark validity, leakage control, baselines,
  ablations, statistical testing, failure cases, artifact availability.
- **Interdisciplinary bridge claim:** every relevant domain standard passes, and
  the mapping between domains is validated directly.

## Output Expectations

In the final review, include a concise **Field Evidence Map** listing:

- Domain and fusion map.
- Classic anchors.
- Canonical methods and evidence thresholds.
- Current frontier or provisional sources when relevant.
- Main loophole, false-positive, confounding, edge-case, leakage, source-bias, or
  overreach risks.

Every Critical or Major issue must cite at least one source from this dossier or
an additional source found during targeted search.
