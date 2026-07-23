# hub/ — 充电站管理模块

> 复核状态：人工复核 [reviewed]

## 模块结构

- `hub/hub.py` — 充电站管理中心
- `hub/cs.py` — 充电站类（单站）
- `hub/s.py` — 电价与服务策略

## 核心类

| 符号 | 文件 | 功能 |
|------|------|------|
| CSHub | hub.py | 充电站集合管理器，管理所有充电站 |
| FCSHub | hub.py | 快充站集合 |
| SCSHub | hub.py | 慢充站集合 |
| GSHub | hub.py | 加油站集合 |
| MixedHub | hub.py | 混合站集合 |
| StationHub | hub.py | 站点中心基类 |
| CS | cs.py | 单个充电站实例 |
| BiCS | cs.py | 双向充电站（V2G） |
| UniCS | cs.py | 单向充电站 |
| BaseStation | cs.py | 站点基类 |
| AllocEnv | cs.py | 充电分配环境 |
| PriceGetter | s.py | 电价获取器基类 |
| ConstPriceGetter | s.py | 固定电价 |
| ToUPriceGetter | s.py | 分时电价 |
| ToUSoCPriceGetter | s.py | 基于 SOC 的分时电价 |

## 充电过程

| 方法 | 所属 | 功能 | 输入 | 输出 |
|------|------|------|------|------|
| allocate() | CS | 为到达车辆分配充电桩 | EV, 时间 | 分配结果 |
| charge_step() | CS | 执行一步充电计算 | — | 充电功率 |
| release() | CS | 释放充电桩 | EV | — |
| get_queue_length() | CS | 获取排队长度 | — | int |
| get_load() | CS | 获取当前负荷 | — | float(kW) |

## 控制动作

| 方法 | 功能 | V2G 相关 |
|------|------|---------|
| v2g_discharge() | V2G 放电 | 是 |
| set_max_power() | 设置最大充电功率 | 功率调节 |
| set_price() | 设置充电电价 | 电价控制 |
