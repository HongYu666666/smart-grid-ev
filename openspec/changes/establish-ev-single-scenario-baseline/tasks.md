## 1. 基线准备

- [ ] 1.1 `lead`（Reviewer: `member`）在本 change 中确认三项成果路径、两周成果窗口和 `lead`/`member` 职责边界；验证：proposal、design、specs、tasks 表述一致，且没有外部分工台账依赖。
- [x] 1.2 `lead`（Reviewer: `member`）从任务书/实施方案和正式计划提取可定位的来源条目，建立 `REQ-EV-001` 起的需求编号清单；成果：`docs/deliverables/软件需求分析报告.md`；验证：每条规范性需求包含来源和验收方式。

## 2. 软件需求分析报告

- [x] 2.1 `lead`（Reviewer: `member`）完成 `docs/deliverables/软件需求分析报告.md` 的引言和综合描述，写清建设目标、系统边界、参与者、运行环境、约束、假设和非目标；验证：与正式计划技术基线无冲突。
- [x] 2.2 `lead`（Reviewer: `member`）完成单场景需求章节，覆盖对象、输入、状态、事件、动作、约束、指标、正常/异常流程以及新系统目标状态；参考代码库复现状态单独记录，不计入新系统完成度；验证：所有 `REQ-EV-*` 均有验收方式且不存在重复编号。

## 3. 电动汽车承载力提升场景调研

- [ ] 3.1 `member`（Reviewer: `lead` 或另一名组员）盘点现有 EV 研究材料、`ev_charging_v1/`、V2Sim 和后续调研项目，将其作为参考代码库分类为已复现、部分可参考、待调研、不适用；成果：`docs/deliverables/电动汽车承载力提升场景调研报告.md`；验证：每项“已复现”参考能力具有命令或文件锚点，且没有写成新系统已实现能力。
- [ ] 3.2 `member`（Reviewer: `lead` 或另一名组员）补全场景业务流程、对象/数据、控制动作、物理与业务约束、评价指标、异常情形和数据缺口；验证：内容能支撑后续工具选型与统一数据模型 change，且未提前决定配电网主仿真工具。
- [ ] 3.3 `member`（Reviewer: `lead` 或另一名组员）复现并记录 v1 参考项目，不称其为新系统原型或基线；在 `ev_charging_v1/` 执行 `python -m smart_grid_core.tools.root_step_check --root .` 和 `python -m smart_grid_core.tools.parity_report --root .`，把命令、环境、结果摘要和“仅供参考、不计入新系统验收”的结论写入调研报告。

## 4. 场景-业务需求-孪智功能映射

- [x] 4.1 `lead`（Reviewer: `member`）创建 `docs/deliverables/典型场景-业务需求-孪智功能映射表.md`，至少包含 design.md 定义的 11 个共同字段；验证：所有 `REQ-EV-*` 在映射表中至少出现一次。
- [x] 4.2 `lead`（Reviewer: `member`）逐行区分新系统孪生体、智能体、工具/模型组件责任，补充动作校验、拒绝/回退、新系统证据和目标状态；验证：不存在把确定性工具直接标为独立智能体的行，也不存在用参考项目结果代替新系统证据的行。
- [x] 4.3 `lead`（Reviewer: `member`）将 `ev_charging_v1/`、V2Sim 和后续项目作为参考资产映射到需求 ID，并与新系统目标组件、证据和状态分栏记录；验证：参考声明包含仓库相对路径或复现命令，所有尚未独立实现的新系统能力标记为“规划中”或“待裁定”。

## 5. 交叉 Review 与一致性收敛

- [ ] 5.1 `member`（Reviewer: `lead`）Review 软件需求分析报告和映射表中的仿真/数据语义，在 PR 中逐项确认或提出修改意见。
- [ ] 5.2 `member`（Reviewer: `lead`）Review 场景调研报告中的孪智边界、接口语义和证据状态，在 PR 中逐项确认或提出修改意见。
- [ ] 5.3 `lead`（Reviewer: `member`）统一三项成果中的术语、需求 ID、对象、动作、约束和指标；验证：抽查任一 `REQ-EV-*` 均可在三项成果间追踪且定义一致。

## 6. 验证、归档输入与最终验收

- [ ] 6.1 `lead`（Reviewer: `member`）执行 `openspec validate establish-ev-single-scenario-baseline`、`git diff --check` 和文档链接/路径检查，并在最终 PR 记录结果。
- [ ] 6.2 `lead`（Reviewer: `member`）从已验收成果提取 `select-grid-simulation-backend` 与 `define-unified-data-model` 的输入、依赖和待裁定问题，记录在最终 PR 的后续工作中。
- [ ] 6.3 `lead`（Reviewer: `member`）完成最终验收：确认三项正式成果、交叉 Review、复现证据和 OpenSpec 验证全部通过后合并 PR；未满足项必须退回对应负责人，不以完成百分比代替验收。
