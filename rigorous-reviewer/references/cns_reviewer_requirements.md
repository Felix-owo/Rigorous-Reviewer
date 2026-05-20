# Elite-Journal-Calibrated Reviewer Requirements

Use this reference to define the reviewer role before judging any scholarly
manuscript, proposal, figure set, dataset, code artifact, source argument, or
preliminary result. The filename is retained for compatibility with the original
biology-focused skill, but the requirements now apply to biology, chemistry,
physics, mathematics, medicine, computer science, and fusion fields.

## Contents

- Source Anchors
- Role Routing
- Review Structure
- Decision Calibration
- Red Flags for Unacceptable Review Quality

## Source Anchors

Use these sources as calibration anchors for rigorous review:

- **Nature peer review and editorial criteria:** reviewers should assess validity,
  originality, significance, data, methodology, statistics, robustness of
  conclusions, references, clarity, and context.
  https://www.nature.com/nature/editorial-policies/peer-review
  https://www.nature.com/nature/for-authors/editorial-criteria-and-processes
- **Cell reviewer/editor guidance:** high-quality reviews identify the main
  take-home message, judge close technical details and broader conceptual
  significance, and avoid undeclared conflicts, unrealistic expectations, and
  moving goalposts. https://crosstalk.cell.com/blog/how-does-cell-select-reviewers
  https://doi.org/10.1016/j.cell.2019.08.044
- **Science/AAAS publication policies:** materials, methods, and data needed to
  verify conclusions should be available when possible, and expert review should
  protect validity and reproducibility.
  https://www.science.org/content/page/science-journals-editorial-policies
- **COPE ethical guidance for peer reviewers:** peer review should be fair,
  confidential, evidence-based, timely, and free of conflicts of interest.
  https://publicationethics.org/resources/guidelines-new/cope-ethical-guidelines-peer-reviewers
- **Reporting and transparency standards:** choose field-appropriate standards,
  such as CONSORT for randomized trials, PRISMA for systematic reviews, STROBE
  for observational studies, ARRIVE for animal research, TRIPOD for prediction
  models, APA JARS for quantitative/qualitative reports, ACM artifact review
  badges for computational artifacts, and TOP Guidelines for transparency.
- **Six-domain specialist standards:** use Nature reporting standards for data,
  materials, code, and protocols; ACS research data and characterization guidance
  for chemistry; AMS/MathSciNet reviewer guidance for mathematical errors and
  proof description; ACM/IEEE/NeurIPS/ICLR reproducibility and artifact standards
  for computer science; and EQUATOR-linked reporting guidelines for medicine.

## Role Routing

Use `reviewer_panel_protocol.md` as the canonical six-role procedure. This file
does not duplicate those roles. Instead, use the source anchors above to
calibrate whether the final synthesis meets elite-journal expectations for:

- technical validity and decisive evidence,
- conceptual advance and broad relevance,
- methods, statistics, source, data, code, and reproducibility transparency,
- article-specific literature and benchmark awareness,
- fair, feasible, non-moving-goalpost revision requests.

## Review Structure

Use this mental structure even if the final output differs:

1. **Take-home message:** what the authors want the field to believe.
2. **Evidence dependency:** which evidence must be true for that message to survive.
3. **Technical validity:** whether the decisive evidence is internally sound.
4. **Alternative explanations:** strongest false-positive, confounding, or
   competing interpretation.
5. **Conceptual advance:** what changes relative to strongest prior work.
6. **Essential revisions:** smallest revision package needed to support or narrow
   the take-home message.
7. **Decision logic:** acceptable, revisable, or fundamentally under-supported.

## Decision Calibration

- **Accept / very favorable:** no central technical or interpretive weakness
  remains; the take-home message is strongly supported and advances the field.
- **Minor Revision:** the main conclusion is already supported; remaining requests
  concern clarity, reporting, citations, or bounded non-decisive checks.
- **Major Revision:** promising but one or more central claims require additional
  analyses, controls, validation, source support, proof repair, or explicit
  narrowing within current scope.
- **Reject:** the central claim is unsupported, decisive evidence would require a
  fundamentally different study, dominant alternatives cannot be excluded, or the
  claimed advance is not established even if parts are technically valid.

## Red Flags for Unacceptable Review Quality

Do not produce reviews that:

- Give a recommendation without explaining evidence dependency.
- Ask for "more controls" without naming the exact control, benchmark, source, or
  decisive readout.
- Treat editorial fit or personal taste as a technical flaw.
- Dismiss novelty without citing prior work.
- Overlook supplementary data, appendices, code, sources, or methods that bear on
  the claim.
- Ignore uncertainty, confounding, batch effects, sampling, source bias,
  reproducibility, or data leakage.
- Confuse feasibility, plausibility, or interpretation with proof.
- Suggest broad new projects unrelated to the central conclusion.
- Include confidential/editor-only concerns in comments to authors.
- Rely on unsourced field impressions where evidence is available.
