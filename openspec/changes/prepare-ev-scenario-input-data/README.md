# prepare-ev-scenario-input-data

电动汽车承载力提升单场景的数据准备/场景输入模块级 OpenSpec change。

- 上层合同：`openspec/specs/unified-ev-grid-data-model/spec.md`（已接受）
- 上层需求：`docs/deliverables/软件需求分析报告.md` 的 `REQ-EV-001`、`REQ-EV-008`、`REQ-EV-009`
- 来源移交：归档 change `2026-07-31-define-unified-ev-grid-data-model` 的 tasks 4.1／4.2，对应 Issue #19
- 负责人：`member`；Reviewer：`lead`
- 模块定位：`object-registry` 的输入准备子责任（lead 裁定），不是新增第 15 个顶层系统模块

本 change 只定义模块外部行为、字段级契约、校验规则、结构化错误和验收方式，不实现运行时代码，也不选择最终配电网生产内核。后续可提议 `validated-scenario-input` 等能力名称，但不得静默修改 #23 manifest。

`ev_charging_v1/`、V2Sim 和 pandapower 只作为参考资产与来源登记对象，不构成新系统输入格式或实现状态。
