# pandapower 核心符号人工复核记录

本记录对应 pandapower `v3.5.4`（commit `be3f13b6db3632fe690f997654d15c9173a14839`）。复核目标不是证明新系统已实现，而是确认首轮 PoC 会直接调用的状态对象、建模入口、求解入口、控制/时序循环、结果清理和错误边界。

## 复核范围

| 类别 | 已逐项复核符号 | PoC 边界结论 |
| --- | --- | --- |
| 网络对象 | `pandapowerNet` | 可变 DataFrame 容器；适配器不得把其内部表直接暴露为新系统统一模型 |
| 模型创建 | `create_empty_network`、`create_bus`、`create_ext_grid`、`create_line`、`create_line_from_parameters`、`create_load` | 工厂函数会修改 `net` 并返回索引；数据适配器必须统一单位、索引和必填电气参数 |
| 求解 | `runpp`、`rundcpp`、`runpp_3ph`、选项构造、`pd2ppc`、`_powerflow`、Newton-Raphson 及母线/支路结果回写入口 | 首轮使用 `runpp`；直流潮流不能替代电压/无功安全校核；三相入口留作参数完整后的下一 PoC |
| 控制 | `prepare_run_ctrl`、初始化/计算/修复/迭代/收尾入口、`run_control` | 控制器按 level/order 迭代并触发重算；智能体动作仍须先经过新系统安全校验 |
| 时序 | `init_time_series`、`cleanup`、单步/输出入口、`run_loop`、`run_timeseries` | 可支撑准静态时间步，但连续运行、回放和事件时标需要新系统外层编排与证据 |
| 结果 | `reset_results`、`verify_results` | 每次实验前必须清理结果；写回前检查元件/结果索引一致性 |
| 错误 | `ppException`、`LoadflowNotConverged`、`AlgorithmUnknown` | 统一转换为结构化后端错误；`AlgorithmUnknown` 的类名与源码说明不一致，暂不做确定映射 |

逐符号人工摘要已写入 `manual_review_summaries.tsv`，生成器将这些摘要写入 `symbols.csv` 和对应模块页，并把 `review_status` 标为“人工复核”。

## 模块抽检

对 `build_branch`、`build_bus`、`convert_format`、`diagnostic`、`file_io`、`toolbox.grid_modification`、`topology.create_graph` 的全部目录行执行字段完整性抽检。抽检只确认限定名、签名、源码锚点、非空摘要和静态依赖可追踪，不把运行行为升级为 E2/E3。
