# Rigorous Reviewer Benchmark Leaderboard

This file records benchmark definition validity and, when available, scored model outputs across releases.

| Version | Benchmark track | Definition validation | Model outputs scored | Mean score | Pass rate | Notes |
|---|---|---:|---:|---:|---:|---|
| v1.9.0 | v1.0-synthetic | PASS | No | N/A | N/A | Introduced synthetic benchmark definitions and schema-backed validation. |
| v2.0.0 | v1.1-public | PASS | No | N/A | N/A | Adds public-source case cards, trigger routing, installable smoke checks, MCP tool-use policy, and semantic-lite scoring. |
| v2.0.1 | v1.1-public | PASS | No | N/A | N/A | Quality patch for portable trigger checks, bilingual validation, strict JSON linting, reduced activation load, and safer placeholder detection. |
| v2.0.2 | v1.1-public | PASS | No | N/A | N/A | CI portability patch for the absolute-path trigger registry regression test. |
| v2.1.0 | v1.1-public | PASS | No | N/A | N/A | Adds optional companion capability bridge expansion, external companion evidence schema/linting, and companion-aware trigger routing. |
| v2.1.3 | v1.1-public | PASS | No | N/A | N/A | Adds package compliance checks, version consistency validation, and bundled regression fixtures. |

## How to update

1. Generate one model output per benchmark case.
2. Save outputs as `outputs/<case_id>.md`.
3. Run:

```bash
python rigorous-reviewer/scripts/score_benchmark_semantic.py \
  --benchmark-root benchmarks/v1.1-public \
  --outputs-dir outputs \
  --json > benchmarks/results/v2.1.3_public_outputs.json
```

4. Compute mean score and pass rate from the JSON.
5. Update this leaderboard and `benchmark_results.json`.

Do not commit private manuscripts, unpublished outputs containing confidential data, local file paths, or full copyrighted papers.
