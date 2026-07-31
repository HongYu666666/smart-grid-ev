## Why

正式进度安排在 2026 年 7 月 18—24 日要求形成《V2Sim 典型案例运行记录》和《配电网仿真工具选型与验证报告》。当前仓库已有 V2Sim 快照和若干工具调研结论，但尚未使用统一标准比较 OpenDSS、GridLAB-D、pandapower、PowerModelsDistribution 等候选项目，也缺少能支撑后续选型的可复现证据。

## What Changes

- 将本周成果明确拆成两个互不重叠的交付部分：
  - `member` 负责《V2Sim 典型案例运行记录》，运行并记录至少一个代表性案例，梳理车辆、充电站、负荷、配电网约束、动作和指标的输入输出；
  - `lead` 负责《配电网仿真工具选型与验证报告》，使用统一评价矩阵分析 OpenDSS、GridLAB-D、pandapower、PowerModelsDistribution。
- `member` 对 V2Sim 完成当前环境允许的最高证据等级验证；无法运行时记录环境、依赖、输入、命令、错误和已完成的最深步骤，不把资料阅读或文件存在冒充实测。
- `lead` 基于官方资料、许可、版本和可获得的最小验证证据形成四个配网后端的比较初版，选出一个进入下一步 PoC 的首选后端并给出备选；证据不足时保留待裁定，不强行确定唯一生产内核。
- 最终形成两份可供开发使用的代码目录：
  - `member` 为固定版本的 V2Sim 生成全部生产源码函数、类和方法目录；
  - `lead` 只为进入 PoC 的首选配网后端生成同样的完整目录，其余候选不做全量符号整理。
- 代码目录通过自动提取生成完整清单和逐符号功能初稿；所有符号均保留功能说明与复核状态，负责人只对直接影响后续开发的核心模块逐项人工复核，其余模块按模块抽检，不要求人工从零抄写全部符号。
- 两份报告使用相同的 E0—E4 证据等级和参考项目边界，通过链接共享证据，不在同一 PR 中混写或互相覆盖。
- 将 V2Sim、OpenDSS、GridLAB-D、pandapower、PowerModelsDistribution 及新增项目统一视为候选参考项目；调研和复现结果不构成新系统实现状态或代码基线。
- 将本轮结论作为后续统一数据模型和仿真内核适配 change 的输入。

### Non-goals

- 本 change 不把候选项目正式集成进生产代码。
- 本 change 不把任何候选项目的仓库结构、示例工程或运行结果直接指定为新系统 baseline。
- 本 change 不搭建完整多场景联合仿真平台。
- 本 change 不因计划日期而跳过许可、数据、精度、接口或可复现性检查。
- 本 change 不把 V2Sim 作为整个运行架构评估模块的唯一主内核。
- 本 change 不要求对四个配网候选全部建立函数/类目录，也不要求在本周人工逐字重写全量符号说明。

## Capabilities

### New Capabilities

- `grid-simulation-backend-assessment`: 定义候选仿真项目的统一评价、最小运行证据、V2Sim 边界和阶段建议要求。

### Modified Capabilities

无。该 change 形成选型输入，不修改现有运行时 capability。

## Impact

- 正式成果：
  - `member`：`docs/deliverables/V2Sim典型案例运行记录.md`、`docs/reference_catalogs/v2sim/`；
  - `lead`：`docs/deliverables/配电网仿真工具选型与验证报告.md`、`docs/reference_catalogs/grid_backend/<selected-project>/`。
- 输入：正式计划和已批准 OpenSpec 作为需求边界；`v2sim/`、现有世界模型调研材料、候选项目官方文档/仓库和最小案例作为参考输入。
- 分工：`member` 的当前直接负责人由 GitHub Issue/PR 记录，独立交付 V2Sim 运行记录；`lead` 独立交付配网后端选型报告并做最终集成验收。两部分分别使用一个 Issue、一个短期分支和一个 PR，互为 Reviewer，不另建分工台账。
- 代码/API：原则上不修改 `smart_grid_core` 公共接口；如需试验代码，放在独立、可删除的验证目录并通过单独 Issue 授权。
- 外部依赖：候选项目可能引入 Python、Julia、Java/.NET 或本地求解器环境；安装前先记录依赖和许可，不将试验依赖直接加入生产环境。
- 验收证据：官方来源、版本/提交、安装记录、最小输入、运行命令、输出摘要、失败日志、评价矩阵、符号清单、目录覆盖率和 Reviewer 意见。
