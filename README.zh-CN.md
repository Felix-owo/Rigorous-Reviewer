# Rigorous Reviewer Codex Skill 中文说明

这个仓库包含一个面向 Codex 的顶刊级科学审稿 skill：
`rigorous-reviewer`。

它重点覆盖六大领域：

- 生物
- 化学
- 物理
- 数学
- 医学
- 计算机科学 / AI

它也特别强化交叉学科和融合学科审稿能力，例如生物信息学、计算生物学、
化学生物学、药物化学、生物物理、医学 AI、计算化学、材料 AI、数学
生物学和 physics-informed machine learning。

## 功能概览

`rigorous-reviewer` 用于严格审查论文、proposal、preprint、图表、
方法、证明、数据集、代码、临床模型、算法和跨学科主张。

它重点支持：

- 顶刊级创新性和概念推进判断
- 六视角 reviewer-panel 综合审稿
- 基于 gold、near-gold、negative 和 boundary papers 的校准
- 可选桥接 K-Dense Scientific Agent Skills，用于论文检索、数据库核验、
  文献综述和 scientific critical thinking
- 按领域设定决定性证据门槛
- 隐藏漏洞、替代解释和 false-positive 模型查找
- 专业审稿意见块：每条意见必须写清楚具体问题、为什么严重/重要、证据、影响、
  替代解释/漏洞、解决方案和决定性 readout
- Markdown 审稿报告输出：当用户要求保存文档时，生成带 evidence ledger 的
  `.md` 报告并可执行结构校验
- 当用户需要机器可读输出时，支持基于 schema 的结构化 JSON 校验
- 增加 unit tests、golden fixtures、CI 和合成 versioned benchmark set，用于
  防止回归和行为漂移
- 针对无 citation、泛泛 controls、重复批评、无 decisive readout 等问题的红线检查
- `Critical` / `Major` / `Minor` 问题分级
- 针对具体稿件建立 field evidence map
- 可重复性、可审计性和数据/代码/材料透明度审查
- 针对不同学科检查实验控制、数学证明、化学表征、物理测量、临床验证、
  算法基准和代码/数据 artifact

## 在 Codex 中安装

### 对话式安装

安装稳定版，在 Codex 中输入：

```text
Use $skill-installer to install https://github.com/Felix-owo/Rigorous-Reviewer/tree/v1.8.0/rigorous-reviewer
```

如果你想安装 `main` 分支上的最新开发版，则输入：

```text
Use $skill-installer to install https://github.com/Felix-owo/Rigorous-Reviewer/tree/main/rigorous-reviewer
```

安装完成后，重启 Codex 以加载新 skill。

### 命令行安装

如果你希望直接通过命令运行已安装的 skill-installer helper：

```bash
python "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --url https://github.com/Felix-owo/Rigorous-Reviewer/tree/v1.8.0/rigorous-reviewer
```

执行后重启 Codex。

只有在你想安装未发布的最新开发版时，才使用 `main` 分支 URL。

### 关于 slash command

有些 Codex 客户端可能提供 `/` 形式的命令启动器。这个仓库本身不定义自定义
`/install` 命令；如果你的客户端支持 slash command，可以打开命令启动器并输入
上面的 `$skill-installer` 安装请求。确定可用的安装方式是 `$skill-installer`
或它的 helper 脚本。

## 适用场景

这个 skill 适合用于：

- 生物机制、细胞/动物实验、组学和谱系推断审稿
- 化学合成、催化、材料、结构表征和化学生物学审稿
- 物理实验、理论、模拟、测量不确定性和系统误差审稿
- 数学定理、证明、假设、边界情况和反例审稿
- 医学临床试验、观察性研究、诊断/预后模型、系统综述和医学 AI 审稿
- 计算机科学、AI/机器学习、系统、算法、benchmark 和 reproducibility 审稿
- 跨学科研究中的领域接口验证，例如模型是否真的支持生物/化学/临床结论

## 仓库结构

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
│   ├── article_specific_literature_mapping.md
│   ├── cns_reviewer_requirements.md
│   ├── reviewer_output_standards.md
│   └── rubric.json
├── scripts/
│   ├── validate_review_report.py
│   ├── lint_structured_review.py
│   └── score_benchmark.py
├── schemas/
│   ├── review_report.schema.json
│   ├── issue.schema.json
│   ├── evidence_ledger.schema.json
│   └── score.schema.json
└── templates/
    ├── comment_templates.json
    ├── review_report_template.md
    └── search_hints.json
