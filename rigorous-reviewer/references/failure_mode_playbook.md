# Failure-Mode Playbook

Use this playbook as a final self-audit before returning any review. If a red
line triggers, rewrite the affected section before final output.

## Red Lines

1. **Citation-free finding**
   - Signal: a Critical or Major issue relies on field knowledge but has no
     external source.
   - Rewrite: add a primary paper, guideline, benchmark, theorem source,
     standard, dataset, protocol, trial record, repository, or downgrade to a
     question.

2. **Generic control request**
   - Signal: wording such as "more controls are needed" without naming the exact
     control and interpretation change.
   - Rewrite: name the missing positive/negative control, baseline, perturbation,
     rescue, null test, validation cohort, benchmark, proof repair, or
     characterization.

3. **Repeated criticism**
   - Signal: multiple issues make the same point with different wording.
   - Rewrite: merge duplicates, then separate distinct mechanisms only if each
     has a different evidence basis, impact, and decisive readout.

4. **No decisive readout**
   - Signal: an issue asks for work but does not define what outcome would
     support versus weaken the claim.
   - Rewrite: add support/refute readouts and the claim-narrowing consequence.

5. **No manuscript-internal evidence**
   - Signal: the issue does not point to a figure, table, method, proof step,
     quoted claim, data source, code artifact, benchmark, cohort, or stated
     omission.
   - Rewrite: identify the exact manuscript location or state that the required
     evidence is absent.

6. **No search hint for a weak evidence link**
   - Signal: a central uncertainty is unresolved, but the search hints do not
     map to it.
   - Rewrite: add a targeted search task with preferred source type, 2-4 queries,
     decision-changing evidence, and linked issue.

7. **Uncalibrated severity**
   - Signal: recommendation severity is not tied to claim dependency, comparable
     literature, field standards, or gold/cautionary anchors.
   - Rewrite: add calibration context or explicitly state that suitable anchors
     could not be found.

8. **Devil's Advocate omitted**
   - Signal: the review does not include the strongest counter-argument or
     dominant false-positive route.
   - Rewrite: run the Devil's Advocate pass and integrate any supported issue.

9. **Synthesis fabrication**
   - Signal: final recommendation includes a reason not traceable to a reviewer
     pass, manuscript evidence, or external source.
   - Rewrite: remove it or trace it properly.

10. **Evidence-action mismatch**
    - Signal: a requested revision is not necessary for the stated conclusion.
    - Rewrite: move it from essential to optional, or explain why the main claim
      depends on it.

11. **Terse or incomplete issue block**
    - Signal: an issue is a short bullet, lacks the professional reviewer anatomy,
      or omits any of: specific problem, seriousness/importance, manuscript
      evidence, external evidence or search target, impact, loophole, resolution,
      or decisive readout.
    - Rewrite: expand it into a complete issue block. In Chinese reports, use
      the labels `具体问题：`, `为什么严重：` or `为什么重要：`, `证据：`, `影响：`,
      `替代解释/漏洞：`, `解决：`, and `决定性 readout：`.

12. **Missing evidence ledger**
    - Signal: a full review has citations or source claims but no table mapping
      sources to issues, revision actions, calibration anchors, or recommendation.
    - Rewrite: add an Evidence Ledger with manuscript-internal and external
      sources, decision roles, and identifiers/links.

13. **Markdown/report validation failure**
    - Signal: a saved `.md` report fails `scripts/validate_review_report.py`, or
      the chat report lacks Markdown headings and issue blocks.
    - Rewrite: fix the missing headings, issue labels, evidence split, decisive
      readouts, or evidence ledger before returning the report.

## Final Red-Line Checklist

Before final output, verify:

```text
[ ] Every Critical/Major issue has manuscript-internal evidence.
[ ] Every Critical/Major issue has external support or is framed as missing evidence.
[ ] Every Critical/Major issue is a complete professional issue block, not a terse bullet.
[ ] Chinese issue blocks use the required labels: 具体问题, 为什么严重/为什么重要, 证据, 影响, 替代解释/漏洞, 解决, 决定性 readout.
[ ] Every issue has a decisive readout.
[ ] No issue is generic or duplicated.
[ ] Search hints map to the weakest evidence links.
[ ] Full reviews include an Evidence Ledger mapping sources to issues/actions.
[ ] Saved Markdown reports pass scripts/validate_review_report.py.
[ ] Panel synthesis is traceable to reviewer passes.
[ ] Calibration is numeric only when labeled anchors support it.
[ ] Overall recommendation follows unresolved claim dependency.
```
