# Revision Response Bridge

Use only after the review judgment is complete. This bridge maps reviewer issues
to revision strategy; it does not replace the review, soften severity, invent
experiments, or draft unsupported rebuttal prose.

## Action map

Map each Critical, Major, Minor, and reporting issue to:

| Issue ID | Reviewer concern | Severity | Required action | Manuscript location | Evidence needed | Response posture |
|---|---|---|---|---|---|---|

Allowed `Required action` labels:

- `ACCEPT_TEXT`
- `ACCEPT_ANALYSIS`
- `ACCEPT_EXPERIMENT`
- `SOFTEN_CLAIM`
- `ADD_CONTROL`
- `ADD_REPLICATION`
- `ADD_PUBLIC_DATA_VALIDATION`
- `ADD_MECHANISTIC_READOUT`
- `ADD_BENCHMARK_OR_BASELINE`
- `ADD_PROOF_REPAIR`
- `ADD_DATA_CODE_RELEASE`
- `JUSTIFIED_DISAGREEMENT`
- `AUTHOR_INPUT_NEEDED`
- `NOT_RESPONDABLE_WITH_CURRENT_EVIDENCE`

Allowed `Response posture` labels:

- `full_acceptance`
- `partial_acceptance_with_boundary`
- `evidence_added`
- `claim_narrowed`
- `justified_disagreement_with_source`
- `cannot_answer_without_author_input`
- `not_feasible_without_new_study`

## Hard prohibitions

- Do not invent completed experiments, new analyses, figure panels, line numbers,
  citations, source-data files, institutional approvals, or manuscript changes.
- Do not turn a Critical or Major issue into a wording-only response unless the
  original issue explicitly says the decisive evidence already exists.
- Do not draft final rebuttal prose unless the user supplies the author-side
  changes or asks for clearly labeled placeholders.
- If a required action needs author confirmation, use
  `AUTHOR_INPUT_NEEDED` rather than guessing.
