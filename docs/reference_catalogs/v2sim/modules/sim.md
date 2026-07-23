# sim/ — 交通仿真模块

> 复核状态：人工复核 [reviewed]

## 模块结构

- `sim/base.py` — 仿真基类与配置
- `sim/uxworld.py` — UXsim 交通仿真封装（中观）
- `sim/uxsim/uxsim.py` — UXsim 引擎核心（vendored）
- `sim/tlog.py` — 行程日志记录
- `sim/utils.py` — 仿真工具函数

## 核心类

| 符号 | 文件 | 功能 | 说明 |
|------|------|------|------|
| TrafficInst | base.py | 交通仿真实例基类 | 定义 step/start/stop 接口 |
| SUMOConfig | base.py | SUMO 配置 | SUMO 后端参数 |
| UXsimConfig | base.py | UXsim 配置 | UXsim 后端参数 |
| CommonConfig | base.py | 通用仿真配置 | 时间步长、车辆数等 |
| TimeConfig | utils.py | 时间配置 | 开始/结束/步长 |
| CaseData | utils.py | 案例数据容器 | 加载案例所有配置文件 |
| TripLogger | tlog.py | 行程记录器 | 记录车辆出行事件 |
| TripsLogger | tlog.py | 多车行程记录器 | 管理所有车辆行程 |

## 场景加载流程

1. `CaseData` 从案例目录加载所有 XML 配置
2. `V2SimInstance.from_case_data()` 根据配置选择 UXsim 或 SUMO 后端
3. 创建 `TrafficInst` 实例管理交通仿真
4. 每个 `step()` 推进交通状态并触发车辆事件

## 时间推进

| 方法 | 所属 | 功能 |
|------|------|------|
| step() | TrafficInst | 推进一个交通仿真步 |
| get_vehicles_at() | TrafficInst | 获取某位置的车辆 |
| update_vehicle_positions() | TrafficInst | 更新所有车辆位置 |
