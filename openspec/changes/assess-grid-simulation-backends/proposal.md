## Why

正式进度安排在 2026 年 7 月 18—24 日要求形成《V2Sim 典型案例运行记录》和《配电网仿真工具选型与验证报告》。当前仓库已有 V2Sim 快照和若干工具调研结论，但尚未使用统一标准比较 OpenDSS、GridLAB-D、pandapower、PowerModelsDistribution 等候选项目，也缺少能支撑后续选型的可复现证据。

## What Changes

- 在当前两周成果窗口内运行并记录至少一个 V2Sim 代表性案例，梳理车辆、充电站、负荷、配电网约束、动作和指标的输入输出。
- 使用统一评价矩阵分析 OpenDSS、GridLAB-D、pandapower、PowerModelsDistribution，允许补充有明确理由的候选项目。
- 对条件允许的候选项目完成最小安装/运行验证；无法运行时记录环境、依赖、数据或许可阻塞，不把资料阅读冒充实测。
- 形成《配电网仿真工具选型与验证报告》有证据的初版，给出阶段建议、风险和下一步 PoC，不要求在证据不足时强行确定唯一主内核。
- 将 V2Sim、OpenDSS、GridLAB-D、pandapower、PowerModelsDistribution 及新增项目统一视为候选参考项目；调研和复现结果不构成新系统实现状态或代码基线。
- 将本轮结论作为后续统一数据模型和仿真内核适配 change 的输入。

### Non-goals

- 本 change 不把候选项目正式集成进生产代码。
- 本 change 不把任何候选项目的仓库结构、示例工程或运行结果直接指定为新系统 baseline。
- 本 change 不搭建完整多场景联合仿真平台。
- 本 change 不因计划日期而跳过许可、数据、精度、接口或可复现性检查。
- 本 change 不把 V2Sim 作为整个运行架构评估模块的唯一主内核。

## Capabilities

### New Capabilities

- `grid-simulation-backend-assessment`: 定义候选仿真项目的统一评价、最小运行证据、V2Sim 边界和阶段建议要求。

### Modified Capabilities

无。该 change 形成选型输入，不修改现有运行时 capability。

## Impact

- 正式成果：`docs/deliverables/V2Sim典型案例运行记录.md`、`docs/deliverables/配电网仿真工具选型与验证报告.md`。
- 输入：正式计划和已批准 OpenSpec 作为需求边界；`v2sim/`、现有世界模型调研材料、候选项目官方文档/仓库和最小案例作为参考输入。
- 分工：`member` 代表两名组员组成的执行小组，共同负责 V2Sim 运行记录和候选配电网仿真项目预研；`lead` 确认评价标准并验收阶段建议。两名组员在实际 Issue/PR 中自行协商具体分工。
- 代码/API：原则上不修改 `smart_grid_core` 公共接口；如需试验代码，放在独立、可删除的验证目录并通过单独 Issue 授权。
- 外部依赖：候选项目可能引入 Python、Julia、Java/.NET 或本地求解器环境；安装前先记录依赖和许可，不将试验依赖直接加入生产环境。
- 验收证据：官方来源、版本/提交、安装记录、最小输入、运行命令、输出摘要、失败日志、评价矩阵和 Reviewer 意见。
