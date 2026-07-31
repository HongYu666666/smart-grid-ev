## 1. 系统级契约准备

- [x] 1.1 `lead` 编写 `openspec/changes/define-unified-ev-grid-data-model/{proposal.md,design.md,specs/**}`，明确统一身份、时间、单位、事件、动作、结果、错误和适配边界；Reviewer：`member`；验证：`openspec status --change define-unified-ev-grid-data-model` 显示 proposal、design、specs 完成。
- [x] 1.2 `member` Review 本 change 的 Requirement/Scenario，逐项检查是否足以细化数据准备模块且未把 v1、V2Sim 或候选后端提升为新系统合同；Reviewer：`lead`；验证：在 #12 留下带结论的 Review 记录并关闭全部阻塞意见。

## 2. 场景数据基础

- [x] 2.1 `member` 恢复并更新 `docs/deliverables/电动汽车承载力提升场景调研报告.md`，保持新系统目标状态与参考项目复现状态分离；Reviewer：`lead`；验证：文档链接检查、参考证据锚点检查和 `git diff --check` 通过。
- [x] 2.2 `member` 新建 `docs/deliverables/电动汽车场景基础数据清单.md`，逐项记录对象/字段组、单位、时间粒度、公共 ID、来源、质量、证据、共享边界、缺口和后续模块归属；Reviewer：`lead`；验证：清单覆盖配电网、常规负荷、车辆/行程、交通、充电设施、事件、动作、约束、结果和指标。
- [x] 2.3 `member` 将基础数据清单映射到 `REQ-EV-001`—`REQ-EV-012` 以及本 change 的 Requirement/Scenario，不以样例数据填补正式数据缺口；Reviewer：`lead`；验证：每项需求至少具有数据输入、产物或明确的“不适用/待获取”记录。

## 3. 正式设计成果

- [x] 3.1 `lead` 编写 `docs/deliverables/统一数据模型设计说明书.md` 初稿，覆盖公共语义内核、领域对象族、状态/事件/动作、适配器、结果/错误、指标、证据和版本演进；Reviewer：`member`；验证：文档逐项追踪本 change 的 11 项 Requirement。
- [x] 3.2 `lead` 编写 `docs/deliverables/软件设计规格说明书.md` 的总体设计和数据模型初稿，明确模块职责、交互方向、安全裁决和后续实现边界；Reviewer：`member`；验证：文档链接到统一数据模型说明书及 `REQ-EV-*`，且不包含未验证的运行时完成声明。
- [x] 3.3 `lead` 根据 member 的场景报告、基础数据清单和 Review 收敛两份设计文档中的来源、缺口与开放问题；Reviewer：`member`；验证：Review 意见逐项关闭，三份文档不存在相互冲突的对象、单位、时序或边界定义。

## 4. 后续移交（不属于本 change 验收）

- 4.1 已转交 Issue #19：`member` 在 8.1 后从最新主分支创建独立的数据准备/
  场景输入模块 OpenSpec change，声明本上层合同、对应 Requirement/Scenario、
  负责模块、外部契约、内部设计自由度、依赖和验收。
- 4.2 随 4.1 转入下一阶段：member 在模块 change 中细化字段、校验、转换、
  结构化错误、版本兼容和测试；公共契约变更必须先形成独立上层修订。

以上为已批准设计基线的后续使用方式，不是
`define-unified-ev-grid-data-model` 的归档阻塞项。

## 5. 集成、文档收敛与验收

- [x] 5.1 `lead` 将 #12、#13、#14 和成员模块 change 的依赖关系与未决问题记录到对应 Issue，保持 OpenSpec 为设计与验收权威；Reviewer：`member`；验证：每个 Issue 可回链到唯一 change、负责人、Reviewer 和当前状态。
- [x] 5.2 `lead` 对本 change 执行 `openspec validate define-unified-ev-grid-data-model`、文档本地链接检查和 `git diff --check`；Reviewer：`member`；验证：命令全部通过且结果记录在 PR。
- [x] 5.3 `member` 对正式设计成果执行最终交叉 Review，确认基础数据缺口、参考证据边界和成员细化入口清晰；Reviewer：`lead`；验证：PR Review 结论为通过或全部阻塞意见已关闭。
- [x] 5.4 `lead` 完成文档收敛和最终接受，确认本 change 只建立设计基线、不宣称新系统运行时已实现；Reviewer：`member`；验证：#12 验收项、OpenSpec tasks、PR 文件范围和合并结论一致。
