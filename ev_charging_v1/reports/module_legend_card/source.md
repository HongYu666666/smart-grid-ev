# 图例卡可编辑来源说明

对应文件：`legend_card.html`
对应 Issue：#24（辅助任务，Reviewer：lead；整合决定：HongYu）
对应上层制图 Issue：#26 / `document-ev-scenario-architecture-views`
权威来源分支：`origin/openspec/23-runnable-simulation-dashboard`（尚未合并 main）

## 1. 模块类别 → 归属（不改名、不新增）

来源：`experiments/architecture_proof/module-manifest.json` 的 `modules[].kind`

| kind | 模块 id |
| --- | --- |
| reusable_core | scenario-manager, object-registry, contract-registry, clock-scheduler, runtime-orchestrator, proposal-gateway, safety-transaction, evidence-storage, evaluation, review-replay |
| replaceable_domain | grid-twin, ev-traffic-twin, charging-twin |
| replaceable_adapter | external-adapters |

三类命名逐字取自 manifest，卡片里的边框符号（实线/虚线/点线）是本卡新提议的视觉建议，未见于任何既有文档或页面，HongYu 可自行更换。

## 2. 能力状态 → 配色（复用既有约定，未新造）

来源：`experiments/architecture_proof/architecture_proof/render.py` 中 `.pill` 系列 CSS 类（该页面已实现并冻结）

| status | 背景色 | 文字色 | 对应 render.py 已有 class |
| --- | --- | --- | --- |
| demo_bound | #d9f0e6 | #147a56 | `.demo_bound`（与 `.accepted` 同色） |
| planned | #e1e8f2 | #315b8a | `.planned`（与 `.important` 同色） |
| unavailable | #f4e7ce | #a66a12 | `.unavailable`（与 `.failed` 同色） |
| not_applicable | #e8e5dd | #615f59 | `.not_applicable` |

状态定义文字逐字引自 `docs/deliverables/仿真系统总体架构设计说明书.md` 第 168-171 行。

## 3. 页脚/角标措辞来源

| 角标 | 措辞来源 |
| --- | --- |
| `v0.1 · EXPERIMENTAL` | `experiments/architecture_proof/architecture_proof/render.py` 页头 `.stamp` 文案 |
| `demo / synthetic 输入` | `experiments/architecture_proof/frozen_demo/README.md`：“本目录…从固定 `demo/synthetic` 输入生成” |
| `来源：module-manifest.json v0.1.0` | 本卡新提议的引用角标格式，用于让每张图可回溯到具体 manifest 版本 |

## 4. 明确未做的事（对齐 Issue #24 约束）

- 未绘制模块之间的依赖/数据流箭头（`depends_on` / `provides` / `consumes` 关系留给 #26 的关键图）。
- 未新增模块、能力、字段或完成状态；三类 kind 和四类 status 均为 manifest 已有枚举的完整集合，没有裁剪也没有扩充。
- 未修改 `module-manifest.json`、`module-manifest.schema.json`、OpenSpec 文件或任何运行时代码，只新增了 `reports/module_legend_card/` 下两个只读文件。
