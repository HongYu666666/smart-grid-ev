# EV 场景实体关系图

> 版本：v0.1 experimental | 场景：EV 承载力提升 | 数据来源：`run-record.schema.json`, `module-manifest.json`
>
> 覆盖 Run、Scenario、Grid、EVFleet、ChargingGroup、Mapping、Snapshot、Action、Decision、Event、Error、Evidence、Module、Capability。

```mermaid
erDiagram
  Run ||--o{ Snapshot : "produces"
  Run ||--|| Scenario : "executes"
  Run ||--o{ Event : "records"
  Run ||--o{ Evidence : "archives"
  Run }|--|| Module : "assembled_by"

  Scenario ||--o{ Grid : "defines"
  Scenario ||--o{ EVFleet : "defines"
  Scenario ||--o{ ChargingGroup : "defines"
  Scenario ||--o{ Mapping : "establishes"

  Snapshot ||--|| Grid : "contains"
  Snapshot ||--|| EVFleet : "contains"
  Snapshot ||--|| ChargingGroup : "contains"
  Snapshot ||--o{ Action : "triggers"

  Action ||--|| Decision : "evaluated_by"
  Action }o--|| Snapshot : "references (snapshot_version)"

  Decision ||--o{ Event : "produces"
  Decision ||--o{ Error : "may_produce"

  Event }o--|| Evidence : "recorded_in"
  Error }o--|| Evidence : "recorded_in"

  Module ||--o{ Capability : "provides"
  Module }o--o{ Capability : "consumes"

  Grid ||--o{ Mapping : "mapped_to (charging/load)"
  ChargingGroup ||--o{ Mapping : "mapped_to (grid_node)"
  EVFleet ||--o{ Mapping : "mapped_to (road/station)"

  %% ===== 实体属性 =====
  Run {
    string run_id PK "稳定运行标识"
    string scenario_id FK "场景引用"
    string scenario_version "场景版本"
    int step_index "当前步骤"
    int step_seconds "步长(秒)"
    int random_seed "随机种子"
    string schema_version "合同版本 0.x"
    string status "accepted|rejected|failed|degraded"
  }

  Scenario {
    string scenario_id PK "场景标识"
    string scenario_version "场景版本"
    string source_kind "demo/synthetic"
    string input_sha256 "输入哈希"
  }

  Grid {
    string grid_id PK "配网标识"
    float capacity_kw "容量(kW)"
    float base_load_kw "基础负荷(kW)"
    float total_load_kw "总负荷(kW)"
    float headroom_kw "剩余容量(kW)"
  }

  EVFleet {
    string ev_fleet_id PK "EV 车队标识"
    float ev_load_kw "当前 EV 负荷(kW)"
    float target_ev_load_kw "目标 EV 负荷(kW)"
  }

  ChargingGroup {
    string charging_group_id PK "充电组标识"
    string mapping_version "映射版本"
  }

  Mapping {
    string source_id FK "源端对象 ID"
    string target_id FK "目标端对象 ID"
    string source_type "源端类型"
    string target_type "目标端类型"
    string mapping_version "映射版本"
    string valid_from "有效起始"
  }

  Snapshot {
    string version PK "快照版本哈希"
    int step_index "对应步骤"
    string run_id FK "所属运行"
  }

  Action {
    string action_id PK "动作标识"
    string action_type "set_ev_aggregate_load"
    string target_id FK "目标对象"
    string proposer "提议者"
    string snapshot_version FK "依据快照"
    string lifecycle "proposed→accepted→executed | proposed→rejected"
  }

  Decision {
    string rule_id "illustrative_grid_capacity_gate.v0"
    string outcome "accepted|rejected|not_evaluated"
    string reason_code "原因码"
    string message "可读消息"
    bool safe_state "安全状态"
  }

  Event {
    string event_id PK "事件标识"
    string event_type "状态变更类型"
    string before_version FK "变更前快照"
    string after_version FK "变更后快照"
  }

  Error {
    string code "错误码"
    string field "定位字段"
    string message "错误消息"
    bool retryable "可重试"
    bool safe_state "安全状态"
  }

  Evidence {
    string evidence_id PK "证据标识"
    string kind "evidence 类型"
    string sha256 "内容哈希"
  }

  Module {
    string module_id PK "模块标识"
    string responsibility "系统责任"
    string kind "reusable_core|replaceable_domain|replaceable_adapter"
    string status "demo_bound|planned|unavailable|not_applicable"
  }

  Capability {
    string capability_id PK "能力标识"
    string owner_module FK "所有者模块"
    string status "demo_bound|planned|unavailable"
  }
```

## 实体说明

| 实体 | 唯一标识 | 所有者模块 | 来源 |
|------|---------|-----------|------|
| Run | `run_id` | scenario-manager | run-record.schema.json |
| Scenario | `scenario_id` + `scenario_version` | scenario-manager | run-record.schema.json |
| Grid | `grid_id` | grid-twin | field_group `grid` |
| EVFleet | `ev_fleet_id` | ev-traffic-twin | field_group `ev-traffic` |
| ChargingGroup | `charging_group_id` | charging-twin | field_group `charging` |
| Mapping | `source_id` + `target_id` + `mapping_version` | object-registry | field_group `charging` + 跨域映射 |
| Snapshot | `version` (哈希) | runtime-orchestrator | run-record `snapshots` |
| Action | `action_id` | proposal-gateway | field_group `action` |
| Decision | 内嵌于 Action 结果 | safety-transaction | field_group `safety-and-commit` |
| Event | `event_id` (隐含) | evidence-storage | run-record `evidence` |
| Error | 内嵌于运行结果 | 各生产者 | run-record `errors` |
| Evidence | `evidence_id` | evidence-storage | run-record `evidence` |
| Module | `module_id` | contract-registry | module-manifest.json |
| Capability | `capability_id` | contract-registry | module-manifest `provides`/`consumes` |

## 追踪

- Action 可回查 Snapshot（`snapshot_version`）、目标对象（`target_id`）和 Decision
- Decision 可回查 Event/Error 和 Evidence
- Evidence 包含 `sha256` 用于可复现校验
- 其他场景（如分布式新能源）实体标记为 `planned`，本图不展开未批准字段
