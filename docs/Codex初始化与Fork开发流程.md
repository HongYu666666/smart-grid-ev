# Codex 初始化与 Fork 开发流程

本流程面向两名固定组员。每人维护自己的 GitHub fork 和任务分支，主仓库只通过 PR 接收成果。Codex 是开发助手，GitHub Issue 的 Assignee 和成果责任人仍是组员本人。

## 1. 需要安装什么

### 必需

- Git；
- GitHub 账号和 GitHub CLI `gh`；
- Node.js `20.19.0` 或更高版本；
- Codex CLI；
- OpenSpec CLI `1.5.0`（与当前仓库生成文件保持一致）。

安装 Codex 和 OpenSpec：

```bash
npm install -g @openai/codex@latest
npm install -g @fission-ai/openspec@1.5.0
```

登录并检查：

```bash
codex login
codex login status
gh auth login
gh auth status
```

Codex 官方支持使用 ChatGPT 账号或 API key 登录；本项目的交互式开发优先使用组员自己的 ChatGPT 登录。不要共享账号、Token 或 API key。

### 推荐但不强制：GitNexus

GitNexus 为 Codex 提供调用关系、影响范围和变更检测。它是 MCP/代码索引增强，不是项目必须安装的 OpenAI 插件。安装或初始化失败时，可以用源码搜索和测试继续工作，但 PR 必须注明没有图索引证据。

```bash
npm install -g gitnexus@1.6.3
gitnexus setup
```

在仓库中首次建立本地索引：

```bash
gitnexus analyze
gitnexus status
codex mcp list
```

`.gitnexus/` 是每个人电脑上的本地索引，已被 Git 忽略，不要提交。

### 不需要安装

- 不需要为本项目创建新的 Codex plugin；
- 不需要 Figma、浏览器自动化等无关插件；
- 不要求安装项目负责人的个人命令代理或 shell 配置；
- 不需要主仓库写权限。

仓库中的 `AGENTS.md` 会被 Codex 启动时自动读取。OpenSpec 的 repo 文件已经纳入 Git，但个人 Codex 的 `/opsx:*` 命令仍需在克隆后同步一次。

## 2. Fork 和 Clone

先在 GitHub 页面 fork：

`https://github.com/TsLouis/smart-grid-ev`

得到：

```text
TsLouis/smart-grid-ev          主仓库 upstream
你的账号/smart-grid-ev          个人 fork origin
```

然后克隆自己的 fork：

```bash
git clone git@github.com:<你的GitHub账号>/smart-grid-ev.git
cd smart-grid-ev
git remote add upstream git@github.com:TsLouis/smart-grid-ev.git
git remote -v
```

`git remote -v` 应显示：

```text
origin    git@github.com:<你的账号>/smart-grid-ev.git
upstream  git@github.com:TsLouis/smart-grid-ev.git
```

如果使用 HTTPS，则两个地址都统一使用 HTTPS，不要混用无效凭据。

## 3. 初始化仓库里的 Codex 工作流

在仓库根目录执行：

```bash
openspec --version
openspec update
openspec list
codex mcp list
```

`openspec update` 会读取仓库中已有的 OpenSpec 配置，并把 `/opsx:explore`、`/opsx:propose`、`/opsx:apply`、`/opsx:sync`、`/opsx:archive` 同步到当前用户的 Codex home。执行后重新启动 Codex。

如果 `openspec update` 导致仓库文件出现意外 diff，不要提交，先在 Issue 中联系 lead 核对 OpenSpec 版本。

运行仓库检查脚本：

```bash
bash scripts/check_codex_setup.sh
```

再验证 Codex 确实读到了仓库规则：

```bash
codex --cd . --ask-for-approval never "只读取仓库并概括当前 AGENTS.md 的任务、分支、验证和 PR 规则，不要修改文件"
```

## 4. 每次开始任务

从主仓库同步最新 `main`：

```bash
git fetch upstream
git switch main
git merge --ff-only upstream/main
git push origin main
```

