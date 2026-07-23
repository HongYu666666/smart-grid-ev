## 1. 评估准备

- [ ] 1.1 lead（Reviewer: member）确�?V2Sim、OpenDSS、GridLAB-D、pandapower、PowerModelsDistribution 五个对象及统一评估维度，在 `docs/deliverables/配电网仿真工具选型与验证报�?md` 建立报告骨架；逐项检查对象、维度和证据栏均已覆�?
- [ ] 1.2 lead（Reviewer: member）建立组员调�?Issue，写明两周成果窗口和证据目标；组员在开始后自行记录实际分工，不限定每日进度

## 2. V2Sim 典型案例验证

- [x] 2.1 member（Reviewer: lead 或另一名组员）选择一个代表�?V2Sim 案例，在 `docs/deliverables/V2Sim典型案例运行记录.md` 记录环境、依赖、输入和运行命令；由 Reviewer 按记录从干净环境复核准备步骤
- [x] 2.2 member（Reviewer: lead 或另一名组员）完成当前环境允许的最高证据等级验证，保存成功输出、失败日志或受限原因，并在运行记录中标注 E0-E4 等级；使用原始命令和关键输出交叉核对结论
- [x] 2.3 member（Reviewer: lead）在运行记录中区分可参考的交通、充电、电动汽车能力与配电网计算内核、Python 编排层边界，并明�?V2Sim 不是新系�?baseline；由 lead 对照当前需求分析和映射表复核边�?

## 3. 配电网仿真后端调�?

- [ ] 3.1 member（Reviewer: lead 或另一名组员）基于官方仓库和文档补全四个候选后端的统一比较矩阵，写�?`docs/deliverables/配电网仿真工具选型与验证报�?md`；每条关键判断均附来源、版本或提交信息
- [ ] 3.2 member（Reviewer: lead 或另一名组员）在隔离环境中对条件允许的候选后端尝试安装、导入和最小案例运行，记录命令、输出、错误及 E0-E4 证据等级；Reviewer 抽查至少一个可复现实验或受限记�?
- [ ] 3.3 member（Reviewer: lead）形成阶段性建议，明确“可进入 PoC”“继续观察”“暂不采用”及其依据，不强制本窗口选出唯一后端，也不把候选项目指定为新系统代码基线；�?lead 检查建议与证据等级是否一�?

## 4. 交叉复核与需求收�?

- [ ] 4.1 member（Reviewer: lead）复核工具报告中的电气语义、数据接口和 EV 场景适配判断，在对应 PR 中给出逐条意见；lead 确认意见已处理或转为 Issue
- [ ] 4.2 member（Reviewer: lead）复�?V2Sim 运行记录的环境完整性、命令可复现性和证据等级，在对应 PR 中给出逐条意见；lead 确认意见已处理或转为 Issue
- [ ] 4.3 lead（Reviewer: member）把调研结论�?`docs/deliverables/软件需求分析报�?md`、`docs/deliverables/典型场景-业务需�?孪智功能映射�?md` 对照，记录需要进入下一�?OpenSpec 的接口、数据模型和 PoC 问题；通过文档链接逐项追踪

## 5. 集成、文档归并与验收

- [ ] 5.1 lead（Reviewer: member）运�?`openspec validate assess-grid-simulation-backends`、`git diff --check` 及报告链接检查，并把命令与结果写�?PR；所有检查通过或有明确的受限说�?
- [ ] 5.2 lead（Reviewer: member）将本轮可执行结论拆成下一阶段 PoC、接口或数据模型 OpenSpec change/Issue；逐项确认来源可回链到两份调研成果
- [ ] 5.3 lead（Reviewer: member）按“证据充分、结论不过度、后续问题可追踪”完成验收；未达到高证据等级的项目允许作为阶段稿合入，但必须转为下一成果窗口�?Issue
