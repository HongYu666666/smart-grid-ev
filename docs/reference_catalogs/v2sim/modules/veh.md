# veh/ — 车辆模型模块

> 复核状态：人工复核 [reviewed]

## 模块结构

- `veh/ev.py` — 电动汽车模型
- `veh/veh.py` — 通用车辆基类

## 核心类

| 符号 | 文件 | 功能 |
|------|------|------|
| EV | ev.py | 电动汽车实体，含 SOC、电池容量、充电状态 |
| GV | veh.py | 普通燃油车实体 |
| Vehicle | veh.py | 车辆基类 |
| SV | veh.py | 特殊车辆 |
| VehStatus | veh.py | 车辆状态枚举（行驶/充电/空闲等） |
| VehType | veh.py | 车辆类型枚举（EV/GV） |
| Trip | veh.py | 出行事件 |
| OwnerGroup | veh.py | 车辆所有者分组 |

## EV 关键属性与方法

| 属性/方法 | 功能 | 说明 |
|----------|------|------|
| soc | 当前 SOC (0-1) | 电池状态 |
| battery_capacity | 电池容量 (kWh) | 固定属性 |
| update_soc() | 更新 SOC | 充电/行驶后调用 |
| consume_energy() | 消耗能量（行驶） | SOC 下降 |
| charge() | 充电 | SOC 上升 |
| is_need_charge() | 是否需要充电 | SOC 阈值判断 |
