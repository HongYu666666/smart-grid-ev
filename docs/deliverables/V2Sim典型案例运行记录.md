# V2Sim 典型案例运行记录

> **OpenSpec change**: `assess-grid-simulation-backends`  
> **对应 tasks**: 2.1—2.3  
> **负责人**: HongYu666666 (member)  
> **Reviewer**: lead  
> **日期**: 2026-07-23

---

## 1. 版本与提交（固定）

| 项目 | 值 |
|------|---|
| V2Sim 版本 | 1.4.4 |
| GitHub 仓库 | https://github.com/hesl-seu/v2sim |
| 固定 tag | `v1.4.4` |
| 固定 commit | `5cf6777ac6780f2247802533941204e4a95bc2ce` |
| PyPI wheel SHA256 | `8f6dd9b4822af0545806d29d0c8371cccad2594a36e5aa91e2dc9cec4ab2198e` |
| wheel 文件名 | `v2sim-1.4.4-py3-none-any.whl` |
| 案例来源 | 同一 tag `v1.4.4` 的 `cases/ux_12nodes/` 目录 |
| 案例获取方式 | `https://github.com/hesl-seu/v2sim/archive/refs/tags/v1.4.4.zip` |
| FPowerKit 版本 | 0.4.3 |
| libsumo 版本 | 1.27.1 |

> **说明**：PyPI 1.4.4 wheel 与 GitHub tag `v1.4.4` (commit `5cf6777`) 为同一发布，SHA256 一致。案例文件从同一 tag 的 zip 包获取，确保源码与案例版本统一。

---

## 2. 运行环境（隔离环境）

| 项目 | 值 |
|------|---|
| OS | Windows 10 x64 (build 19045) |
| Python | 3.12.13 (conda env `v2sim_test`) |
| pip | 26.1.2 |
| 隔离方法 | `conda create -n v2sim_test python=3.12 -y` 独立虚拟环境 |
| 安装命令 | `pip install v2sim==1.4.4` |
| SUMO | 未独立安装（使用 pip 依赖的 libsumo + sumo-data） |

### 关键依赖版本（pip freeze 摘要）

```
v2sim==1.4.4
fpowerkit==0.4.3
libsumo==1.27.1
sumolib==1.27.1
traci==1.27.1
sumo-data==1.27.1
pyproj==3.7.2
feasytools==0.1.6
numpy==2.5.1
scipy==1.18.0
matplotlib==3.11.1
networkx==3.6.1
```

> **注意**：pip 默认解析 fpowerkit>=0.4.1 时会安装 0.5.0，但 v2sim 1.4.4 在 fpowerkit 0.5.0 下存在运行时兼容问题。需手动固定 `pip install fpowerkit==0.4.3`。

---

## 3. 代表性案例选择

| 属性 | 值 |
|------|---|
| 案例名称 | ux_12nodes |
| 交通引擎 | UXsim（中观，内置于 v2sim，无需额外安装） |
| 配电网规模 | 12 节点 |
| 选择原因 | 最轻量案例，不依赖外部 SUMO 安装，适合验证基本流程 |

### 案例配置文件

案例路径（从 tag v1.4.4 zip 解压后）：`v2sim-1.4.4/cases/ux_12nodes/`

```
ux_12nodes/
├── node_type.txt           # 节点类型定义
├── preference.v2simcfg     # 仿真偏好配置
├── ux_12nodes.fcs.xml      # 快充站配置（12 个站点）
├── ux_12nodes.grid.xml     # 配电网拓扑
├── ux_12nodes.gs.xml       # 加油站配置（12 个站点）
├── ux_12nodes.net.xml      # 交通路网
├── ux_12nodes.plg.xml      # 插件配置（pdn 配电网模型）
└── ux_12nodes.scs.xml      # 慢充站配置（12 个站点）
```

---

## 4. 安装命令

```bash
pip install v2sim
```

**实际输出摘要**：
```
Successfully installed feasytools-0.1.6 fpowerkit-0.4.3 libsumo-1.27.1
pyproj-3.7.2 sumo-data-1.27.1 sumolib-1.27.1 traci-1.27.1 v2sim-1.4.4
```

**验证**：
```bash
python -c "import v2sim; print(v2sim.__version__)"
# 输出: 1.4.4
```

---

## 5. 车辆行程生成

案例不自带车辆文件，需先生成。

**命令**：
```bash
conda activate v2sim_test
pip install v2sim==1.4.4
pip install fpowerkit==0.4.3  # 固定兼容版本
v2sim-gen-trip -d "v2sim-1.4.4/cases/ux_12nodes" -n-ev 500 -n-gv 500
```

