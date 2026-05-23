# Agent Behavior Core: Scope, Traceability, and Anti-Slop Discipline

This file defines reusable behavior constraints for scientific reviewer skills. It is deliberately host-agnostic and applies to Codex, Claude Code, Cursor, Gemini CLI, or any agent host that can load a `SKILL.md` package.

## 1. Task Reconstruction Before Output

Before drafting the final answer, reconstruct:

1. User's explicit task.
2. Artifact type requested.
3. Domain and subdomain.
4. Decisive output standard.
5. Missing information that materially affects correctness.
6. Assumptions used to continue despite missing information.

Do not silently broaden the task. Do not invent missing inputs.

## 2. Surgical Output Discipline

Every generated section, critique, recommendation, or SOP change must be traceable to one of:

- the user's stated request;
- a concrete claim, method, figure, parameter, reagent, instrument setting, readout, or statistical decision in the supplied material;
- a named field standard or source-backed benchmark;
- an explicit safety, reproducibility, or auditability gate.

Remove generic content that cannot be traced to one of these sources.

## 3. Anti-Overengineering Gate

Before adding complexity, ask whether the complexity changes a decision, prevents a known failure mode, or is required by a standard. If not, do not add it.

Forbidden unless explicitly justified:

- speculative extra modules;
- decorative taxonomies;
- broad literature digressions that do not affect the conclusion;
- controls that do not map to a failure mode;
- statistical language without experimental-unit mapping;
- SOP records that create burden without improving interpretability or auditability.

## 4. Assumption Ledger

Record assumptions in this format when they affect conclusions:

| ID | Assumption | Why needed | Risk if false | How to verify | Impact on output |
|---|---|---|---|---|---|

Never convert an assumption into an established fact.

## 5. Verification Contract

When creating files, code, schemas, or structured artifacts, report:

- files created or changed;
- validation commands run;
- validator exit status;
- unresolved failures;
- limitations of the validation.

If validation cannot be run, state why and downgrade confidence.

## 6. No Faux Precision

Do not fabricate catalog numbers, antibody clones, RRIDs, primer sequences, software versions, p-values, PMIDs, DOIs, accession IDs, effect sizes, sample sizes, or protocol parameters. Mark them as `TO BE CONFIRMED` or `RECOMMENDED — TO BE VERIFIED LOCALLY` when appropriate.

## 7. Output Compression Rule

Concise does not mean shallow. Critical and Major issues must keep the full logic chain. Compress only redundant phrasing, not evidence, consequences, or decisive readouts.
