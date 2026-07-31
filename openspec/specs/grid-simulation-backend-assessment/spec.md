# grid-simulation-backend-assessment Specification

## Purpose
TBD - created by archiving change assess-grid-simulation-backends. Update Purpose after archive.
## Requirements
### Requirement: 本周两份报告具有独立内容合同和责任人
本 change SHALL 只形成两部分成果：`lead` 负责《配电网仿真工具选型与验证报告》和首选 PoC 后端代码目录，GitHub Issue 指定的 `member` 负责《V2Sim 典型案例运行记录》和 V2Sim 代码目录。两部分 MUST 分别使用一个 Issue、一个短期分支和一个 PR，MUST 通过链接共享证据且 MUST NOT 在同一 PR 中互相覆盖。上一周的需求、场景调研和孪智映射任务不得继续作为本周执行入口。

《配电网仿真工具选型与验证报告》 MUST 包含：范围与文档信息、证据等级、四个配网候选的官方来源/版本/维护状态/许可证、统一评价维度、逐候选证据、比较矩阵、需求对应、首选 PoC 后端与备选、阶段建议、下一 PoC、数据模型/适配器输入、风险和限制。四个候选不要求全部建立代码目录；只有进入 PoC 的首选后端 MUST 建立完整目录。

《V2Sim 典型案例运行记录》 MUST 包含：范围与文档信息、案例选择、版本与环境、隔离方法、输入与配置、实际安装/生成/运行命令、车辆/交通/充电/配网/控制/指标输出、结果检查、失败记录、证据等级、能力边界和干净环境复现步骤。固定版本 V2Sim MUST 建立完整代码目录。

#### Scenario: lead 开始配网后端选型报告
- **WHEN** lead 根据本 change 开始本周工作
- **THEN** 使用独立 lead Issue/分支填写四个配网候选的统一矩阵和阶段建议，不代写 V2Sim 运行成功结论

#### Scenario: member 开始 V2Sim 运行记录
- **WHEN** GitHub Issue 指定的 member 开始本周工作
- **THEN** 只在个人 fork 的独立分支提交 V2Sim 运行与边界证据，不修改配网后端选型报告或上一周映射表

#### Scenario: Reviewer 检查本周 GitHub 环境
- **WHEN** Reviewer 查看开放 Issue 和 PR
- **THEN** 只存在本 change 的 lead/member 工作入口；上一周未验收的 Issue/PR 已关闭且不继续作为执行依据

### Requirement: V2Sim 与首选配网后端具有完整函数类目录
V2Sim 和进入 PoC 的首选配网后端 MUST 分别在 `docs/reference_catalogs/v2sim/` 与 `docs/reference_catalogs/grid_backend/<selected-project>/` 形成基于固定版本源码的完整目录。目录 MUST 覆盖生产源码中的所有模块级函数、类和类方法，包括私有/内部符号；测试、示例、vendored、生成代码和构建产物可以排除，但 MUST 在覆盖率报告中记录。

每个目录 MUST 包含项目/版本/扫描范围说明、机器可读 `symbols.csv`、覆盖率报告和按模块组织的人类可读目录。每个符号 MUST 记录类型、限定名、签名、源码锚点、可见性、非空功能说明、输入输出、副作用、依赖、开发用途、证据状态和复核状态。功能无法可靠确认时 MUST 写清待确认点，不得留空或虚构。

全量符号清单和功能初稿 SHALL 自动生成。与新系统开发直接相关的核心模块、公共入口和关键调用链 MUST 逐项人工复核；内部支撑模块 SHALL 按模块抽检。MUST NOT 要求负责人从零手写全部符号，或为未入选的三个配网候选建立全量目录。

#### Scenario: 自动生成初始目录
- **WHEN** 负责人对固定版本源码运行目录生成器
- **THEN** 所有可解析函数、类和方法进入 `symbols.csv` 和对应模块目录，未解析文件与排除项进入 `coverage.md`

#### Scenario: 源码符号缺少文档
- **WHEN** 自动提取到没有 docstring、注释或可确认功能说明的符号
- **THEN** 目录保留该符号并标记“待人工补充”，不得因为无法解释而省略

#### Scenario: Reviewer 验收目录完整性
- **WHEN** Reviewer 重新扫描同一版本源码
- **THEN** 源码限定名集合与目录集合无遗漏、无重复，所有差异和未解析文件均有明确记录

#### Scenario: Reviewer 验收人工工作范围
- **WHEN** 全量目录包含大量内部函数或方法
- **THEN** 核心开发相关符号均为“人工复核”，其余符号至少具有非空功能初稿和明确复核状态，并按模块留下抽检记录