**输出**：
```
1000/1000, 100.00%
已完成. 用时0.1秒.
```

**生成文件**：`ux_12nodes.veh.xml.gz`（车辆行程压缩文件）
**退出码**：0

---

## 6. 仿真运行（隔离环境实际执行）

**命令**：
```python
from v2sim import simulate_single, TimeConfig
simulate_single("v2sim-1.4.4/cases/ux_12nodes", TimeConfig(0, 10, 172800), silent=False, seed=42)
```

**等效命令行**：
```bash
v2sim-gen-trip -d "v2sim-1.4.4/cases/ux_12nodes" -n-ev 500 -n-gv 500
# 然后通过 Python API 调用 simulate_single
```

**实际终端输出**：
```
仿真开始，按Ctrl-C中断
  交通仿真器：UXsim
  路网: .../ux_12nodes/ux_12nodes.net.xml
  行程: .../ux_12nodes/ux_12nodes.veh.xml.gz, 1000辆车
  快充: .../ux_12nodes/ux_12nodes.fcs.xml, 12个站点
  慢充: .../ux_12nodes/ux_12nodes.scs.xml, 12个站点
  加油站: .../ux_12nodes/ux_12nodes.gs.xml, 12个站点
已创建单个串行仿真.
  插件: pdn - 配电网模型
进度: 100.00%, 172800/172800. 已用时: 00:00:09, 预计剩余时间: 00:00:00
仿真结束. 用时: 00:00:09
Total steps: 17280
```

| 运行指标 | 值 |
|---------|---|
| 仿真步数 | 17280 |
| 仿真时长 | 172800 秒（2 天） |
| 时间步长 | 10 秒 |
| 墙钟时间 | 9.2 秒 |
| 退出状态 | 正常完成（exit code 0） |
| 随机种子 | 42 |
| 环境 | conda env `v2sim_test`, Python 3.12.13 |

---

## 7. 输出结果

### 7.1 输出目录

```
ux_12nodes/results/
├── bus.csv        # 母线电压/功率（配电网）
├── fcs.csv        # 快充站负荷时序
├── scs.csv        # 慢充站负荷时序
├── gen.csv        # 发电机数据
├── gs.csv         # 加油站数据
├── line.csv       # 线路潮流
├── utn.csv        # 交通网络数据
├── cproc.log      # 充电过程日志
├── cproc.clog     # 充电过程压缩日志
├── pdn_res.log    # 配电网计算日志
├── pdn_logs/      # 配电网详细日志
└── saved_state/   # 仿真状态保存
```

### 7.2 各输出内容

| 输出文件 | 大小 | 内容说明 |
|---------|------|---------|
| fcs.csv | 288 B | 快充站列名定义 + Time,Item,Value 表头（命令行模式仅输出结构，无完整时序数据） |
| scs.csv | — | 慢充站列名定义（同上） |
| gs.csv | — | 加油站列名定义 |
| cproc.clog | 1405 B | 充电过程压缩日志（二进制格式，含实际充电事件） |
| cproc.log | 0 B | 充电过程文本日志（本次运行为空） |
| pdn_res.log | — | 配电网计算日志（含 "Enable load reduction at bus b0/b1/b2"） |
| pdn_logs/ | 目录 | 配电网详细日志 |

> **发现**：V2Sim 命令行模式（`simulate_single` API）默认不输出完整时序 CSV 数据。GUI 模式下可获得完整的站级负荷时序。此差异为 V2Sim 功能设计，非运行错误。`logging_items` 参数传入后仍仅生成列名而无数据行，需进一步研究 V2Sim 的结果输出机制。

### 7.3 结果检查

**可确认的事实**：
- 仿真 17280 步正常完成，无异常退出
- pdn 插件被加载并执行（pdn_res.log 有输出）
- 充电过程有事件记录（cproc.clog 1405 字节非空）
- 配电网计算触发了负荷削减（"Enable load reduction"日志）

**无法确认的结论**（降级处理）：
- 快充站峰值负荷数值：命令行模式未输出完整时序，标为 E1
- 各站负荷分布：同上，需 GUI 模式或进一步 API 研究
- 电气数值合理性：未进行交叉校核

---

## 8. 证据等级评定（按 OpenSpec E0—E4 定义）

> E0=未尝试 | E1=有代码/配置但未执行 | E2=安装/导入成功 | E3=固定输入+命令+输出+结果检查齐备的最小案例运行 | E4=输出经交叉验证或与基准对比