从更新后的 `main` 创建个人任务分支：

```bash
git switch -c research/<issue编号>-<简短名称>
```

常用分支类型：

- `research/`：调研、选型、运行记录；
- `docs/`：正式文档；
- `feature/`：功能实现；
- `fix/`：缺陷修复；
- `test/`：测试与验收工具。

一个分支只处理一个主要 Issue。时间安排以两周成果窗口为主，不要求每天卡死，但组员应在 Issue 中保持进展、证据和阻塞可见。

## 5. 启动自己的 Codex

在任务分支和仓库根目录启动 `codex`，把 Issue、OpenSpec change 和自己的角色告诉它：

```text
你在我的 smart-grid-ev fork 中处理 GitHub Issue #<编号>。
主仓库是 TsLouis/smart-grid-ev，当前 OpenSpec change 是 <change-id>，
我的角色是 member（组员）。

请先读取 AGENTS.md、CONTRIBUTING.md、Issue 和该 change 下的全部文件，
再检查当前分支、origin/upstream 和工作区。先说明范围、拟修改文件、证据和验证方式，
得到确认后再实施。只处理本 Issue，不直接推送 upstream/main，不把研究假设写成已验证结论。
完成后运行检查、更新自己负责的 tasks、检查 diff，并准备 commit 和 PR 内容。
```

组员应先阅读 Codex 的计划。发现它扩大范围、改公共接口或准备安装新的生产依赖时，必须暂停并在 Issue 中请求 lead 决定。

## 6. 提交到个人 fork

Codex 完成后，组员本人检查：

```bash
git status --short --branch
git diff
```

只暂存明确文件：

```bash
git add <明确文件列表>
git diff --cached --check
git commit -m "docs: add grid simulator assessment"
git push -u origin research/<issue编号>-<简短名称>
```

不要使用 `git add .`，不要让 Codex 将缓存、原始数据、密钥或个人配置提交到 fork。

## 7. 向主仓库提 PR

在 GitHub 页面选择：

```text
base repository: TsLouis/smart-grid-ev
base branch: main
head repository: <你的账号>/smart-grid-ev
compare branch: research/<issue编号>-<简短名称>
```

也可以使用 GitHub CLI：

```bash
gh pr create \
  --repo TsLouis/smart-grid-ev \
  --base main \
  --head <你的GitHub账号>:research/<issue编号>-<简短名称>
```

PR 提交后：

1. 实现者将状态改为“待 Review”；
2. 另一名组员检查内容和证据；
3. lead 检查与正式成果/OpenSpec 是否一致；
4. lead 合并 PR；
5. 组员同步自己的 fork，删除已完成任务分支。

## 8. 常见问题

### Codex 没有看到 `/opsx:*`

重新执行 `openspec update`，然后重启 Codex。不要重复运行 `openspec init --force`，以免覆盖仓库已有配置。

### GitNexus 不可用

继续使用 `rg`、直接源码阅读和针对性测试；在 PR 中写明 GitNexus 未启用。GitNexus 不可用不能成为调研、文档或局部实现长期停滞的理由。

### fork 落后主仓库

在自己的 `main` 上执行：

```bash
git fetch upstream
git merge --ff-only upstream/main
git push origin main
```

不要在多人协作分支上执行破坏性 reset，也不要对别人使用的分支强推。

## 参考

- Codex CLI 与登录：<https://learn.chatgpt.com/docs/codex/cli>、<https://learn.chatgpt.com/docs/auth>
- Codex `AGENTS.md`：<https://learn.chatgpt.com/docs/agent-configuration/agents-md>
- Codex skills：<https://learn.chatgpt.com/docs/build-skills>
- Codex MCP：<https://learn.chatgpt.com/docs/extend/mcp>
- OpenSpec：<https://github.com/Fission-AI/OpenSpec>
- GitNexus：<https://github.com/abhigyanpatwari/GitNexus>
