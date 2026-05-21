# Trigger Keywords and Routing Rules

This file provides explicit activation hints for agent hosts, installers, and maintainers. It supplements the `SKILL.md` `description` metadata; it does not replace the main skill instructions.

## Strong triggers

Use `rigorous-reviewer` when the user asks for top-journal-level scientific critique of a manuscript, preprint, proposal, figure set, dataset, proof, computational model, code artifact, or central scientific claim.

### English trigger phrases

- rigorous review
- scientific peer review
- manuscript review
- preprint review
- proposal review
- grant review
- referee report
- reviewer 2
- editorial recommendation
- top-journal review
- Nature / Cell / Science / CNS-level review
- journal-level estimate
- Accept / Minor Revision / Major Revision / Reject
- central claim
- decisive evidence
- evidence sufficiency
- evidence ledger
- alternative explanation
- hidden loophole
- critical flaw
- novelty claim
- overclaiming
- reproducibility audit
- methodological loophole
- statistical validity
- benchmark integrity
- artifact reproducibility
- clinical model validation
- external validation
- orthogonal validation
- causal claim
- mechanistic evidence
- proof review
- theorem review
- field evidence map
- gold-paper calibration

### Chinese trigger phrases

- 严格审稿
- 科学审稿
- 顶刊审稿
- CNS审稿
- Nature审稿
- Cell审稿
- Science审稿
- 论文审稿
- 预印本审稿
- 基金评审
- proposal审查
- 审稿意见
- 评审意见
- reviewer 2
- 期刊级别评估
- 能发什么期刊
- 顶刊水平
- 中心claim
- 中心结论
- 主要结论
- 决定性证据
- 证据是否充分
- 证据链
- 替代解释
- 隐藏漏洞
- 关键缺陷
- 致命缺陷
- Major revision
- Reject
- 新颖性
- 过度声称
- 机制证据
- 因果claim
- 统计有效性
- 可重复性
- benchmark有效性
- 代码可重复性
- 外部验证
- 正交验证
- 需要什么补实验
- 最小补实验包

## Weak contextual triggers

These terms should increase confidence only when paired with a scientific manuscript, proposal, dataset, model, figure, or claim:

- evaluate
- critique
- assess
- red flag
- fatal flaw
- journal fit
- novelty
- limitations
- evidence gap
- robustness
- reproducibility
- method critique
- statistics critique
- benchmark critique
- revision feasibility

## Negative routing

Do not trigger `rigorous-reviewer` by default for tasks that primarily ask for:

- biological protocol/SOP rewriting or bench workflow execution readiness
- pure language polishing
- Nature-style prose editing
- figure styling or visualization production
- slide generation or paper-to-PPT conversion
- citation formatting only
- literature/database lookup only
- code debugging only

Route these to the corresponding installed skill when available. Trigger `rigorous-reviewer` only if the user explicitly asks for scientific critique, evidence sufficiency, claim stress-testing, or final reviewer judgment.

## Routing precedence

1. If the task is about whether a scientific claim is true, novel, decisive, publishable, or reviewer-ready, use `rigorous-reviewer`.
2. If the task is about whether a wet-lab protocol or SOP can be executed and reproduced, route to `biological-protocol-reviewer`.
3. If the task is only about writing, polishing, figures, citations, slides, or response-letter drafting, route to a writing/production skill unless scientific critique is requested.
4. If the task is only about external lookup, use lookup/database companion skills first and reserve `rigorous-reviewer` for synthesis.
