# Rigorous Reviewer

[English](README.md)

[![License: MPL-2.0](https://img.shields.io/badge/License-MPL--2.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Standard-Agent_Skills-blueviolet.svg)](https://agentskills.io/specification)
[![Version](https://img.shields.io/badge/Version-v2.2.2-blue.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.10--3.12-3776AB.svg)](pyproject.toml)
[![Works with](https://img.shields.io/badge/Works_with-Codex_%7C_Claude_Code_%7C_Cursor-blue.svg)](docs/compatibility/agent_matrix.md)

`Rigorous Reviewer` 是一个可移植的 Agent Skill，用于顶刊级严格科学审稿。
它可以让兼容的 agent host 对 manuscript、proposal、preprint、图表、方法、
证明、数据集、代码 artifact、模型和跨学科科学主张进行系统审查。

Codex 是已验证的运行环境之一；可安装包 `rigorous-reviewer/` 也按公开
[Agent Skills](https://agentskills.io/specification) 包格式设计，便于其他兼容
agent host 安装。该 skill 支持 MCP-aware 工作流，但不捆绑、也不要求 MCP server。

## 包含内容

本仓库包含一个可安装的 skill 包 `rigorous-reviewer/`，以及用于发布、测试和
回归控制的工程资产。

- **顶刊级审稿工作流**：六角色 reviewer panel、claim dependency 分析、
  创新性校准、决定性证据门槛，以及 Accept / Minor Revision / Major Revision /
  Reject 推荐逻辑。
- **六大领域覆盖**：生物、化学、物理、数学、医学、计算机科学 / AI，以及
  生物信息学、化学生物学、生物物理、医学 AI、计算化学、材料 AI、
  physics-informed machine learning 等融合方向。
- **专业审稿意见块**：每条实质性意见必须包含具体问题、为什么严重、稿件内部
  证据、外部支持、影响、替代解释/漏洞、解决方案和决定性 readout。
- **渐进式资源组织**：精简 `SKILL.md` 入口，配套 `references/`、`templates/`、
  `schemas/`、`scripts/`、`examples/` 和 `agents/`。
- **MCP-backed skill policy**：宿主提供 MCP 时，可用于检索、解析、计算、
  source verification 和验证；最终审稿判断仍由 skill 完成。
- **可选 companion-skill bridge**：可与 K-Dense、Life Science Research、
  bioinformatics、simulation、software-engineering、writing/output 和 design
  companion 协作，作为边界清晰的证据检索、校准、验证或输出转换支持。
- **验证套件**：installability smoke test、trigger keyword checker、Markdown
  validator、structured JSON linter、golden fixtures、unit tests、合成 benchmark
  和公开来源 semantic-lite benchmark。
- **安全与贡献文档**：明确私人数据边界、benchmark 内容规则和 release 检查清单。

每个 release 都应保留：

- `SKILL.md` 和有效 Agent Skills frontmatter
- `references/` 中的领域标准和审稿协议
- `templates/` 中的 issue block、search hints 和 Markdown 报告模板
- `scripts/` 与 `schemas/` 中的确定性校验工具
- `examples/` 中的输出形态示例
- `agents/openai.yaml` 中的 host-facing metadata

## 目录

- [包含内容](#包含内容)
- [为什么使用它](#为什么使用它)
- [快速开始](#快速开始)
- [安全提示](#安全提示)
- [前置要求](#前置要求)
- [快速示例](#快速示例)
- [适用场景](#适用场景)
- [Skill 包结构](#skill-包结构)
- [MCP 与 Companion Skills](#mcp-与-companion-skills)
- [验证与 Benchmarks](#验证与-benchmarks)
- [贡献](#贡献)
- [故障排查](#故障排查)
- [FAQ](#faq)
- [引用](#引用)
- [证据基础与致谢](#证据基础与致谢)
- [许可证](#许可证)

## 为什么使用它

### 更强的科学审稿深度

- **默认完整审查**：不是 quick review、partial review 或普通写作反馈。
- **决定性 readout**：每个关键批评都必须定义什么结果能够真正改变结论。
- **Panel synthesis**：EIC、方法/统计 reviewer、领域 reviewer、跨学科 reviewer、
  Devil's Advocate 和 editorial synthesizer 独立给出意见后再合成。

### 更广的领域覆盖

- **实验科学**：controls、perturbation/rescue、orthogonal validation、表征、
  calibration、uncertainty 和 reproducibility。
- **数学与理论**：假设、证明完整性、边界情况、反例、前置结果依赖和 sharpness。
- **计算机科学与 AI**：benchmark integrity、data leakage、baselines、ablation、
  statistical testing、complexity、security 和 artifact reproducibility。
- **临床与转化研究**：endpoint、bias、external validation、calibration、安全性、
  ethics 和 reporting guideline fit。

### 可维护、可回归测试

- **Installability checks** 防止可安装 skill 缺文件。
- **Schema 与 Markdown validators** 保证输出可审计。
- **Golden fixtures 与 benchmarks** 检测行为漂移。
- **CI-ready scripts** 默认本地确定性运行，不依赖外部服务。

### 可移植集成

- **Agent Skills 包格式**：`rigorous-reviewer/` 是完整自包含目录。
- **触发路由**：中英文 trigger keywords 支持 `top-journal review`、`reviewer 2`、
  `顶刊审稿`、`决定性证据` 等请求。
- **MCP-aware 但不依赖 MCP**：有 MCP 时调用工具增强；无 MCP 时仍可完整审稿。

## 快速开始

### 方式 1：Codex 对话式安装

在 Codex 中输入：

```text
Use $skill-installer to install https://github.com/Felix-owo/Rigorous-Reviewer/tree/v2.2.2/rigorous-reviewer
```

安装后重启 Codex，让 skill metadata 重新加载。

### 方式 2：命令行安装

```bash
python "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --url https://github.com/Felix-owo/Rigorous-Reviewer/tree/v2.2.2/rigorous-reviewer
```

安装后重启 agent host。

### 方式 3：手动复制

将完整 `rigorous-reviewer/` 目录复制到目标 host 的 skill 目录。不要只复制
`SKILL.md`，否则 references、templates、schemas、scripts、examples 和
`agents/openai.yaml` 会丢失。

验证复制后的目录：

```bash
python rigorous-reviewer/scripts/check_installable_skill.py --skill-dir rigorous-reviewer
```

### 方式 4：其他 Agent Skills installer

如果你的 host 支持 `npx skills add`、`gh skill` 或其他 Agent Skills installer，
请按该 host 文档指向本仓库或 `rigorous-reviewer/` 子目录。当前已验证的 fallback
是 Codex `$skill-installer` 或手动复制。

### 版本固定

使用 release tag `v2.2.2` 可获得可复现安装。只有在明确想安装未发布修改时才使用
`main`：

```text
Use $skill-installer to install https://github.com/Felix-owo/Rigorous-Reviewer/tree/main/rigorous-reviewer
```

## 安全提示

> Skills 会影响 agent 行为，并可能指示 agent 读文件、运行脚本、查询服务或调用
> host tools。安装前应审查其内容。

科学审稿经常涉及未发表 manuscript、私人数据、保密附件、本地路径和 embargoed
results。本仓库按 local-first 方式设计，但仍需要遵守以下规则：

- 不要提交私人 manuscript、未发表用户数据、本地路径、credentials 或 copyrighted
  full-text papers。
- 向联网 MCP 或第三方 MCP 发送保密 manuscript、私人附件、本地路径或未发表数据前，
  必须先获得用户明确授权。
- MCP 输出只能作为 evidence input，不能替代最终审稿判断。
- benchmark 和 validation scripts 默认本地运行。
- 安装或修改前阅读 `SECURITY.md`。

## 前置要求

- **Agent host**：Codex 或其他支持 Agent Skills 的运行环境。
- **Python**：3.10、3.11 或 3.12，用于本地 validators 和 benchmark scripts。
- **网络**：核心验证不需要网络；文献、数据库、DOI 或 web check 可选依赖网络。
- **MCP**：可选；本仓库不捆绑也不要求 MCP server。
- **Companion skills**：可选；K-Dense skills 可单独安装作为检索和校准助手。

可选开发依赖：

```bash
python -m pip install -r requirements-dev.txt
```

## 快速示例

### 全文 manuscript 审稿

```text
Use $rigorous-reviewer to review this manuscript at Nature/Cell/Science level.
Focus on novelty, central claim dependency, decisive evidence gaps, hidden
alternative explanations, and the minimum revision package needed for a stronger
editorial decision.
```

### AI benchmark 审查

```text
Use $rigorous-reviewer to review this AI paper. Check benchmark validity,
train-test leakage, baseline strength, ablations, statistical testing, compute
budget, code/data availability, and whether the claimed clinical or scientific
impact is supported.
```

### 数学证明审查

```text
Use $rigorous-reviewer to review this theorem and proof. Identify every
dependency on prior results, boundary condition, missing lemma, possible
counterexample family, and the minimum proof repair needed before publication.
```

### 医学 AI 审查

```text
Use $rigorous-reviewer to review this medical AI manuscript. Check cohort
selection, leakage, endpoint definition, calibration, external validation,
decision-curve utility, safety, reporting guideline fit, and unsupported
clinical deployment claims.
```

### 跨学科 claim 审查

```text
Use $rigorous-reviewer to review this chemical biology manuscript. Separate
compound identity and target engagement evidence from biological mechanism
claims, and define decisive readouts for each bridge claim.
```

## 适用场景

### 生物与组学

机制论文、perturbation/rescue、lineage tracing、single-cell analysis、spatial
omics、CRISPR screens、trajectory inference 和 sample provenance reproducibility。

### 化学与材料

合成方法、催化、结构表征、纯度、谱学、target engagement、kinetics、计算化学、
材料性质主张和稳定性 controls。

### 物理

实验 calibration、uncertainty、systematic error、regime validity、simulation
convergence、dimensional consistency 和 independent observables。

### 数学

定理创新性、假设、证明完整性、边界情况、反例、前置结果依赖和 sharpness examples。

### 医学与临床 AI

临床试验、观察性研究、诊断/预后模型、外部验证、calibration/discrimination、
安全性、ethics 和 reporting standards。

### 计算机科学与 AI

算法、系统论文、ML benchmarks、leakage、baseline fairness、ablation、complexity、
code artifacts、reproducibility 和 security/failure modes。

### 融合学科

生物信息学、计算生物学、化学生物学、生物物理、医学 AI、计算化学、材料 AI、
数学 biology 和 physics-informed machine learning。

## Skill 包结构

可安装包是 `rigorous-reviewer/` 目录。

```text
rigorous-reviewer/
├── agents/
│   └── openai.yaml
├── examples/
│   ├── full_review_example.md
│   └── issue_block_examples.md
├── SKILL.md
├── references/
│   ├── six_domain_review_standards.md
│   ├── reviewer_rigor_contract.md
│   ├── reviewer_panel_protocol.md
│   ├── calibration_protocol.md
│   ├── failure_mode_playbook.md
│   ├── external_scientific_skills_bridge.md
│   ├── mcp_tool_use_policy.md
│   ├── trigger_keywords.md
│   ├── article_specific_literature_mapping.md
│   ├── cns_reviewer_requirements.md
│   ├── reviewer_output_standards.md
│   └── rubric.json
├── scripts/
│   ├── validate_review_report.py
│   ├── lint_structured_review.py
│   ├── score_benchmark.py
│   ├── score_benchmark_semantic.py
│   ├── check_installable_skill.py
│   └── apply_trigger_keywords.py
├── schemas/
│   ├── review_report.schema.json
│   ├── issue.schema.json
│   ├── evidence_ledger.schema.json
│   ├── external_companion_evidence.schema.json
│   ├── trigger_keywords.schema.json
│   └── score.schema.json
└── templates/
    ├── comment_templates.json
    ├── review_report_template.md
    ├── trigger_keywords.json
    └── search_hints.json
```

仓库级验证资产位于可安装包外：

```text
.github/workflows/validate.yml
tests/
benchmarks/v1.0/
benchmarks/v1.1-public/
docs/
├── README.md
├── compatibility/
│   └── agent_matrix.md
└── routing/
    └── trigger_keyword_support.md
SECURITY.md
CONTRIBUTING.md
CHANGELOG.md
```

## MCP 与 Companion Skills

### MCP-backed，而不是 Skill-as-MCP

`rigorous-reviewer` 仍是主审稿逻辑。MCP tools 只是可选 evidence-gathering helpers。

当 host 暴露以下能力时，按 `references/mcp_tool_use_policy.md` 使用：

- PDF/document parsing
- PubMed、Europe PMC、Crossref、DOI 或 web search
- Zotero 或 citation-library access
- Python/R computation
- public scientific database lookup
- filesystem/document handling
- GitHub/code artifact inspection
- benchmark 或 schema validation

MCP 结果必须带 provenance，且不能替代最终 Markdown review、evidence ledger、
issue-block logic 或 editorial recommendation。

### 可选 companion ecosystem

Rigorous Reviewer 可以在当前 host 已暴露相关能力时使用外部 skills、官方插件、
MCP tools 或 host-provided capabilities。这些 companion 只提供证据、验证、
分析或输出转换支持，永远不能替代最终 reviewer judgment。

推荐 companion：

- ChatGPT Life Science Research：公共 life-science database evidence。
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)：
  paper/database/literature lookup 和 critical-thinking cross-checks。
- GPTomics/bioSkills：omics 与 bioinformatics workflow cross-checks。
- HeshamFS/materials-simulation-skills：simulation、numerical、convergence 和
  HPC reproducibility support。
- Yuan1z0825/nature-skills：scientific review 完成后的 rebuttal、paper polishing、
  citation、figure 和 paper-to-PPT。
- guizang-ppt-skill / open-design / taste-skill：结论固定后的 slide deck、
  visual summary 或 design output。
- [mattpocock/skills](https://github.com/mattpocock/skills)：相关 code artifact、
  test strategy、debugging 和 engineering handoff support。

具体调用、隐私、provenance 和冲突规则见
`references/external_scientific_skills_bridge.md`。K-Dense companion 可单独安装：

```text
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/paper-lookup
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/database-lookup
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/literature-review
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/scientific-critical-thinking
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/scholar-evaluation
```

不要把 companion 代码 vendored 到本仓库；companion skills 应单独安装，并遵守其原始许可证。

## 验证与 Benchmarks

发布前运行完整本地验证链：

```bash
python -m py_compile rigorous-reviewer/scripts/*.py
python rigorous-reviewer/scripts/check_installable_skill.py --skill-dir rigorous-reviewer
python rigorous-reviewer/scripts/apply_trigger_keywords.py --skill-md rigorous-reviewer/SKILL.md --check
python rigorous-reviewer/scripts/validate_review_report.py tests/fixtures/markdown/valid_review.md --strict
python rigorous-reviewer/scripts/validate_review_report.py rigorous-reviewer/examples/full_review_example.md
python rigorous-reviewer/scripts/lint_structured_review.py tests/fixtures/json/valid_structured_review.json --strict
python rigorous-reviewer/scripts/score_benchmark.py --benchmark-root benchmarks/v1.0
python rigorous-reviewer/scripts/score_benchmark_semantic.py --benchmark-root benchmarks/v1.1-public
python -m unittest discover -s tests
```

Benchmark tracks：

- `benchmarks/v1.0/`：合成 benchmark definitions，用于核心审稿 failure modes。
- `benchmarks/v1.1-public/`：公开来源 case cards、source metadata 和短 paraphrases；
  不包含私人 manuscript 或 copyrighted full-text。

CI 在 Python 3.10、3.11 和 3.12 上运行同类检查。

## 贡献

贡献应让该 skill 成为更严格、可审计的科学审稿人，而不是泛化写作助手。

规则：

1. 保持任务边界：本 skill 审查 scientific claims，不变成 protocol rewriting、
   copyediting 或 figure styling skill。
2. 遵守 Agent Skills specification 的 `SKILL.md` metadata、包结构和渐进式加载原则。
3. 不把私人 manuscript、未发表用户数据、本地路径、credentials 或 copyrighted
   full-text papers 放进 tests 或 benchmarks。
4. 行为改变时，同步 validators、fixtures、benchmark expectations 和文档。
5. PR 前运行完整 validation chain。

详见 `CONTRIBUTING.md`。

## 故障排查

### Skill 没有触发

- 确认可安装目录名是 `rigorous-reviewer`。
- 确认 `rigorous-reviewer/SKILL.md` 存在且 frontmatter 有效。
- 安装后重启 agent host。
- 显式写：`Use $rigorous-reviewer ...`。
- 查看 `references/trigger_keywords.md` 和 `templates/trigger_keywords.json`。

### Installable package 检查失败

- 运行 `python rigorous-reviewer/scripts/check_installable_skill.py --skill-dir rigorous-reviewer`。
- 确认 `references/`、`templates/`、`schemas/`、`scripts/`、`examples/` 和
  `agents/` 文件完整。
- 不要只安装 `SKILL.md`；复制完整目录。

### 输出太浅

- 明确要求 full `rigorous-reviewer` report，并尽量提供 title、abstract、
  central claims、figures/tables、methods、data/code availability、target journal
  和 supplements。
- 预期 issue-block 深度见 `references/reviewer_rigor_contract.md`、
  `references/reviewer_output_standards.md` 和 `examples/full_review_example.md`。

### MCP tools 不可用

MCP 是可选能力。无 MCP 时，skill 应继续使用内置 reviewer protocol、search hints、
calibration rules、examples、schemas 和 validators。

### Companion skills 不可用

K-Dense companion skills 是可选增强。未安装时，`rigorous-reviewer` 会回退到内置
calibration、search hints 和 red-line audit。

## FAQ

**Q: 这只适用于生物领域吗？**

A: 不是。它覆盖生物、化学、物理、数学、医学、计算机科学 / AI 和融合学科。

**Q: 它会安装或要求 MCP server 吗？**

A: 不会。它是 MCP-aware skill，不是 MCP server。MCP 由 host 提供且完全可选。

**Q: 能输出 Markdown 审稿文档吗？**

A: 可以。默认在对话中输出 Markdown。只有用户要求文件、文档、archive 或 export 时，
才创建本地 `.md` 报告。

**Q: 能输出结构化 JSON 吗？**

A: 可以。机器可读审稿输出应使用 `schemas/review_report.schema.json` 和
`scripts/lint_structured_review.py` 校验。

**Q: 它能替代真实专家 peer review 吗？**

A: 不能。它用于结构化 critique、evidence mapping 和 failure-mode discovery；
最终科学与编辑决策仍应由人类专家负责。

## 引用

如在科研工作流中使用，请引用仓库和版本。

### BibTeX

```bibtex
@software{rigorous_reviewer_2026,
  author = {{Felix-owo}},
  title = {Rigorous Reviewer: A Portable Agent Skill for Scientific Peer Review},
  year = {2026},
  version = {2.2.2},
  url = {https://github.com/Felix-owo/Rigorous-Reviewer}
}
```

### Plain text

```text
Rigorous Reviewer v2.2.2. A portable Agent Skill for scientific peer review.
https://github.com/Felix-owo/Rigorous-Reviewer
```

## 证据基础与致谢

审稿标准参考了
[Nature peer-review criteria](https://www.nature.com/nature/editorial-policies/peer-review)、
[Nature Portfolio reporting standards](https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards)、
[ACS research data guidance](https://researcher-resources.acs.org/publish/data_guidelines)、
[ACM artifact review and badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current)、
[AMS Mathematical Reviews reviewer guidance](https://mathscinet.ams.org/mresubs/guide-reviewers.html)、
[CONSORT](https://pubmed.ncbi.nlm.nih.gov/20346629/)、
[PRISMA](https://www.prisma-statement.org/prisma-2020)、
[STROBE](https://www.strobe-statement.org/fileadmin/Strobe/uploads/checklists/STROBE_checklist_v4_combined.pdf)、
[ARRIVE](https://arriveguidelines.org/arrive-guidelines)、
[SPIRIT](https://www.spirit-statement.org/spirit-statement/) 和
[TRIPOD](https://www.bmj.com/content/350/bmj.g7594)。

README 信息架构参考
[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)：
overview、contents、table of contents、rationale、installation、security、
prerequisites、examples、use cases、package inventory、contribution guidance、
troubleshooting、FAQ、citation 和 license。

包设计遵循公开
[Agent Skills specification](https://agentskills.io/specification)，包括 `SKILL.md`
frontmatter、可选 `scripts/`、`references/`、`assets/` 目录和 progressive
disclosure。可选工具路由政策参考公开
[Model Context Protocol specification](https://modelcontextprotocol.io/specification/2025-06-18)，
其定义了 MCP resources、prompts、tools，以及 consent、privacy 和 tool safety
相关原则。

本仓库还参考了以下公开 skill 仓库作为比较设计来源：

- [mattpocock/skills](https://github.com/mattpocock/skills)
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
- [tanweai/pua](https://github.com/tanweai/pua)
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

本仓库不复制第三方 skill 代码。外部仓库保持其原许可证。

## 许可证

MPL-2.0。见 `LICENSE`。
