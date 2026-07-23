# plugins/ — 插件系统（含配电网）

> 复核状态：人工复核 [reviewed]

## 模块结构

- `plugins/base.py` — 插件基类与管理器

## 核心类

| 符号 | 功能 | 说明 |
|------|------|------|
| PluginBase | 插件基类 | 定义 on_step/on_start/on_stop 接口 |
| PluginMan | 插件管理器 | 加载、注册和调度插件 |
| StepCallback | 步骤回调 | 每步仿真后执行的钩子 |

## 配电网插件 (pdn)

V2Sim 通过插件机制加载配电网计算，使用 FPowerKit 包实现。

| 功能 | 说明 |
|------|------|
| 潮流计算 | LinDistFlow 线性化潮流（FPowerKit 提供） |
| 输入 | 充电站负荷（从 hub 模块获取） |
| 输出 | bus.csv（母线电压）、line.csv（线路潮流） |
| 配置 | `*.plg.xml` 中定义启用的插件 |

## 插件生命周期

```
仿真开始 → plugin.on_start()
  每步:  → plugin.on_step(sim_time, traffic, hubs)
仿真结束 → plugin.on_stop()
```

## 已知插件

| 插件名 | 功能 | 依赖包 |
|--------|------|--------|
| pdn | 配电网潮流计算 | fpowerkit |
