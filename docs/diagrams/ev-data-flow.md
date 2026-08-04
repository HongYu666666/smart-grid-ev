# EV 场景数据流图

> 版本：v0.1 experimental | 场景：EV 承载力提升 | 数据来源：`run-accepted.json`, `run-rejected.json`
>
> 覆盖 accepted、rejected、degraded 三类路径。

```mermaid
flowchart TD
  %% ===== 样式 =====
  classDef input fill:#e8eaf6,stroke:#283593
  classDef process fill:#e3f2fd,stroke:#1565c0
  classDef decision fill:#fff9c4,stroke:#f9a825,stroke-width:2px
  classDef accepted fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
  classDef rejected fill:#ffcdd2,stroke:#c62828,stroke-width:2px
  classDef degraded fill:#fff3e0,stroke:#e65100,stroke-width:2px
  classDef output fill:#f3e5f5,stroke:#6a1b9a

  %% ===== 输入 =====
  IN["demo/synthetic 输入包<br/><small>source.kind: demo/synthetic<br/>input_sha256: 固定哈希</small>"]:::input

  %% ===== 对象注册与校验 =====
  REG["对象注册与输入校验<br/><small>schema_version ✓<br/>identity ✓ | unit ✓ | mapping ✓</small>"]:::process

  %% ===== 步骤 0 快照 =====
  SNAP0["步骤 0 只读快照<br/><small>grid: capacity=1000kW, base_load=880kW<br/>ev: ev_load=0kW<br/>charging: mapping_version=v1</small>"]:::process

  %% ===== 动作提议 =====
  PROP["动作提议网关<br/><small>action_type: set_ev_aggregate_load<br/>proposer: rule/ev_capacity_gate<br/>snapshot_version: step-0-xxx</small>"]:::process

  %% ===== 合同/容量校验 =====
  CHECK{"合同校验 + 容量门槛<br/><small>base_load + target_ev_load<br/>≤ grid_capacity ?</small>"}:::decision

  %% ===== Accepted 路径 =====
  ACCEPT["统一提交（accepted）<br/><small>target_ev_load=120kW<br/>total_load=1000kW, headroom=0kW<br/>lifecycle: proposed→accepted→<br/>executing→executed</small>"]:::accepted

  %% ===== Rejected 路径 =====
  REJECT["拒绝（rejected）<br/><small>target_ev_load=200kW → total=1080kW<br/>reason: capacity_exceeded<br/>lifecycle: proposed→rejected<br/>事实不变，步骤 1 = 步骤 0</small>"]:::rejected

  %% ===== Failed 路径（非法输入）=====
  FAIL["失败（failed）<br/><small>输入含负负荷或缺字段<br/>error: {code, field, message,<br/>retryable, safe_state}<br/>不生成已执行动作</small>"]:::rejected

  %% ===== Degraded 路径 =====
  DEGRADE["降级（degraded）<br/><small>可选模块 unavailable<br/>核心链路仍完成<br/>capability_status 标记差距</small>"]:::degraded

  %% ===== 事件/证据 =====
  EVID["事件与证据存储<br/><small>evidence_id + sha256<br/>前后版本 + 决策原因</small>"]:::output

  %% ===== 网页投影 =====
  WEB["只读网页评审<br/><small>四视图投影 JSON<br/>不新增业务计算</small>"]:::output

  %% ===== 连线 =====
  IN --> REG
  REG -->|校验通过| SNAP0
  REG -->|"schema/identity/unit 错误"| FAIL
  SNAP0 --> PROP
  PROP --> CHECK

  CHECK -->|"≤ capacity"| ACCEPT
  CHECK -->|"> capacity"| REJECT
  CHECK -.->|"可选模块不可用"| DEGRADE

  ACCEPT --> EVID
  REJECT --> EVID
  FAIL --> EVID
  DEGRADE --> EVID
  EVID --> WEB
```

## 路径说明

| 路径 | 触发条件 | 步骤 1 事实 | 运行状态 |
|------|---------|------------|---------|
| accepted | `base_load + target_ev_load ≤ capacity` | 提交新负荷 | `accepted` |
| rejected | `base_load + target_ev_load > capacity` | 与步骤 0 相同 | `rejected` |
| failed | 输入非法（负负荷、缺字段、schema 不兼容） | 无快照生成 | `failed` |
| degraded | 可选模块 `unavailable`，核心链路可继续 | 标记差距后提交 | `degraded` |

## 字段来源

所有图中字段均可回链到 `schemas/run-record.schema.json` 和 `module-manifest.json`：
- `capacity_kw`, `base_load_kw`, `total_load_kw`, `headroom_kw` → field_group `grid`
- `ev_load_kw`, `target_ev_load_kw` → field_group `ev-traffic`
- `action_type`, `lifecycle`, `parameters` → field_group `action`
- `rule_id`, `outcome`, `reason_code` → field_group `safety-and-commit`