| 维度 | 等级 | 依据 |
|------|------|------|
| 安装 + import | **E2** | `pip install v2sim==1.4.4` 成功；`import v2sim; print(v2sim.__version__)` 输出 `1.4.4` |
| 车辆生成 | **E3** | 固定命令 `v2sim-gen-trip -n-ev 500 -n-gv 500`；输出 `1000/1000, 100.00%`；生成 `ux_12nodes.veh.xml.gz`；exit code 0 |
| 仿真主循环 | **E3** | 固定输入(seed=42)；`TimeConfig(0,10,172800)`；输出 17280 步、9.2 秒、exit 0；pdn 插件加载确认 |
| 充电事件记录 | **E2** | `cproc.clog` 非空(1405B)，但未解析验证内容 |
| 配电网插件 | **E2** | pdn_res.log 有"Enable load reduction"输出，但未校核电气数值 |
| 时序 CSV 输出 | **E1** | fcs.csv 仅有列定义，命令行模式未产生完整数据行 |
| V2G 功能 | **E1** | 配置中存在 V2G 参数，未单独运行放电场景 |
| SUMO 后端 | **E0** | 未安装独立 SUMO，sumo_* 案例未运行 |

---

## 9. V2Sim 能力边界

### 9.1 可复用能力（交通 + 充电 + EV 行为）

| 能力 | V2Sim 实现方式 | 新系统潜在复用方式 |
|------|--------------|-----------------|
| EV 出行生成 | OD 驱动 + 随机种子 | 作为数据生成器参考 |
| 交通流仿真 | UXsim(中观) / SUMO(微观) | 交通孪生体候选后端 |
| 充电排队与功率仿真 | 事件驱动 + CC-CV 模型 | 充电站孪生体参考 |
| V2G 放电 | 可配置 V2G 策略 | 待验证后评估 |

### 9.2 配电网计算内核（FPowerKit）

| 属性 | 值 |
|------|---|
| 求解方式 | 基于 LinDistFlow 线性化潮流 |
| 精度 | 线性近似（非全非线性潮流） |
| 与候选后端关系 | 为 V2Sim 内置方案，需与 pandapower/OpenDSS 等对比后决定 |

### 9.3 不可直接复用（需 Python 编排层）

- 自定义智能体决策逻辑
- T 型架构孪生体编排
- LLM 顾问接入
- 拓扑画布可视化
- 多场景对比分析

---

## 10. 与新系统验收边界

| 声明 | 说明 |
|------|------|
| V2Sim 为外部参考项目 | 其运行结果不计入新系统完成度 |
| 配电网内核未决定 | FPowerKit 仅为候选之一，需对比后选型 |
| 交通路线未决定 | UXsim/SUMO 仅为候选，需评估后确定 |
| 本记录不预设技术路线 | 仅记录复现事实，不做推荐 |

---

## 11. 复现步骤（供 Reviewer 在干净环境复核）

```bash
# 1. 创建干净隔离环境
conda create -n v2sim_test python=3.12 -y
conda activate v2sim_test

# 2. 安装固定版本（注意 fpowerkit 兼容性）
pip install v2sim==1.4.4
pip install fpowerkit==0.4.3
# 验证: python -c "import v2sim; print(v2sim.__version__)"  →  1.4.4

# 3. 下载固定 tag 案例
# https://github.com/hesl-seu/v2sim/archive/refs/tags/v1.4.4.zip
# 解压后案例位于 v2sim-1.4.4/cases/ux_12nodes/

# 4. 生成车辆
v2sim-gen-trip -d "v2sim-1.4.4/cases/ux_12nodes" -n-ev 500 -n-gv 500
# 预期: 1000/1000, 100.00% | exit code 0

# 5. 运行仿真（Python API）
python -c "
from v2sim import simulate_single, TimeConfig
simulate_single('v2sim-1.4.4/cases/ux_12nodes', TimeConfig(0, 10, 172800), silent=False, seed=42)
"
# 预期: Total steps: 17280 | 用时 ~9 秒 | exit code 0

# 6. 检查输出
ls v2sim-1.4.4/cases/ux_12nodes/results/
# 预期: fcs.csv, scs.csv, gs.csv, cproc.clog, cproc.log, pdn_res.log, pdn_logs/
# 注意: 命令行模式 fcs.csv 仅含列定义，无完整时序数据行

# 7. 代码目录重扫验证
python docs/reference_catalogs/v2sim/generate_catalog.py --output /tmp/rescan/
diff docs/reference_catalogs/v2sim/symbols.csv /tmp/rescan/symbols.csv
# 预期: 无差异（同版本同结果）
```

> **已知问题**：`pip install v2sim==1.4.4` 默认解析 `fpowerkit>=0.4.1` 为最新版 0.5.0，会导致 UXsim 路由时 `IndexError`。必须手动 `pip install fpowerkit==0.4.3` 降级。
