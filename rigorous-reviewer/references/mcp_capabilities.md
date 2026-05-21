# MCP Capabilities for Rigorous Reviewer

Use this file only when the host agent exposes MCP servers, tools, resources, or
prompts, or when the user asks which MCP capabilities can strengthen the review.
MCP is optional. This skill must still work without MCP.

## MCP Role Boundary

MCP capabilities may support evidence gathering, source verification, structured
artifact handling, and deterministic validation. They do not replace the
reviewer's synthesis, severity ranking, field judgment, or final recommendation.

Before using MCP:

1. Confirm the capability is visible in the current host.
2. Identify whether it is local-only, networked, authenticated, or third-party.
3. Use the narrowest query needed for the review.
4. Preserve provenance: server name, tool/resource/prompt used, query, returned
   identifiers, date accessed when available, and review issue affected.
5. Do not disclose confidential manuscripts, unpublished data, private file
   paths, credentials, or personally identifying information to a networked MCP
   service unless the user explicitly approves that transfer.

## Recommended Capability Matrix

| Capability class | Useful for | Minimum provenance to record | Privacy default |
| --- | --- | --- | --- |
| Paper and citation search | DOI/PMID/arXiv lookup, gold-anchor discovery, contrary evidence, retractions, replication status | query, database, identifiers, retrieval date, why comparable | Safe for public titles/DOIs; ask before sending private text |
| Public scientific databases | genes, proteins, variants, pathways, compounds, structures, clinical trials, datasets, patents, materials records | database, endpoint, accession or identifier, result summary, affected claim | Prefer identifiers; avoid raw unpublished data |
| Web/search | guidelines, standards, public repositories, reporting checklists, venue policy, public benchmark pages | URL, publisher/organization, date accessed, issue affected | Public queries only unless user approves |
| Filesystem/document | local PDF, DOCX, supplements, figures, tables, code, saved reports | local path, extracted artifact, page/section/table, transformation performed | Local-only preferred; do not publish outputs by default |
| GitHub/code artifact | repository inspection, commit/release history, CI status, code reproducibility, benchmark scripts | repo URL, commit SHA/tag, file path, command/check inspected | Public repos by default; ask before private repos |
| Citation manager/bibliography | citation normalization, BibTeX/RIS export, DOI metadata, duplicate citation checks | source record, DOI/PMID/arXiv, normalized citation | Use public metadata only |
| Benchmark/evaluation | run local validators, schema lint, benchmark scoring, golden fixture checks | command/tool, input fixture, score or failure, version | Local-only unless user asks to publish |
| Clinical/regulatory | trials, approvals, safety labels, adverse event sources, reporting guideline checks | registry/database, identifier, status/date, endpoint or claim affected | Public identifiers only |
| Math/proof tooling | theorem dependencies, symbolic checks, counterexample search, formal proof artifact inspection | theorem/source, assumptions, tool result, counterexample if found | Local/public sources only |
| Chemistry/materials tooling | structure/spectra checks, compound identity, crystallography, materials records, property databases | identifier, database, measurement/structure record, uncertainty if available | Prefer public identifiers; avoid unpublished structures |

## Review-Time Routing

Use MCP selectively:

- **Calibration anchors:** paper/citation search plus public databases.
- **Manuscript reconstruction:** local filesystem/document MCP for PDFs,
  supplements, figures, tables, and code archives.
- **Domain verification:** database MCP for accessions, compounds, structures,
  variants, clinical trials, materials, datasets, and public benchmark records.
- **Code and benchmark review:** GitHub/code MCP plus local benchmark/evaluation
  tools.
- **Structured output:** local filesystem plus schema/benchmark tools.
- **Venue and reporting standards:** web/search MCP for official public
  policies and checklists.

## Disclosure Block

If MCP was used, add a concise disclosure to the final report:

```text
MCP Capabilities Used:
- <server/capability>: <tool/resource/prompt>, <query or artifact>, <evidence returned>
- Privacy note: <local-only / public query / user-approved networked transfer>
- Limitations: <unavailable full text, missing API key, incomplete metadata, no matching record>
```

If no MCP was used, omit this block unless the absence of MCP explains a review
limitation.

## Red Lines

Rewrite the review or ask the user before proceeding if any of these occur:

- A networked MCP tool would receive unpublished manuscript text without
  explicit user approval.
- A result is cited without database, URL, accession, DOI/PMID/arXiv, commit, or
  other retrieval handle.
- MCP output is treated as authoritative despite conflicting manuscript-internal
  evidence or missing source provenance.
- A broad search result is used as evidence without checking the primary source.
- Local private artifacts are copied into a public repository, issue, release, or
  external service without explicit user request.
