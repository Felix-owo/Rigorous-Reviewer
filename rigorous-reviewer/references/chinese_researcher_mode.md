# Chinese Researcher Mode

Use when the user writes in Chinese or asks for Chinese author-facing review,
revision, or lab-meeting material.

## Output rules

- Reason at the same scientific standard as English output.
- Default to Chinese review text unless the user asks for journal-facing English.
- Keep standard technical terms in English when translation would reduce
  precision: gene/protein names, datasets, software, statistical models,
  antibodies, methods, theorems, benchmarks, and reporting standards.
- Do not translate literally if it weakens scientific precision.
- Keep unresolved author-input fields in Chinese when they are action items for
  the user's lab.
- If final journal-facing text is requested, separate English text from Chinese
  verification notes.

## Required issue labels in Chinese reports

Use these labels exactly for Critical, Major, and Minor issue blocks:

- `具体问题：`
- `为什么严重：` or `为什么重要：`
- `证据：`
- `影响：`
- `替代解释/漏洞：`
- `解决：`
- `决定性 readout：`
