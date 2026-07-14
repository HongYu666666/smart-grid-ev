# EV Charging Repository Instructions

本仓库由 1 名软件负责人和 2 名固定组员共同维护，日常开发默认由 Codex 辅助完成。两名组员各自 fork 主仓库，在个人 fork 的任务分支上工作，再向主仓库 `main` 提交 PR。

## 权威来源

发生冲突时，按以下顺序处理：

1. `docs/仿真系统开发进度安排.md`：里程碑、时间和正式成果名称。
2. 当前 `openspec/changes/<change-id>/`：本次变更的范围、需求、设计和验收任务。
3. 对应 GitHub Issue：负责人、成果窗口、依赖和协作状态。
4. 现有实现与研究文档：作为复用资产和实现证据，不得反向修改已批准范围。

没有已批准 OpenSpec change 和对应 Issue 时，不开始新的功能实现。发现需求不清或范围冲突时，先在 Issue 中记录并交由软件负责人裁定。

## 三人职责

- `lead`（软件负责人）：维护计划与 OpenSpec、拆分任务、处理接口决策，承担少量集成/文档工作并最终验收。原则上不包办组员模块。
- `member-a`：配电网/交通/电动汽车仿真、数据模型、场景适配和运行内核。
- `member-b`：孪智交互接口、智能体编排、结果管理、可视化与自动化测试。

具体人员姓名和当前任务以 `docs/项目推进与分工.md` 及 GitHub Issue 为准。模块边界允许按里程碑调整，但每个 Issue 只能有一个直接负责人和一个 Reviewer。

## Codex 开工顺序

接到任务后，Codex 必须依次执行：

1. 阅读本文件、对应 Issue、当前 OpenSpec change 和相关源文件。
2. 执行 `git status --short --branch`，确认位于个人 fork 的任务分支且工作区没有来源不明的修改。
3. 执行 `openspec status --change <change-id>`，确认所做内容在 change 范围内。
4. GitNexus 可用且索引新鲜时，在修改函数、类或方法前执行影响分析；不可用时用直接源码检查、搜索和针对性测试替代，并在 PR 中说明。
5. 只实现 Issue 中的任务；发现额外问题时新建或建议新建 Issue，不顺手扩大本 PR。
6. 实现后运行针对性检查和仓库基线检查，更新 `tasks.md` 中由自己完成的任务。
7. 提交原子 commit，推送到个人 fork 的任务分支，并按模板向主仓库创建 PR；不得直接推送主仓库 `main` 或长期使用 `sim` 开发。

推荐在新 Codex 会话中使用以下开场提示：

```text
请先阅读 AGENTS.md、GitHub Issue #<编号> 和
openspec/changes/<change-id>/ 下的全部文件。只处理分配给 <member-a|member-b|lead>
的未完成任务。先检查分支与工作区，再说明拟修改文件、验收标准和验证命令；
完成后更新 tasks.md，运行验证并准备符合模板的 commit/PR，不要扩大范围。
```

## 分支、提交与 PR

- 个人 fork 使用 `origin`，主仓库使用 `upstream`。先同步 `upstream/main`，再创建短期分支：`feature/<issue>-<slug>`、`fix/<issue>-<slug>`、`research/<issue>-<slug>`、`docs/<issue>-<slug>` 或 `chore/<issue>-<slug>`。
- 一个分支只服务一个 Issue；一个 PR 只交付一个可验收目标。
- commit 使用 `feat:`、`fix:`、`docs:`、`test:`、`refactor:`、`chore:` 前缀，描述具体结果，避免 `update`、`修改一下` 等模糊信息。
- 不提交原始大数据、运行产物、缓存、密钥、个人路径配置或 Codex 临时记录。
- PR 必须关联 Issue 和 OpenSpec change，列出成果路径、验证命令、验证结果、已知限制和 Reviewer。
- 实现者负责自测，Reviewer 负责代码/文档审查，`lead` 负责最终验收。实现者不能自行把成果标记为“已验收”。

## 最低验证门槛

在 `ev_charging_v1/` 中至少执行：

```bash
python -m compileall -q smart_grid_core
python -m smart_grid_core.tools.root_step_check --root .
python -m smart_grid_core.tools.parity_report --root .
```

若改动无法运行其中某项，必须在 PR 中说明原因，并提供等价的针对性检查。最终验收还必须包含 OpenSpec 场景、计划成果文件和可复现证据。

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **smart-grid-ev** (1378 symbols, 2364 relationships, 53 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> GitNexus is a recommended enhancement, not a startup blocker. If it is configured and the index is stale, run `npx gitnexus analyze` in terminal first.

## Always Do

- When GitNexus MCP is available and fresh, run impact analysis before editing a shared symbol and report the blast radius.
- When GitNexus MCP is available, run `gitnexus_detect_changes()` before committing.
- Warn the user if available impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `gitnexus_query({query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `gitnexus_context({name: "symbolName"})`.

## Never Do

- When GitNexus is available, do not edit a shared function, class, or method without first running `gitnexus_impact` on it.
- Never ignore HIGH or CRITICAL risk warnings returned by impact analysis.
- NEVER rename symbols with find-and-replace — use `gitnexus_rename` which understands the call graph.
- NEVER commit changes without running `gitnexus_detect_changes()` to check affected scope.

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/smart-grid-ev/context` | Codebase overview, check index freshness |
| `gitnexus://repo/smart-grid-ev/clusters` | All functional areas |
| `gitnexus://repo/smart-grid-ev/processes` | All execution flows |
| `gitnexus://repo/smart-grid-ev/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->