```

仓库级工程检查位于可安装 skill 文件夹外：

```text
.github/workflows/validate.yml
tests/
benchmarks/v1.0/
```

benchmark cases 全部是合成材料，不应包含真实 manuscript、附件、本地路径或用户
私人研究材料。

`references/` 和 `templates/` 是 skill 的必要组成部分，安装或分享时应与
`SKILL.md` 一起保留。

这个 skill 默认执行完整全文审查，不新增 quick-review、partial-review 或
re-review 模式。skill 目录内只保留对 agent 审稿流程直接有用的资源。

Markdown 审稿报告默认在对话中输出。若保存具体稿件的 `.md` 报告，默认只保留
在本地，除非用户明确要求发布或推送。

## 可选 K-Dense Companion Skills

这个 skill 可以通过 `references/external_scientific_skills_bridge.md` 可选调用
[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
中的已安装 skills。这是可选增强，不是硬依赖。

推荐安装的 companion skills：

```text
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/paper-lookup
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/database-lookup
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/literature-review
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/scientific-critical-thinking
Use $skill-installer to install https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/scientific-skills/scholar-evaluation
```

如果这些 companion skills 已安装，`rigorous-reviewer` 会把它们用于
论文发现、DOI/PMID/arXiv 查询、公共科学数据库核验、GRADE/risk-of-bias
思考和二次评分校准。若未安装，则回退到内置 search hints、calibration protocol
和 red-line audit。

不建议默认安装 K-Dense 的 `peer-review` skill，因为它与本仓库的核心审稿角色
重叠，可能造成触发歧义。建议以 `rigorous-reviewer` 作为主审稿引擎，
以上 K-Dense skills 仅作为检索、数据库核验、校准和偏倚分析助手。

## 使用示例

安装后，可以在 Codex 中直接提出类似请求：

```text
请使用 rigorous-reviewer 审查这篇 Nature 级别生物论文的创新性和证据漏洞。
请用 rigorous-reviewer 严格审查这篇 AI 论文的方法、benchmark、消融实验和可复现性。
请用 rigorous-reviewer 审查这篇数学论文的证明完整性、隐藏假设和反例风险。
请用 rigorous-reviewer 审查这篇医学 AI 论文是否存在数据泄漏、外部验证不足和临床过度主张。
```

为了获得更完整的评审，建议提供：

```text
Title:
Abstract:
Central Claims / Hypotheses / Theorems:
Figures / Tables / Results / Proofs / Algorithms:
Methods / Data / Code / Materials / Clinical Protocol:
Target Field or Journal:
Supplementary Material: 可选
```

## 证据基础

该 skill 的审稿标准参考了
[Nature peer review 标准](https://www.nature.com/nature/editorial-policies/peer-review)、
[Nature Portfolio 关于 data/materials/code/protocols 的 reporting standards](https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards)、
[ACS research data guidance](https://researcher-resources.acs.org/publish/data_guidelines)、
[ACM artifact review and badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current)、
[AMS Mathematical Reviews reviewer guidance](https://mathscinet.ams.org/mresubs/guide-reviewers.html)，
以及 [CONSORT](https://pubmed.ncbi.nlm.nih.gov/20346629/)、
[PRISMA](https://www.prisma-statement.org/prisma-2020)、
[STROBE](https://www.strobe-statement.org/fileadmin/Strobe/uploads/checklists/STROBE_checklist_v4_combined.pdf)、
[ARRIVE](https://arriveguidelines.org/arrive-guidelines)、
[SPIRIT](https://www.spirit-statement.org/spirit-statement/) 和
[TRIPOD](https://www.bmj.com/content/350/bmj.g7594) 等生物/医学报告规范。

## 参考与致谢

本仓库在整理和增强过程中参考了以下公开 skill 仓库：

- [mattpocock/skills](https://github.com/mattpocock/skills)：主要参考其仓库
  结构、简洁 `SKILL.md` 入口、渐进式加载和面向任务的辅助文件组织方式。
- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)：
  作为可选 companion skills 来源，用于论文检索、公共数据库核验、文献综述和
  scientific critical thinking；这些 skills 需单独安装，本仓库不内置其代码。
- [tanweai/pua](https://github.com/tanweai/pua) 和
  [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)：
  作为 agent skill 打包方式和学术工作流呈现方式的比较参考。

本仓库没有复制第三方 skill 代码。外部仓库保持其原有许可证；实际使用或安装时
应从原始来源获取并遵守对应许可。

## 许可证

MIT
