# Figure Claim Audit

Use when figures, panels, tables, graphical models, images, plots, source data,
or visual summaries are central to the manuscript's claims.

## Per-figure contract

For each central figure/table:

| Field | Required question |
|---|---|
| Figure/table ID | Which artifact is being audited? |
| Claim defended | What exact claim does this artifact support? |
| Decisive panel/readout | Which panel or metric would make the claim convincing? |
| Contextual panel/readout | Which panels only provide context or illustration? |
| Quantification match | Does the quantification measure what the image/experiment claims? |
| Control match | Are positive, negative, vehicle, baseline, sham, FMO, mock, null, or boundary controls appropriate for the claim? |
| Statistics and n | Are n, experimental unit, error bars, tests/models, uncertainty, and exclusions explicit? |
| Source data | Are source data, raw images, code, or tables available enough to verify the plot? |
| Redundancy | Does the figure add decisive evidence or repeat non-independent evidence? |
| Survival test | Would the central claim survive if this artifact were removed? |

## Review rules

- Do not ask for prettier figures unless readability affects interpretation.
- Do not credit model cartoons, schematic arrows, or representative images as
  decisive evidence unless paired with quantitative and controlled data.
- If the decisive panel lacks controls, statistics, n, source data, or a
  matched readout, map the problem to a Major or Critical issue depending on
  claim dependency.
- For image-heavy biology, flow, microscopy, pathology, or spatial claims, check
  gating/segmentation/thresholding, representative image selection, batch
  effects, and quantification independence.
- For computational benchmark figures, check leakage, baseline parity, dataset
  splits, uncertainty, ablations, and independent replication.
