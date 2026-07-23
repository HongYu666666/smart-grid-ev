# V2Sim 典型案例运行记录

## 文档信息

| 项目 | 内容 |
| --- | --- |
| OpenSpec change | `assess-grid-simulation-backends` |
| GitHub Issue | `#8` |
| 对应任务 | `2.1`—`2.6` |
| 代表性案例 | `v2sim/cases/ux_12nodes/` |
| 负责人 | `member` |
| Reviewer | `lead` |
| 当前状态 | 环境探测完成，案例尚未运行 |
| 当前证据等级 | `E1`；E2 导入受依赖阻塞 |
| 更新日期 | 2026-07-23 |

本记录只证明 V2Sim 参考项目在指定环境中的资料、导入或运行状态，不构成新系统实现证据，也不把 V2Sim 指定为新系统代码基线或唯一主仿真内核。

本成果还必须在 `docs/reference_catalogs/v2sim/` 建立固定版本 V2Sim 的完整函数、类和方法目录，供后续新系统设计和适配时检索。全量目录由工具生成，核心开发链路逐项人工复核，其余模块按模块抽检；本报告不重复粘贴逐符号内容。

## 1. 案例选择

选择 `v2sim/cases/ux_12nodes/`，原因如下：

- 仓库已包含完整案例配置文件；
- 使用仓库内置的 UXsim 路线，避免把 SUMO 外部程序作为第一步前置条件；
- 案例声明同时包含交通、车辆、快/慢充、配网与统计配置，适合梳理输入输出边界；
- 规模较小，适合作为 E3 最小案例，不代表新系统固定规模。

## 2. 仓库输入

### 2.1 快照信息

| 字段 | 当前值 |
| --- | --- |
| 项目仓库提交 | `a92432a` |
| V2Sim 源码路径 | `v2sim/` |
| 源码声明版本 | `1.5.0b2`，来自 `v2sim/pyproject.toml` 与 `v2sim/v2sim/__init__.py` |
| Python 要求 | `>=3.9` |
| 许可证声明 | BSD-3-Clause，待与正式评估版本官方 LICENSE 复核 |

### 2.2 案例文件

| 文件 | 作用 | 当前核查 |
| --- | --- | --- |
| `preference.v2simcfg` | 时间、随机种子、交通步长、统计项等统一配置 | 已读取 |
| `ux_12nodes.net.xml` | UXsim 交通网络 | 文件存在，语义待运行核查 |
| `ux_12nodes.plg.xml` | 插件配置 | 文件存在，插件依赖待核查 |
| `ux_12nodes.grid.xml` | 配网配置 | 文件存在，FPowerKit 边界待核查 |
| `ux_12nodes.fcs.xml` | 快充站配置 | 文件存在 |
| `ux_12nodes.scs.xml` | 慢充站配置 | 文件存在 |
| `ux_12nodes.gs.xml` | 加油站配置 | 文件存在 |
| `node_type.txt` | 节点类型配置 | 文件存在 |

当前案例目录未发现车辆/行程输入文件。Reviewer 在实际运行前必须确认是由命令生成、由保存状态提供，还是仓库快照不完整；不得把“案例文件存在”写成“案例已运行”。

### 2.3 配置摘要

| 配置项 | 当前值 |
| --- | --- |
| `start_time` | `0` |
| `end_time` | `172800` 秒 |
| `traffic_step` | `10` 秒 |
| `seed` | `0` |
| `routing_method` | `astar` |
| `visualize` | `false` |
| `stats` | `fcs`、`scs`、`gs`、`gen`、`bus`、`line`、`utn` |

以上只说明配置意图。输出是否实际产生、字段是否完整以及结果是否合理，必须由 E3 运行证据确认。

## 3. 当前环境

| 字段 | 当前值 |
| --- | --- |
| 操作系统 | Linux（具体发行版待 member 补充） |
| Python | `3.13.12` |
| 隔离环境 | 尚未创建 |
| 本地源码导入方式 | `PYTHONPATH=v2sim` |
| 当前导入结果 | 失败 |
| 首个阻塞依赖 | `feasytools` |
| 其他已探测缺失 | `fpowerkit`、`scipy`；完整依赖仍需在隔离环境核查 |

### 3.1 已执行命令

