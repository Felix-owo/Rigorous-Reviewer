# Issue Traceability and Scope Discipline

Every issue must have a traceable anchor:

| Issue anchor | Examples |
|---|---|
| Claim | “X causes Y”, “method improves benchmark Z” |
| Figure/table/panel | Fig. 2c, Extended Data Fig. 5, Table 1 |
| Method | sample prep, perturbation, model training, proof lemma |
| Dataset/code | accession, repository, split, baseline, preprocessing |
| Statistic/proof | experimental unit, model, correction, theorem dependency |
| Standard | ARRIVE, CONSORT, MIQE, FAIR, benchmark protocol, field convention |

Forbidden issue types:

- vague “add more controls” comments;
- style complaints framed as scientific fatal flaws;
- literature wish lists without decision impact;
- speculative experiments not tied to an alternative explanation;
- criticism of absent goals the manuscript never claimed.

Each issue must include a `Decision impact` field: Critical, Major, Minor, or None.
