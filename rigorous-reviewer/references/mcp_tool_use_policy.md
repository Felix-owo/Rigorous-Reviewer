# MCP Tool Use Policy for Rigorous Reviewer

Use this file only when the host agent exposes MCP servers, tools, resources, or
prompts, or when the user asks which MCP capabilities can strengthen the review.
MCP is optional. This skill must still work without MCP.

## Precedence

Rigorous Reviewer remains the primary peer-review workflow.

1. Use Rigorous Reviewer logic for all reviewer judgments, severity ranking,
   novelty assessment, claim dependency analysis, and final recommendation.
2. Use MCP only when retrieval, parsing, computation, source verification, or
   deterministic validation is required.
3. Treat MCP outputs as evidence inputs that need provenance, not as final
   conclusions.
4. Do not allow any MCP tool to replace the final Markdown review structure,
   issue-block logic, evidence ledger, or red-line audit.

Before using MCP:

1. Confirm the capability is visible in the current host.
2. Identify whether it is local-only, networked, authenticated, or third-party.
3. Use the narrowest query needed for the review.
4. Preserve provenance: server name, tool/resource/prompt used, query, returned
   identifiers, date accessed when available, and review issue affected.
5. Do not disclose confidential manuscripts, unpublished data, private file
   paths, credentials, or personally identifying information to a networked MCP
   service unless the user explicitly approves that transfer.

## Recommended MCP Tool Classes

| Capability class | Useful for | Minimum provenance to record | Privacy default |
| --- | --- | --- | --- |
| PDF / document parsing | manuscript, figures, methods, supplementary materials, figure legends, references, tables | local path or document ID, page/section/table, extraction method, output artifact | local-only preferred |
| PubMed / Europe PMC / literature retrieval | novelty assessment, claim precedent, contradictory literature, method benchmark papers, citation support | query, database, identifiers, retrieval date, why comparable | public titles/DOIs are safe; ask before sending private text |
| Zotero / citation library | curated personal library, known gold papers, user-maintained citation collections | library/collection, item key, DOI/PMID/arXiv, citation note used | ask before querying private libraries |
| Crossref / DOI validation | DOI metadata, reference mismatch, correction/retraction links, publication status | DOI, returned metadata, relation type, access date | public identifiers only |
| Python / R computation | p-values, confidence intervals, sample size checks, omics QC metrics, figure-level recalculation | script/tool, input data source, formula/model, output, version | local-only unless user approves data transfer |
| Public scientific databases | genes, proteins, variants, pathways, compounds, structures, clinical trials, datasets, patents, materials records | database, endpoint, accession or identifier, result summary, affected claim | Prefer identifiers; avoid raw unpublished data |
| Web/search | guidelines, standards, public repositories, reporting checklists, venue policy, public benchmark pages | URL, publisher/organization, date accessed, issue affected | Public queries only unless user approves |
| Filesystem/document | local PDF, DOCX, supplements, figures, tables, code, saved reports | local path, extracted artifact, page/section/table, transformation performed | Local-only preferred; do not publish outputs by default |
| GitHub/code artifact | repository inspection, commit/release history, CI status, code reproducibility, benchmark scripts | repo URL, commit SHA/tag, file path, command/check inspected | Public repos by default; ask before private repos |
| Benchmark/evaluation | run local validators, schema lint, benchmark scoring, golden fixture checks | command/tool, input fixture, score or failure, version | Local-only unless user asks to publish |
| Clinical/regulatory | trials, approvals, safety labels, adverse event sources, reporting guideline checks | registry/database, identifier, status/date, endpoint or claim affected | Public identifiers only |
| Math/proof tooling | theorem dependencies, symbolic checks, counterexample search, formal proof artifact inspection | theorem/source, assumptions, tool result, counterexample if found | Local/public sources only |
| Chemistry/materials tooling | structure/spectra checks, compound identity, crystallography, materials records, property databases | identifier, database, measurement/structure record, uncertainty if available | Prefer public identifiers; avoid unpublished structures |

## Review-Time Routing

Use MCP selectively:

- **Manuscript reconstruction:** PDF/document and filesystem MCP for manuscript,
  methods, figures, supplements, tables, references, and code archives.
- **Claim extraction:** Rigorous Reviewer extracts claims; MCP only supplies
  parsed text, page/table provenance, or code/data artifacts.
- **Calibration anchors:** PubMed, Europe PMC, Crossref, Zotero, paper search,
  and public databases for gold, near-gold, negative, and boundary anchors.
- **Domain verification:** database MCP for accessions, compounds, structures,
  variants, clinical trials, materials, datasets, and public benchmark records.
- **Statistical/computational checks:** Python/R MCP only for transparent local
  recalculation, QC checks, benchmark scoring, or confidence-interval/sample-size
  checks.
- **Code and benchmark review:** GitHub/code MCP plus local benchmark,
  schema-lint, and golden-fixture tools.
- **Structured output:** local filesystem plus schema/benchmark tools; do not
  replace the Markdown review unless the user explicitly asks for JSON-only.
- **Venue and reporting standards:** web/search MCP for official public
  policies and checklists.

## K-Dense Companion Skills

Keep K-Dense as an optional skill-companion layer, not an MCP replacement. Use
K-Dense skills only for bounded paper lookup, database lookup, literature-review
strategy, scientific-critical-thinking cross-checks, or scholar-evaluation
sanity checks. Do not install or invoke a broad K-Dense peer-review skill as a
default reviewer because it overlaps with this skill's core judgment role.

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