```text
PYTHONPATH=v2sim python -c "import v2sim; print(v2sim.__file__); print(v2sim.__version__)"
```

### 3.2 实际结果

```text
ModuleNotFoundError: No module named 'feasytools'
```

结论：当前证据达到 `E1`，尚未达到 `E2`。该结果只说明当前 Python 环境依赖不完整，不说明 V2Sim 不可安装或不支持该案例。

## 4. 隔离环境准备步骤

以下为待执行方案，执行前后必须记录实际版本和输出：

1. 在临时目录创建独立 Python 环境，不修改新系统正式依赖；
2. 优先选择与 V2Sim 依赖兼容的 Python 版本；若 Python 3.13 安装失败，应记录失败并改用项目支持范围内的稳定版本；
3. 从仓库快照安装 V2Sim 及所需依赖；
4. 执行版本和导入检查；
5. 核查或生成 `ux_12nodes` 所需车辆/行程输入；
6. 使用命令行运行案例，将结果输出到独立临时目录；
7. 检查声明的 `fcs/scs/gs/gen/bus/line/utn` 输出及时间范围；
8. 保存命令、关键输出、运行时间、错误摘要和环境清单。

拟执行的最小命令形式：

```text
python -m v2sim.app.sim_single \
  -d <仓库绝对路径>/v2sim/cases/ux_12nodes \
  -o <临时输出目录> \
  -b 0 -e 172800 -l 10 \
  --seed 0
```

命令依据来自 `v2sim/v2sim/app/sim_single.py` 与 `v2sim/v2sim/wrapper.py`。实际运行前必须通过版本帮助或源码再次确认参数，不得把拟执行命令记录成已执行命令。

## 5. E3 运行证据模板

| 字段 | 待填写 |
| --- | --- |
| environment |  |
| python_version |  |
| v2sim_version |  |
| dependency_versions |  |
| input_case | `v2sim/cases/ux_12nodes/` |
| vehicle_trip_input |  |
| command |  |
| output_directory |  |
| started_at |  |
| finished_at |  |
| duration |  |
| exit_status |  |
| key_output |  |
| result_check |  |
| evidence_level |  |
| limitations |  |

## 6. 输入输出与能力边界

| 能力 | V2Sim 可提供的参考 | 新系统仍需负责 |
| --- | --- | --- |
| 交通 | UXsim/SUMO 路线、路网、车辆移动和路径相关能力，待 E3 核实 | 统一场景时钟、数据合同、跨域对象映射和验收 |
| EV | 车辆、行程、SOC 和行为模型线索，待 E3 核实 | 新系统对象模型、状态校验、事件合同和证据 |
| 充电/V2G | 快慢充站、充电过程、负荷和 V2G 插件线索，待 E3 核实 | 动作提案、安全校验、执行/拒绝/回退和业务指标 |
| 配电网 | FPowerKit 插件与 bus/line 统计线索，待 E3 核实 | 主仿真内核选型、统一适配器、精度与工程校核 |
| 编排 | V2Sim 自身案例运行和插件机制 | 新系统 Python 编排层、孪智交互、版本和实验管理 |
| 结果 | 案例统计与输出格式线索 | 新系统指标口径、原始证据、需求追踪、回放和归档 |

V2Sim 案例运行成功只能提高 V2Sim 参考项目的证据等级，不得把 `REQ-EV-*` 的新系统状态改为“部分具备”或“已验证”。

## 7. Reviewer 核查清单

- [ ] 环境、Python、V2Sim 与关键依赖版本完整；
- [ ] 输入案例与车辆/行程来源可定位；
- [ ] 完整命令可复制，输出写入独立目录；
- [ ] 运行时间、退出状态和关键输出已记录；
- [ ] 输出文件存在且内容、时间范围和单位经过检查；
- [ ] 失败没有被写成项目能力不足；
- [ ] V2Sim、配网主内核和新系统 Python 编排层边界清晰；
- [ ] 参考证据没有计入新系统完成度。
- [ ] `docs/reference_catalogs/v2sim/` 覆盖全量生产源码符号，功能说明非空且复核状态明确；
- [ ] 场景加载、时间推进、车辆/交通、充电、配网插件、控制和结果输出核心模块已逐项人工复核。
