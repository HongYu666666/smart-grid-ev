## 1. 上层对齐

- [x] 1.1 `member`（Reviewer: `lead`）确认本 change 的上层合同、需求编号和移交来源，写入 `openspec/changes/prepare-ev-scenario-input-data/{README.md,proposal.md}`；验证：README 与 proposal 声明 `openspec/specs/unified-ev-grid-data-model/spec.md`、`REQ-EV-001/008/009` 和归档 change `2026-07-31-define-unified-ev-grid-data-model` 的 tasks 4.1／4.2，且不修改任何已归档文件。
- [x] 1.2 `member`（Reviewer: `lead`）在 `proposal.md` 的 Non-goals 中固定本 change 不做运行时代码、适配器、领域算法、安全校验分类和映射表修改；验证：Non-goals 与 `docs/deliverables/软件设计规格说明书.md` 第 1.2、9 节的模块边界无冲突。
- [ ] 1.3 `lead`（Reviewer: `member`）裁定本模块在总体架构中的正式模块名称与目录位置，并确认是否与 Issue #23 的“数据接入与统一对象注册”合并；验证：裁定结果写入 Issue #19 或 #23，且与 `design.md` 的 Open Questions 第 1 条对应关闭。

## 2. 模块契约设计

- [x] 2.1 `member`（Reviewer: `lead`）编写 `openspec/changes/prepare-ev-scenario-input-data/design.md`，覆盖资产复用、输入包与数据集条目语义槽位、六层校验顺序、缺口判定、转换留痕、输入侧证据和内部设计自由度；验证：design 的每项 Decision 均给出替代方案或不采用理由。
- [x] 2.2 `member`（Reviewer: `lead`）编写 `openspec/changes/prepare-ev-scenario-input-data/specs/ev-scenario-input-data-preparation/spec.md`，形成 11 项 Requirement 且每项含正常路径与至少一条拒绝路径 Scenario；验证：全部 Requirement 使用 MUST/SHALL 并标注来源需求与上层 Requirement。
- [x] 2.3 `member`（Reviewer: `lead`）在 spec 中固定结构化输入错误分类，至少区分 schema 不兼容、清单不完整、来源不可确定、完整性缺失、身份冲突、度量非法、引用不可解析、质量不可用和内部错误；验证：错误分类与 `docs/deliverables/统一数据模型设计说明书.md` 第 10.1 节的错误边界一致。
- [x] 2.4 `member`（Reviewer: `lead`）把 `docs/deliverables/电动汽车场景基础数据清单.md` 的七类数据、仓库外数据声明和来源质量汇总转成可判定的条目要求；验证：清单中的区域数据包与 `jun30` 基线分别对应“已登记哈希的受限条目”和“不可独立校验条目”两条 Scenario。

## 3. 成果文档

- [x] 3.1 `member`（Reviewer: `lead`）编写 `docs/deliverables/场景输入数据准备模块设计说明书.md`，说明模块定位、输入包结构、字段级语义槽位、校验分层、错误分类、受限数据登记、输入侧证据和需求追踪；验证：文档逐项追踪本 change 的 11 项 Requirement 且不含运行时完成声明。
- [x] 3.2 `member`（Reviewer: `lead`）在成果文档中分栏记录新系统目标状态与参考项目复现状态；验证：`ev_charging_v1`、V2Sim、pandapower 仅出现在参考/来源栏，`REQ-EV-*` 状态保持“规划中”。

## 4. 验证

- [x] 4.1 `member`（Reviewer: `lead`）执行 `git diff --check` 并确认无空白错误；验证：命令退出码为 0 且结果记录在 PR。
- [x] 4.2 `member`（Reviewer: `lead`）执行本 change 与成果文档的结构与本地链接检查，确认 change 目录含 `.openspec.yaml`、`README.md`、`proposal.md`、`design.md`、`specs/**/spec.md`、`tasks.md`，且文档内相对链接目标存在；验证：检查命令与输出记录在 PR。
- [ ] 4.3 `member` 或 `lead`（Reviewer: 另一方）在具备 OpenSpec CLI 的环境执行 `openspec validate prepare-ev-scenario-input-data` 与 `openspec status --change prepare-ev-scenario-input-data`；验证：命令输出记录在 PR。本机未安装该 CLI，已在 PR 中如实说明并提供 4.2 的等价结构检查。

## 5. 交叉 Review、文档收敛与验收

- [ ] 5.1 `lead`（Reviewer: `member`）Review 本 change 是否足以支撑数据准备/场景输入模块实现，且未把参考项目格式提升为新系统输入契约；验证：在 PR 中逐条确认或退回。
- [ ] 5.2 `lead`（Reviewer: `member`）确认本 change 的语义槽位、模块名称和数据流与 Issue #23 的可运行薄切片一致；验证：冲突项以上层修订或 Issue 记录方式关闭，不在本 change 自行改名。
- [ ] 5.3 `lead`（Reviewer: `member`）裁定 `design.md` 中的 7 项 Open Questions，未裁定项转为后续 Issue；验证：每项给出裁定结论或明确的后续入口。
- [ ] 5.4 `lead`（Reviewer: `member`）完成最终验收，确认本 change 只建立模块契约、未宣称运行时已实现；验证：Issue #19 验收项、本 tasks 勾选、PR 文件范围和合并结论一致。
