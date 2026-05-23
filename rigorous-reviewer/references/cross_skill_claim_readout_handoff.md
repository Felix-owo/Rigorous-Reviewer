# Cross-Skill Claim-Readout Handoff

Use when a manuscript, proposal, figure set, dataset, or review conclusion
depends on biological protocol-derived evidence. This handoff is the shared
interface between Rigorous Reviewer and Biological Protocol Reviewer.

## Purpose

Map manuscript claims to the protocol readouts and execution details needed to
support them. The handoff prevents a manuscript review from treating a weak
method as strong evidence, and prevents a protocol rewrite from optimizing a
readout without knowing which scientific claim it must defend.

## Required mapping

| Field | Required content |
|---|---|
| claim_id | Stable ID for the manuscript/proposal claim. |
| claim_text | Exact claim or conclusion under review. |
| evidence_role | decisive / supporting / contextual / exploratory. |
| readout_id | Stable protocol readout ID. |
| readout_supports | What the readout can support if it passes. |
| protocol_step_or_method | SOP section, method, assay, proof-of-measurement, or analysis step. |
| parameter_authority | original / local validated / external benchmark / recommended-unvalidated / unresolved. |
| qc_gate | QC threshold, positive/negative control, fail action, and record field. |
| failure_mode | False-positive, false-negative, safety, reproducibility, or interpretability risk. |
| manuscript_impact | How the claim changes if the readout or protocol gate fails. |
| revision_action | Add control / add validation / narrow claim / mark preliminary / author input needed. |
| source_ids | Evidence-ledger or source-table IDs supporting the mapping. |

## Rules

- A claim cannot be marked strongly supported if its decisive readout has an
  unresolved parameter authority or missing QC gate.
- A protocol readout cannot be treated as decisive unless it has a matching
  claim, control logic, acceptance criterion, and failure interpretation.
- Recommended but unvalidated parameters force either local validation,
  mini-pilot gating, or claim narrowing.
- If the handoff is used in a review, record it in the evidence ledger. If used
  in an SOP, record it in readout contracts and review-to-SOP mapping.
- Use `schemas/claim_readout_handoff.schema.json` and
  `scripts/check_claim_readout_handoff.py` when saving a machine-readable
  handoff artifact.
