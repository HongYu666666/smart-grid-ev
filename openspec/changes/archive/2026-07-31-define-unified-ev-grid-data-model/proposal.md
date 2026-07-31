## Why

正式进度安排要求在 2026 年 7 月 25—31 日形成电动汽车场景基础数据清单、
统一数据模型设计说明书和软件设计规格书的数据模型初稿。当前需求、映射表、
V2Sim 记录和配网后端报告已经给出对象与接口线索，但尚无独立于候选工具的
统一身份、时序、事件、动作、结果和错误契约，组员无法据此安全地细化模块实现。

## What Changes

- 建立系统级统一数据模型边界，覆盖场景/运行、配电网、常规负荷、车辆/行程、
  交通、充电设施、状态快照、事件、动作、约束、结果、指标、错误和证据元数据。
- 规定跨模块共同遵守的对象 ID、单位、时标、版本、来源、哈希和引用完整性规则。
- 规定“状态观察—动作提案—校验—执行/拒绝—反馈/回退”的数据交互契约，
  保持智能体提案权与孪生/安全校验层裁决权分离。
- 规定配电网主仿真内核、EV/交通工具和 Python 编排层之间的适配边界，不向
  上层暴露 pandapower DataFrame、V2Sim 内部对象或其他候选私有结构。
- 形成三项正式成果：
  - `docs/deliverables/电动汽车场景基础数据清单.md`；
  - `docs/deliverables/统一数据模型设计说明书.md`；
  - `docs/deliverables/软件设计规格说明书.md` 的总体设计和数据模型章节初稿。
- 由 `lead` 维护本 change 的系统级模块和跨模块契约；`member` 从本 change
  引用对应 Requirement/Scenario，在独立 change 中细化所负责模块的字段、
  校验、转换、错误和测试。

### Non-goals

- 本 change 不实现运行时代码、数据库、API、前端或 pandapower 适配器。
- 不固定成员模块内部的类名、函数、存储格式、序列化库或目录结构。
- 不把参考项目样例字段、对象数量、结果或完成状态写成新系统 baseline。
- 不完成 Issue #14 的配网/V2Sim E4 交叉校核，也不据此宣布最终生产内核。
- 不细化其他典型场景；只保留其复用和扩展所需的系统级元数据与接口边界。

## Capabilities

### New Capabilities

- `unified-ev-grid-data-model`: 定义 EV 单场景各模块共享的对象身份、时序、
  状态、事件、动作、约束、结果、错误、指标和证据契约，以及成员模块级
  OpenSpec 必须遵守的跨模块边界。

### Modified Capabilities

无。仓库当前没有已归档的主 capability；本 change 以已批准的
`establish-ev-single-scenario-baseline` 需求和阶段调研结论为输入，不修改其
需求编号或业务含义。

## Impact

- 计划条目：`docs/仿真系统开发进度安排.md` 中 2026.07 的 7.25—7.31 行。
- 上游输入：
  - `docs/deliverables/软件需求分析报告.md`；
  - `docs/deliverables/典型场景-业务需求-孪智功能映射表.md`；
  - `docs/deliverables/V2Sim典型案例运行记录.md`；
  - `docs/deliverables/配电网仿真工具选型与验证报告.md`。
- 关联 Issue：#12 为本 change；#13 依赖本 change 获批；#14 提供后续高等级
  参考证据，但不阻塞系统级模型初稿。
- 负责人：`lead` 为系统级 spec owner，`member` 负责基础数据盘点、交叉 Review
  和后续独立模块级 change。
- 验收证据：三项成果路径、需求/对象/字段追踪、成员 Review、OpenSpec 校验和
  最终 PR。
- 代码/API/依赖：本 change 不修改运行时代码、公共 API 或生产依赖。
