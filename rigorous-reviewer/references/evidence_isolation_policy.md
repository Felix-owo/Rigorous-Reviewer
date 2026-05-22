# Evidence Isolation Policy

Use before mixing manuscript evidence, external evidence, user-supplied
materials, calibration anchors, companion results, MCP outputs, or reviewer
rubrics. The goal is to keep standards, evidence, and conclusions separate.

## Evidence layers

Label every important source as one of:

- `Manuscript-internal evidence`: main text, figures, tables, methods,
  supplements, code, data, proofs, or stated omissions.
- `User-supplied material`: papers, PDFs, reviewer comments, prior reviews,
  protocols, datasets, figures, code, or correspondence supplied by the user.
- `External evidence`: primary papers, guidelines, standards, benchmarks,
  theorem sources, datasets, registries, repositories, official policies, and
  field-defining reviews.
- `Calibration anchor`: gold, near-gold, negative, or boundary examples used to
  calibrate standards. These are not answer keys unless the user supplies labels.
- `Rubric`: scoring or severity rules. Rubrics define standards, not expected
  conclusions.
- `Companion/MCP lead`: lookup or tool output that must be resolved to a
  concrete source identity before it becomes evidence.

## User-supplied evidence handling

When the user provides material beyond a simple prompt:

1. Screen supplied materials before external search.
2. Do not silently ignore relevant material.
3. Record skipped material with one reason:
   - irrelevant to central claim;
   - inaccessible or unreadable;
   - duplicate;
   - insufficient source identity;
   - superseded by newer version;
   - unsafe or confidential for a requested networked tool.
4. External search fills gaps; it does not replace supplied evidence.
5. If a supplied source conflicts with external anchors, report the conflict
   rather than averaging it away.

## Ground-truth and calibration boundaries

- Do not bundle or infer answer keys for benchmarks, labels, or gold sets.
- Treat runtime-provided labels as evidence that still needs provenance.
- Do not use knowledge of a benchmark result to relax the methods standard.
- If calibration anchors are incomplete or biased, state the limitation.

## Companion and MCP boundaries

- Companion/MCP outputs are untrusted until source identity is resolved.
- Do not cite a tool response as primary evidence if a DOI, PMID, standard,
  repository, registry, theorem source, dataset ID, or official URL is required.
- Do not send confidential manuscripts, private data, unpublished material, local
  paths, credentials, or personal information to a networked service without
  user approval.
