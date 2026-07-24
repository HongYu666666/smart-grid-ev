# V2Sim 典型案例运行记录

> **OpenSpec change**: `assess-grid-simulation-backends`  
> **对应 tasks**: 2.1—2.6  
> **负责人**: HongYu666666 (member)  
> **Reviewer**: lead（2026-07-24 接管修复并独立复核）  
> **日期**: 2026-07-23（运行）/ 2026-07-24（验收）

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
pip install v2sim==1.4.4
pip install fpowerkit==0.4.3
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

> **本次观察**：当前 `simulate_single` 调用生成的 `fcs.csv` 只有列定义，没有完整时序数据。该事实只说明本次固定命令和配置的输出；尚不能据此断言所有命令行模式均如此，也不能把早期 GUI 结果当作本次隔离运行证据。输出配置和读取机制转入后续 PoC。

### 7.3 结果检查

**可确认的事实（含文本证据）**：

1. 仿真 17280 步正常完成，exit code 0，墙钟 9.2 秒
2. pdn 插件加载并执行：
   ```
   # pdn_res.log 完整内容 (96 bytes):
   Enable load reduction at bus b1
   Enable load reduction at bus b0
   Enable load reduction at bus b2
   ```
3. 充电过程有事件记录：
   ```
   cproc.clog: 1405 bytes, sha256=82ac9836c8e792495041ea98e2f2fced1a8b06ef125e0c1c461ff248f679a538
   ```
4. fcs.csv 结构（命令行模式仅输出列定义，无数据行）：
   ```
   # fcs.csv 完整内容 (288 bytes):
   C
   fcs_CS1#cnt,fcs_CS10#cnt,...,fcs_CS9#cnt,fcs_CS1#c,...,fcs_CS9#c
   Time,Item,Value
   ```

**检查命令**（可复跑）：
```bash
# 验证仿真完成
python -c "
from v2sim import simulate_single, TimeConfig
simulate_single('v2sim-1.4.4/cases/ux_12nodes', TimeConfig(0, 10, 172800), silent=False, seed=42)
"
# 预期最后一行: Total steps: 17280

# 验证输出文件存在
python -c "
import os
results = 'v2sim-1.4.4/cases/ux_12nodes/results'
for f in sorted(os.listdir(results)):
    size = os.path.getsize(os.path.join(results, f)) if os.path.isfile(os.path.join(results, f)) else 'dir'
    print(f'{f}: {size}')
"

# 验证 cproc.clog 哈希
python -c "
import hashlib
with open('v2sim-1.4.4/cases/ux_12nodes/results/cproc.clog','rb') as f:
    print(hashlib.sha256(f.read()).hexdigest())
"
# 预期: 82ac9836c8e792495041ea98e2f2fced1a8b06ef125e0c1c461ff248f679a538
```

**降级的结论（原版报告中已移除）**：
- ~~"峰值约 580kW"~~ → 降级为 E1：此数据来自 GUI 模式的早期非隔离运行，当前隔离环境命令行模式未输出时序数据，无法交叉验证
- ~~"第二天显著更低"~~ → 同上，降级为 E1
- ~~"FPowerKit 为 LinDistFlow"~~ → 来源锚点：`fpowerkit/solcmb.py:9` 定义 `LinDistFlow = 'LinDistFlow'` 枚举值。V2Sim pdn 插件使用 FPowerKit 的 `Estimator` 枚举进行潮流估计。证据等级 E1（源码可见但未验证具体调用路径）

---

### 7.4 输入、控制动作与评价指标边界

| 类别 | 本次案例中的对象 | 当前证据 |
| --- | --- | --- |
| 输入 | 12 节点配网、交通路网、快/慢充站、1000 辆车辆行程、插件配置、`seed=42`、10 秒步长 | 固定文件与命令，E3 |
| 交通/车辆状态 | UXsim 时间推进、车辆行程与充电过程 | 主循环完成；逐事件内容未交叉校核 |
| 控制动作 | pdn 插件触发 b0/b1/b2 母线负荷削减 | `pdn_res.log` 文本确认，数值动作与约束未校核，E2 |
| 充电输出 | `cproc.clog`、快/慢充统计文件 | 文件与哈希确认；事件内容和完整时序未解析，E1/E2 |
| 配网输出 | bus/line/gen 日志与 pdn 详细日志 | 输出路径确认；电压、潮流和损耗未做基准对比，最高 E2 |
| 评价指标 | 步数、退出状态、墙钟时间、文件存在/大小/哈希 | 可复核；不构成电气正确性或性能结论 |

代码目录入口：[`docs/reference_catalogs/v2sim/`](../reference_catalogs/v2sim/README.md)。目录固定同一提交，记录 114 个源码文件、1755 个唯一符号、48 个核心人工复核符号和 298 个模块抽检符号。

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

| 属性 | 值 | 证据 |
|------|---|------|
| 包版本 | 0.4.3 | `pip show fpowerkit` |
| 求解方式 | DistFlow / LinDistFlow / LinDistFlow2 (枚举) | 源码锚点: `fpowerkit/solcmb.py:8-10` |
| 默认估计器 | `Estimator.DistFlow` | 源码锚点: `fpowerkit/solcmb.py:24` |
| 算法与精度 | 本次未确认实际求解路径和误差 | 枚举存在只记 E1；未通过案例输出或基准馈线交叉验证 |
| 与候选后端关系 | V2Sim 内置方案，需与 pandapower/OpenDSS 等对比后决定 | — |

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

# 7. 代码目录重扫验证（SOURCE_ROOT 指向固定 tag 克隆）
python tools/reference_catalog/generate_python_catalog.py \
  --source-root "$SOURCE_ROOT" --package v2sim \
  --output /tmp/v2sim-rescan --project V2Sim \
  --version v1.4.4 \
  --commit 5cf6777ac6780f2247802533941204e4a95bc2ce \
  --exclude-dir __pycache__ \
  --manual-review-file docs/reference_catalogs/v2sim/manual_review_symbols.txt \
  --manual-summary-file docs/reference_catalogs/v2sim/manual_review_summaries.tsv \
  --sampled-module-file docs/reference_catalogs/v2sim/sampled_modules.txt
diff docs/reference_catalogs/v2sim/symbols.csv /tmp/v2sim-rescan/symbols.csv
# 预期: 114 files / 1755 symbols / 0 duplicates / 0 empty summaries / 0 parse errors
```

> **已知问题**：`pip install v2sim==1.4.4` 默认解析 `fpowerkit>=0.4.1` 为最新版 0.5.0，会导致 UXsim 路由时 `IndexError`。必须手动 `pip install fpowerkit==0.4.3` 降级。

## 12. Reviewer 验收记录

lead 于 2026-07-24 按固定 tag 重新克隆 `5cf6777ac6780f2247802533941204e4a95bc2ce` 并运行统一目录生成器，确认：

- 114 个 Python 源码文件全部解析；
- 1755 个限定名唯一，0 个重复、0 个空字段、0 个解析失败；
- 13 个多处定义合并并保留全部源码锚点；
- 48 个案例加载、时间推进、交通、车辆、充电、配网插件和结果入口具有人工作业摘要；
- 9 个支撑模块、298 个符号完成字段抽检；
- 运行报告中的 E3 只用于固定 V2Sim 案例，不提高新系统完成度。

原 PR #11 的旧版阻塞项未直接豁免；本分支保留组员提交作者信息，并由 lead 修复目录合同、复核状态和证据边界后再验收。

未达到 E4 的充电事件解析、站级时序、V2G/削减动作和电气交叉校核已转 [Issue #14](https://github.com/TsLouis/smart-grid-ev/issues/14)。