#### Scenario: 候选后端尚未进入 PoC
- **WHEN** OpenDSS、GridLAB-D、pandapower、PowerModelsDistribution 中某候选未被选为首选 PoC 后端
- **THEN** 该候选只需保留统一比较和证据，不要求投入全量函数/类目录整理

### Requirement: 候选项目使用统一评价框架
评估 SHALL 至少覆盖 OpenDSS、GridLAB-D、pandapower、PowerModelsDistribution，并 MUST 对所有候选项目使用同一组核心维度：官方来源与维护状态、许可证、建模范围、求解能力、时序/控制能力、编程接口、平台与依赖、数据要求、最小运行证据、项目适配边界和主要风险。所有对象均 SHALL 作为候选参考项目评估，不得因证据等级提高而成为新系统代码或验收 baseline。

#### Scenario: 比较两个候选项目
- **WHEN** Reviewer 对比任意两个候选项目
- **THEN** 报告中存在相同维度、相同证据等级和可追踪来源，不使用无法解释的综合分数代替事实

#### Scenario: 新增候选项目
- **WHEN** 组员发现具有明确项目价值的其他开源项目
- **THEN** 可在 Issue 中说明理由后加入，并使用同一评价框架，不删除正式计划中已有候选项

### Requirement: 资料结论具有官方来源和版本
每个候选项目的关键结论 MUST 引用项目官方文档、官方仓库、发布信息或许可证文件，并 SHALL 记录评估日期、版本或提交。二手文章可以作为线索，但不得作为采用决定的唯一证据。

#### Scenario: 写入能力或许可结论
- **WHEN** 报告声明某项目支持特定模型、接口、平台或许可证
- **THEN** 同一条目包含可定位的官方来源和所评估版本

### Requirement: 运行证据与资料阅读分级
评估 MUST 区分资料确认、安装/导入成功、最小案例运行成功和项目数据验证四级候选证据。只有实际执行过的等级才能标为该候选项目已验证；失败 MUST 保留环境、命令、错误摘要和下一步判断。候选项目证据 MUST NOT 计入新系统实现状态。

#### Scenario: 最小案例成功
- **WHEN** 候选项目完成最小案例运行
- **THEN** 记录环境、版本、输入、命令、输出摘要、运行时间和结果检查方式

#### Scenario: 候选项目无法安装或运行
- **WHEN** 安装、平台、许可证、求解器或数据问题阻止最小案例
- **THEN** 报告保留失败证据并降低该项证据等级，不将其描述为功能不支持或项目不可用，除非官方材料能够证明

### Requirement: V2Sim 能力边界可复现
《V2Sim 典型案例运行记录》 SHALL 记录至少一个代表性案例的环境、配置、运行命令、输入、车辆/充电站/配网输出、控制动作、评价指标和已知限制。记录 MUST 说明 V2Sim 可参考内容以及它与配电网主仿真内核、Python 编排层的边界，并明确 V2Sim 不是新系统代码或验收 baseline。

#### Scenario: 复现 V2Sim 案例
- **WHEN** Reviewer 在满足记录环境的机器上按照步骤执行案例
- **THEN** 能定位主要输出，理解输入输出关系，并确认记录中声明的能力和限制

#### Scenario: V2Sim 依赖不完整
- **WHEN** 当前机器无法完成代表性案例运行
- **THEN** 记录缺少的依赖/外部程序/数据和已完成的最深验证步骤，不把现有源代码快照等同于运行成功

### Requirement: 阶段建议保留不确定性
《配电网仿真工具选型与验证报告》 SHALL 给出本周成果验收时的阶段建议，包括推荐继续 PoC、保留候选、暂缓或淘汰，并 MUST 说明证据、适用范围、风险和下一验证动作。证据不足时 SHALL NOT 强行确定唯一主仿真内核。

#### Scenario: 多个候选各有优势
- **WHEN** 不同候选项目分别适合快速 Python 集成和高保真工程校核
- **THEN** 阶段建议可以保留分层或组合路线，并明确每个工具的责任边界和待验证问题

#### Scenario: 形成后续实现输入
- **WHEN** lead 验收本 change
- **THEN** 报告能够直接生成后续 PoC、统一数据模型或适配器 change 的范围、依赖和验收标准

### Requirement: 试验环境不污染新系统开发环境
候选项目的安装和最小案例 SHALL 使用隔离环境或明确的临时验证方式。未经独立实现 change 批准，不得把试验依赖加入新系统正式依赖、修改公共接口、复制候选项目结构或提交大体积生成数据。

#### Scenario: 候选项目需要新依赖
- **WHEN** 组员准备安装候选项目或求解器
- **THEN** 先记录版本、许可证和隔离方法；试验结束后只提交必要脚本、配置和小型证据，不提交环境缓存或二进制产物
