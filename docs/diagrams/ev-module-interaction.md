# EV 场景模块交互图

> 版本：v0.1 experimental | 场景：EV 承载力提升 | 数据来源：`module-manifest.json`
>
> 制图不重新设计公共合同；仅对已批准架构的视觉表达。

```mermaid
flowchart TB
  %% ===== 样式分类 =====
  classDef core fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
  classDef domain fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
  classDef adapter fill:#fff3e0,stroke:#e65100,stroke-width:2px,stroke-dasharray:5 5
  classDef planned fill:#f3e5f5,stroke:#6a1b9a,stroke-width:1px,stroke-dasharray:3 3

  %% ===== 可复用核心责任 (1—4, 8—10, 12—14) =====
  SM["1. 场景与实验管理<br/><small>provides: run-context</small><br/><small>status: demo_bound</small>"]:::core
  OR["2. 数据接入与公共对象注册<br/><small>provides: object-identity,<br/>unit-registry, cross-domain-mapping</small><br/><small>status: demo_bound</small>"]:::core
  MR["3. 模块、能力与 Schema 注册<br/><small>provides: contract-registry,<br/>capability-registry</small><br/><small>status: demo_bound</small>"]:::core
  CL["4. 统一时钟与事件调度<br/><small>provides: simulation-clock,<br/>event-ordering</small><br/><small>status: demo_bound</small>"]:::core
  RT["8. 快照与运行编排<br/><small>provides: state-snapshot,<br/>staged-step</small><br/><small>status: demo_bound</small>"]:::core
  PG["9. 动作提议网关<br/><small>provides: action-proposal</small><br/><small>status: demo_bound</small>"]:::core
  ST["10. 安全与事务协调<br/><small>provides: action-validation,<br/>unified-commit</small><br/><small>status: demo_bound</small>"]:::core
  ES["12. 状态、事件与证据存储<br/><small>provides: snapshot-store,<br/>event-store, evidence-store</small><br/><small>status: demo_bound</small>"]:::core
  ME["13. 指标与架构评估<br/><small>provides: architecture-checks,<br/>run-metrics</small><br/><small>status: demo_bound</small>"]:::core
  RV["14. 回放与网页评审<br/><small>provides: read-only-review</small><br/><small>status: demo_bound</small>"]:::core

  %% ===== 可替换领域责任 (5—7) =====
  GT["5. 配网数字孪生<br/><small>provides: grid-facts,<br/>grid-constraints</small><br/><small>status: demo_bound</small>"]:::domain
  ET["6. EV/交通数字孪生<br/><small>provides: ev-facts</small><br/><small>status: demo_bound</small>"]:::domain
  CT["7. 充电设施数字孪生<br/><small>provides: charging-facts</small><br/><small>status: demo_bound</small>"]:::domain

  %% ===== 可替换适配器 (11) =====
  AD["11. 配网、交通、方法和存储适配器<br/><small>provides: external-backend-adapter</small><br/><small>status: unavailable</small>"]:::adapter

  %% ===== 依赖关系（consumes / depends_on）=====
  SM -->|run-context| OR
  SM -->|run-context| CL
  OR -->|object-identity, unit-registry| GT
  OR -->|object-identity| ET
  OR -->|object-identity| CT
  CL -->|simulation-clock| GT
  CL -->|simulation-clock| ET
  CL -->|simulation-clock| CT
  SM -->|run-context| RT
  MR -->|capability-registry| RT
  GT -->|grid-facts| RT
  ET -->|ev-facts| RT
  CT -->|charging-facts| RT
  RT -->|state-snapshot| PG
  PG -->|action-proposal| ST
  GT -->|grid-constraints| ST
  RT -->|state-snapshot| ST
  ST -->|unified-commit| ES
  ST -->|unified-commit| GT
  ST -->|unified-commit| ET
  ST -->|unified-commit| CT
  ES -->|evidence-store| ME
  MR -->|capability-registry| ME
  ES -->|snapshot-store, event-store, evidence-store| RV
  ME -->|architecture-checks| RV
  MR -->|contract-registry| AD

  %% ===== 图例 =====
  subgraph Legend["图例"]
    direction LR
    L1["可复用核心"]:::core
    L2["可替换领域"]:::domain
    L3["可替换适配器<br/>(unavailable)"]:::adapter
  end
```

## 说明

- 箭头标注的是**能力名称**（provides → consumes 方向）
- 模块编号与 `module-manifest.json` 一致
- 所有模块当前状态为 `demo_bound`（仅 #11 为 `unavailable`）
- 本图不画成 14 个微服务；边界通过合同和依赖方向保持
