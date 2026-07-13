# 协作与提交指南

本仓库由软件负责人、组员 A、组员 B 三人协作，默认使用 Codex 辅助实现。本文规定从领任务到验收的完整流程；项目范围与 Codex 强制规则另见 `AGENTS.md`。

## 1. 开工前

每个任务必须同时具备：

- 一个 GitHub Milestone；
- 一个已完成 proposal/specs/design/tasks 的 OpenSpec change；
- 一个明确负责人、Reviewer、截止时间和验收方式的 GitHub Issue。

缺少任一项时，先补齐治理信息，不进入功能编码。

## 2. 领取任务

```bash
rtk git fetch origin
rtk git switch main
rtk git pull --ff-only
rtk git switch -c feature/<issue>-<slug>
rtk openspec status --change <change-id>
```

若当前工作区不干净，不要覆盖或暂存来源不明的修改；先联系原修改者处理。

## 3. 让 Codex 实现

给 Codex 的输入必须包含 Issue 编号、change-id 和自己的角色。推荐提示：

```text
你在 smart-grid-ev 仓库处理 GitHub Issue #<编号>，OpenSpec change 是
<change-id>，我的角色是 <member-a|member-b|lead>。请完整阅读 AGENTS.md、
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
rtk git add <明确文件列表>
rtk git diff --cached --check
rtk git commit -m "feat: add EV scenario state contract"
rtk git push -u origin feature/<issue>-<slug>
```

不要使用 `git add .` 吸收来源不明的改动。需要修改公共接口或共享模型时，先在 Issue 中说明影响并等待 Reviewer 确认。

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
