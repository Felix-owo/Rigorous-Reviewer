# Calibration Protocol

Use this protocol during comprehensive review to calibrate severity, novelty, and
methodological skepticism against gold or gold-adjacent papers in the same or
nearby research area.

## Contents

- Purpose
- Gold Paper Search
- Calibration Dimensions
- FNR / FPR / Balanced Accuracy
- Required Output
- Guardrails

## Purpose

Calibration prevents two failure modes:

- over-severity: rejecting credible field-standard work because the reviewer asks
  for unrealistic evidence;
- under-severity: accepting exciting claims that weaker historical papers also
  made before later correction, failed replication, retraction, benchmark
  leakage, or claim narrowing.

## Gold Paper Search

Search for 5-12 papers or artifacts close to the manuscript's domain, method, and
claim type:

- **Positive anchors:** top-journal or top-venue papers, landmark methods,
  guidelines, benchmark-defining papers, widely reused datasets, independently
  replicated studies, theorem sources, clinical trials, or standards.
- **Negative anchors:** retractions, expressions of concern, failed replications,
  benchmark-leakage reports, major post-publication critiques, contrary
  theorems/counterexamples, clinical trial failures, or papers whose claims were
  later narrowed.
- **Boundary anchors:** solid but incremental papers, negative/null results,
  methods that are useful but not conceptually transformative, and papers that
  are accepted in specialized venues but not top-tier by novelty.

Prefer primary papers, official guidelines, benchmark papers, trial records,
retraction notices, replication studies, field standards, and public artifacts.
Label preprints as provisional.

## Calibration Dimensions

For each anchor, extract:

```text
Citation / identifier:
Why it is comparable:
Anchor label: positive / negative / boundary / provisional
Claim type:
Evidence standard used:
Known outcome or community status:
Main methodological lesson:
Novelty lesson:
Logic / inference lesson:
Relevance to current manuscript:
```

Then calibrate the current manuscript on:

1. **Innovation:** stronger, similar, weaker, or orthogonal to positive anchors.
2. **Method solidity:** stronger, similar, weaker, or not comparable.
3. **Logic chain stability:** whether the central conclusion survives the
   false-positive paths revealed by anchors.
4. **Reporting and reproducibility:** whether current materials meet the bar set
   by accepted anchors and avoid problems seen in negative anchors.
5. **Revision feasibility:** whether decisive fixes are normal field practice or
   would require a different study.

## FNR / FPR / Balanced Accuracy

Do not fabricate numeric accuracy. Compute numeric estimates only when enough
labeled anchors are available and their outcomes are clear:

- **True positive:** the reviewer flags a serious issue in a negative anchor.
- **False negative:** the reviewer would not flag a serious issue in a negative anchor.
- **True negative:** the reviewer does not flag rejection-level issues in a
  positive anchor.
- **False positive:** the reviewer would reject or over-penalize a positive anchor.

Use:

```text
FNR = false negatives / (true positives + false negatives)
FPR = false positives / (false positives + true negatives)
Balanced accuracy = (true positive rate + true negative rate) / 2
```

If fewer than three positive and three negative labeled anchors are available,
provide a qualitative calibration statement instead of numeric FNR/FPR.

## Required Output

Add a concise calibration section to the final report:

```text
Calibration Against Gold / Near-Gold Papers:
- Anchor set: <number and source types>
- Closest positive anchors: <citations and relevance>
- Closest negative or cautionary anchors: <citations and relevance>
- Innovation calibration: <stronger/similar/weaker/orthogonal + why>
- Method calibration: <stronger/similar/weaker/not comparable + why>
- Logic stability calibration: <what historical loopholes this manuscript does or does not close>
- FNR/FPR estimate: <numeric only if labeled anchors are adequate; otherwise qualitative>
- Confidence adjustment: <how calibration changes severity or recommendation>
```

## Guardrails

- A famous paper is not automatically a positive anchor; use it only if the
  current claim is genuinely comparable.
- A retracted or criticized paper is not automatically a negative anchor for the
  current manuscript; name the shared failure mode.
- Do not use citation count alone as evidence of truth.
- Do not let calibration replace article-specific critique. It sets the bar; it
  does not decide the manuscript by analogy.
