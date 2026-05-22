# Claim Maturity Gate

Use before final recommendation to state how mature the central claim is,
separately from Accept / Minor Revision / Major Revision / Reject. This borrows
protocol-readiness logic for manuscript evidence strength.

## Claim maturity levels

| Level | Label | Definition | Typical recommendation pressure |
|---|---|---|---|
| 0 | Speculative / not yet supported | Central claim lacks decisive internal evidence, has unresolved major loopholes, or depends on missing methods/data/proof. | Reject or Major Revision with major claim narrowing. |
| 1 | Plausible but fragile | Evidence is suggestive, but decisive controls, validation, benchmark, proof repair, cohort, or protocol-derived readout remains missing. | Major Revision by default. |
| 2 | Locally supported / bounded | Main claim is supported in the presented system or dataset but external validity, mechanism, robustness, or independent replication is limited. | Major or Minor depending on novelty and scope. |
| 3 | Independently robust | Claim survives decisive controls, alternative-explanation tests, appropriate benchmarks/proofs, source/data audit, and scope boundaries. | Minor Revision or Accept if novelty and reporting also pass. |

## Required fields

| Field | Required content |
|---|---|
| Claim ID | Stable claim identifier. |
| Current maturity | Level 0, 1, 2, or 3. |
| Evidence basis | Manuscript-internal evidence plus external standard/anchor. |
| Blocking loophole | Strongest unresolved false-positive, false-negative, proof, benchmark, clinical, or protocol-derived risk. |
| Maturity upgrade readout | Smallest decisive result or repair that moves the claim up one level. |
| Required narrowing | Exact claim language if the upgrade readout is not supplied. |

## Rules

- Claim maturity is not a style score.
- A high novelty score cannot compensate for Level 0 or Level 1 evidence on the
  central claim.
- If a claim depends on protocol-derived evidence, use
  `cross_skill_claim_readout_handoff.md` before assigning Level 2 or Level 3.
- Level 3 requires adequate reporting, data/material/code/protocol availability,
  or a justified restriction for independent expert audit.
