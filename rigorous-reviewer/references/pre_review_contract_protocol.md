# Pre-Review Contract Protocol

Use after claim reconstruction and before final severity, recommendation, or
reviewer-panel synthesis. The purpose is to prevent post-hoc rubric drift: the
review may become more specific after reading the full artifact, but it must not
quietly weaken the standard required to support the central claim.

## Contract inputs

Build the contract from the title, abstract, target venue, declared claims,
figures/tables/results/proofs/models listed by the user, field, and any supplied
metadata. If only partial material is available, mark the contract as
`partial_material_contract` and name the missing decisive files.

## Required fields

Use `templates/review_contract_template.json` when saving a machine-readable
contract.

- `central_claim_dependency_map`: each central claim, required evidence, and the
  dependent figure/table/result/proof/model/benchmark.
- `decisive_evidence_thresholds`: what would make the claim supported rather than
  merely plausible.
- `mandatory_reviewer_dimensions`: domain, method/statistics, reproducibility,
  novelty, reporting, and fusion-bridge dimensions required for this artifact.
- `failure_conditions`: conditions that force Major Revision or Reject even if
  writing quality is high.
- `evidence_that_changes_recommendation`: explicit support, weakening, and
  claim-narrowing readouts.
- `prohibited_post_hoc_standard_shifts`: standards that must not be removed,
  weakened, or replaced after reading the full manuscript.

## Lock rules

- The contract is a standard lock, not a conclusion lock.
- Later review passes may add paper-specific issues and stronger field-specific
  tests.
- Later review passes must not downgrade a failure condition without explicit
  evidence that the condition does not apply.
- Any contract change after full review must be logged as `contract_amendment`
  with reason and evidence.
- If the contract cannot be completed because material is missing, preserve the
  missing material as a review limitation and do not fill it with assumptions.

## Recommendation implications

- A locked `reject_if` failure condition blocks Accept, Minor Revision, and Major
  Revision unless the review explains why the condition is inapplicable.
- A locked `major_revision_if` failure condition blocks Accept and Minor
  Revision until the decisive readout is supplied or the central claim is
  narrowed.
- A locked reporting-only condition cannot be inflated into rejection unless it
  also threatens interpretation, reproducibility, ethics, safety, or evidence
  traceability.
