# core.py — 核心仿真引擎

> 复核状态：人工复核 [reviewed]

## 主要类

| 符号 | 类型 | 功能 | 输入 | 输出 | 依赖 |
|------|------|------|------|------|------|
| V2SimInstance | class | 仿真主实例，管理整个仿真生命周期 | out_dir, traffic, plugins, stats | 仿真结果 | TrafficInst, PluginMan, StaWriter |
| ClientOptions | class | 客户端选项配置 | — | — | — |
| SaveStateOptions | class(Enum) | 保存状态选项（Skip/Save） | — | — | — |
| LoadStateOption | class(Enum) | 加载状态选项（Skip/Load） | — | — | — |

## 核心方法 (V2SimInstance)

| 方法 | 功能 | 输入 | 输出 | 副作用 |
|------|------|------|------|--------|
| simulate() | 一次性完整仿真 | use_signal: bool | (正常结束, TrafficInst, StaWriter) | 运行全部仿真步 |
| start() | 启动仿真（start-step-stop 模式） | — | — | 初始化仿真状态 |
| step() | 执行一步仿真 | — | 当前仿真时间(int) | 推进一个时间步 |
| step_until(t) | 仿真推进到时间 t | t: int | 当前仿真时间 | 推进多步 |
| stop() | 停止仿真 | save_state_to | — | 清理资源 |
| save(folder) | 保存当前仿真状态 | folder: Path | — | 写入状态文件 |
| from_case_data() | 从案例数据创建实例 (静态工厂方法) | CaseData, 配置参数 | V2SimInstance | — |

## 辅助函数

| 函数 | 功能 | 用途 |
|------|------|------|
| simulate_single() | 单次仿真的完整封装 | 命令行入口调用 |
| create_output_directory() | 创建输出目录 | 仿真前准备 |
| create_pools() | 创建资源池 | 充电分配策略池 |
| get_sim_params() | 获取仿真参数 | 配置解析 |
| get_internal_components() | 获取内部组件 | 组件装配 |
| load_external_components() | 加载外部组件 | 插件加载 |
| find_latest_results_folder() | 查找最新结果目录 | 结果查看 |
