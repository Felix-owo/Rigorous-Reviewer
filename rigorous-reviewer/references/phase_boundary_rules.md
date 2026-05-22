# Review Phase Boundary Rules

Use for long-form reviews, saved intermediate artifacts, multi-agent work, or
reviews resumed across sessions. Phase boundaries prevent premature synthesis
and make final criticism traceable.

## Phase 0 - Intake and claim reconstruction

Allowed writes:

- `Review_Intake`
- `Claim_Map`
- `Missing_Material_List`
- `User_Material_Log`

Forbidden writes:

- final recommendation
- final severity labels
- revision roadmap
- claim-level accept/reject decision

## Phase 1 - Evidence and domain audit

Allowed writes:

- `Evidence_Dossier`
- `Domain_Standards_Map`
- `External_Anchor_List`
- `Figure_Claim_Audit`
- `Calibration_Anchor_Map`

Forbidden writes:

- final recommendation before panel synthesis
- issue downgrades based on rhetorical quality
- replacement of user-supplied evidence with generic background without an
  exclusion log

## Phase 2 - Independent reviewer passes

Allowed writes:

- `EIC_Report`
- `Methods_Statistics_Report`
- `Domain_Report`
- `Interdisciplinary_Report`
- `Devil_Advocate_Report`

Forbidden writes:

- cross-reviewer synthesis inside individual reviewer reports
- final editorial decision
- new source claims without evidence-ledger entries

## Phase 3 - Editorial synthesis

Allowed writes:

- `Final_Review_Report`
- `Recommendation`
- `Minimum_Revision_Bar`
- `Review_to_Revision_Action_Map`

Forbidden writes:

- new criticism not traceable to Phase 1 or Phase 2
- weakening of pre-review failure conditions without a logged contract amendment
- invented line numbers, experiments, citations, figures, or author changes

## Traceability rule

Every final Critical or Major issue must trace to at least one Phase 1 evidence
entry and one Phase 2 reviewer perspective, or explicitly state that the issue is
based on missing decisive material.
