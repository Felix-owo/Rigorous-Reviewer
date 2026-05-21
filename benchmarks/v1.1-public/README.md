# Rigorous Reviewer Public-Source Benchmark v1.1

This benchmark track contains public-source case cards rather than private manuscripts or copyrighted full-text articles.

Each case is a short, paraphrased review scenario anchored to public standards, public controversies, or public reporting guidelines. It is intended to test whether the reviewer skill can identify classes of scientific-review failure modes, not to reproduce or republish original articles.

## Rules

- Do not include confidential manuscripts, unpublished user work, local paths, or credentials.
- Do not paste full copyrighted articles, abstracts, figures, or supplemental methods.
- Use short paraphrases and source metadata.
- Record expected findings in `expected_findings.json`.
- Record public source anchors in `sources.json`.

## Scoring

Run:

```bash
python rigorous-reviewer/scripts/score_benchmark_semantic.py --benchmark-root benchmarks/v1.1-public
```

To score model outputs, place one Markdown review output per case in a directory:

```text
outputs/
├── RR_PUBLIC_001_arsenic_life_claim.md
├── RR_PUBLIC_002_clinical_prediction_reporting.md
└── ...
```

Then run:

```bash
python rigorous-reviewer/scripts/score_benchmark_semantic.py \
  --benchmark-root benchmarks/v1.1-public \
  --outputs-dir outputs \
  --json
```
