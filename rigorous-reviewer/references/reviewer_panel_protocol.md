# Reviewer Panel Protocol

Use this protocol for every comprehensive review. It adds independent reviewer
perspectives without adding alternate review modes. The output remains one
integrated full-paper referee report.

## Core Rule

Run six independent role passes before the final synthesis:

1. **Editor-in-Chief (EIC):** journal-level significance, audience fit,
   conceptual advance, editorial risk, and decision logic.
2. **Methods / Statistics Reviewer:** design, causal inference, statistical
   validity, measurement, proof logic where relevant, benchmark integrity,
   reproducibility, and robustness.
3. **Domain Reviewer:** field-specific novelty, literature completeness,
   canonical methods, biological/chemical/physical/mathematical/clinical/CS
   plausibility, and missing anchors.
4. **Interdisciplinary Reviewer:** bridge claim validity, cross-domain
   assumptions, scale compatibility, translation between evidence standards, and
   fusion-field loopholes.
5. **Devil's Advocate:** strongest counter-argument, dominant alternative
   explanation, hidden false-positive path, cherry-picking risk, and the "so
   what?" test.
6. **Editorial Synthesizer:** integrates only the issues raised by the prior
   five role passes, resolves disagreements, ranks claim dependencies, and
   produces the final recommendation.

Do not require actual subagents. Run these as separated reasoning passes unless
the user explicitly asks for parallel agents.

## Independence Rules

- Each reviewer must first produce distinct concerns from its own role.
- Do not let the domain reviewer rewrite the methods reviewer.
- Do not let the EIC suppress technical flaws because the topic is exciting.
- Do not let the Devil's Advocate invent unsupported criticisms; it must still
  satisfy the evidence chain and citation rules.
- The synthesizer may merge duplicate issues, but must not fabricate issues not
  traceable to at least one reviewer pass.
- If the Devil's Advocate finds a Critical issue against the central claim, the
  final recommendation cannot be Accept unless the issue is explicitly resolved
  by manuscript-internal evidence and external support.

## Reviewer Pass Output

Each role pass should create concise internal notes:

```text
Role:
Primary lens:
Top 3 vulnerabilities:
Strongest supportive evidence:
Missing decisive evidence:
Critical/Major candidates:
Evidence or source needed:
```

Only surface the final consolidated report unless the user asks to see the panel
notes.

## Synthesis Rules

The Editorial Synthesizer must:

1. Identify where reviewers agree.
2. Identify real disagreements and state why one concern has priority.
3. Rank issues by claim dependency, not by reviewer seniority.
4. Convert role-specific concerns into the required issue logic chain.
5. Keep every Critical or Major issue traceable to:
   - manuscript-internal evidence,
   - at least one reviewer role,
   - external support or a named missing-evidence standard,
   - decisive readout.

## Panel Failure Conditions

The panel pass fails and must be rewritten if:

- all reviewers raise essentially the same issue,
- no reviewer names the central claim dependency,
- the Devil's Advocate only repeats generic skepticism,
- the EIC recommendation ignores unresolved Critical issues,
- the methods/statistics reviewer omits reproducibility or uncertainty,
- the interdisciplinary reviewer fails to name the bridge claim,
- the synthesizer adds claims absent from reviewer notes.
