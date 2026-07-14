# 协作与提交指南

本仓库由软件负责人和两名组员协作，管理上只区分 `lead` 与 `member` 两类职责，默认使用 Codex 辅助实现。本文规定从领任务到验收的完整流程；项目范围与 Codex 强制规则另见 `AGENTS.md`。

## 1. 开工前

每个实现任务开始前应具备：

- 一个 GitHub Milestone 或明确的成果窗口；
- 一个已完成 proposal/specs/design/tasks 的 OpenSpec change；
- 一个明确负责人、Reviewer、目标窗口和验收方式的 GitHub Issue。

研究型任务允许先在 Issue 中进行资料盘点和可行性验证，但在形成正式技术决定或进入功能编码前，必须补齐 OpenSpec 范围与验收标准。

两名组员各自 fork `TsLouis/smart-grid-ev`。在个人仓库中，`origin` 指向自己的 fork，`upstream` 指向主仓库。详细初始化见 `docs/Codex初始化与Fork开发流程.md`。

## 2. 领取任务

```bash
git fetch upstream
git switch main
git merge --ff-only upstream/main
git push origin main
git switch -c feature/<issue>-<slug>
openspec status --change <change-id>
```

若当前工作区不干净，不要覆盖或暂存来源不明的修改；先联系原修改者处理。

## 3. 让 Codex 实现

给 Codex 的输入必须包含 Issue 编号、change-id 和自己的角色。推荐提示：

```text
你在 smart-grid-ev 仓库处理 GitHub Issue #<编号>，OpenSpec change 是
<change-id>，我的角色是 <member|lead>。请完整阅读 AGENTS.md、
Issue 和 change 文件，只实现 tasks.md 中分配给我的任务。开工前报告影响范围和
验证方式；完成后更新任务勾选、运行验证、检查 diff，并给出建议 commit 和 PR 内容。
```

Codex 可以协助实现和自检，但不能代替负责人批准范围，也不能代替 Reviewer 和软件负责人验收。

## 4. 开发与提交

- 只改 Issue 授权的文件和行为。
- 小步提交，每个 commit 保持可解释、可验证。
- 不把格式化、重构和功能修改混成一个 commit。
- 不提交本地数据、缓存、生成结果、密钥和个人绝对路径。

提交示例：

```bash
git add <明确文件列表>
git diff --cached --check
git commit -m "feat: add EV scenario state contract"
git push -u origin feature/<issue>-<slug>
```

不要使用 `git add .` 吸收来源不明的改动。需要修改公共接口或共享模型时，先在 Issue 中说明影响并等待 Reviewer 确认。

PR 的目标仓库是 `TsLouis/smart-grid-ev`，目标分支是 `main`，来源分支是个人 fork 中的任务分支。组员不需要主仓库写权限。

## 5. PR 内容

PR 必须写清：

- `Closes #<issue>`；
- OpenSpec change-id 和完成的任务编号；
- 形成的代码、文档、数据模板或测试记录路径；
- 实际执行的验证命令与结果；
- 截图、日志、报表或演示路径；
- 已知限制、后续 Issue 和需要负责人裁定的事项。

Reviewer 首先检查范围和接口，再检查实现质量；软件负责人只对通过 Review 且证据完整的 PR 做最终验收。

## 6. 完成定义

任务只有同时满足以下条件才进入 Done：

- OpenSpec 要求和 Scenario 已满足；
- `tasks.md` 中对应任务已由实现者更新；
- 代码、文档和正式成果名称一致；
- 验证可在干净环境复现；
- Reviewer 已批准；
- 软件负责人已验收；
- PR 已合并，必要时已生成 Release 或归档 change。

“完成 80%”“本地可以”“Codex 说通过”均不视为验收证据。
