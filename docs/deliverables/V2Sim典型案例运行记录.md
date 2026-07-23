# V2Sim 典型案例运行记录

> **OpenSpec change**: `assess-grid-simulation-backends`  
> **对应 tasks**: 2.1—2.3  
> **负责人**: HongYu666666 (member)  
> **Reviewer**: lead  
> **日期**: 2026-07-23

---

## 1. 版本与提交

| 项目 | 值 |
|------|---|
| V2Sim PyPI 版本 | 1.4.4 |
| V2Sim GitHub 仓库 | https://github.com/hesl-seu/v2sim |
| 案例来源 | `v2sim-main.zip` (GitHub main branch, 下载于 2026-07-23) |
| FPowerKit 版本 | 0.4.3 |
| libsumo 版本 | 1.27.1 |

---

## 2. 运行环境

| 项目 | 值 |
|------|---|
| OS | Windows 10/11 x64 |
| Python | 3.12.7 (Anaconda base) |
| pip | 24.2 |
| 隔离方法 | Anaconda base 环境（未使用额外 venv） |
| SUMO | 未独立安装（使用 pip 安装的 libsumo + sumo-data） |

### 关键依赖版本

```
v2sim==1.4.4
fpowerkit==0.4.3
libsumo==1.27.1
sumolib==1.27.1
traci==1.27.1
sumo-data==1.27.1
pyproj==3.7.2
feasytools==0.1.6
numpy==1.26.4
scipy==1.13.1
matplotlib==3.9.2
networkx==3.3
```

---

## 3. 代表性案例选择

| 属性 | 值 |
|------|---|
| 案例名称 | ux_12nodes |
| 交通引擎 | UXsim（中观，内置于 v2sim，无需额外安装） |
| 配电网规模 | 12 节点 |
| 选择原因 | 最轻量案例，不依赖外部 SUMO 安装，适合验证基本流程 |

### 案例配置文件

案例路径（解压后）：`v2sim-main/v2sim-main/cases/ux_12nodes/`

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
v2sim-gen-trip -d "<案例路径>/ux_12nodes" -n-ev 500 -n-gv 500
```

**参数说明**：
- `-n-ev 500`：500 辆电动汽车
- `-n-gv 500`：500 辆普通燃油车
- 默认模拟 7 天（`-day 7`）

**输出**：
```
1000/1000, 100.00%
已完成. 用时0.1秒.
```

**生成文件**：`ux_12nodes.veh.xml.gz`（车辆行程压缩文件）

---

## 6. 仿真运行

**命令**：
```bash
v2sim-gui
# GUI 中：添加项目 → 选择 ux_12nodes 文件夹 → 开始仿真
```

**等效命令行方式**（非 GUI）：
```bash
v2sim -d "<案例路径>/ux_12nodes" --time 0 172800 10
```

**实际终端输出**：
```
仿真开始，按Ctrl-C中断
  交通仿真器：UXsim
  路网: ux_12nodes.net.xml
  行程: ux_12nodes.veh.xml.gz, 1000辆两车
  快充: ux_12nodes.fcs.xml, 12个站点
  慢充: ux_12nodes.scs.xml, 12个站点
  加油站: ux_12nodes.gs.xml, 12个站点
已创建单个串行仿真。
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
| 墙钟时间 | 9 秒 |
| 退出状态 | 正常完成（exit code 0） |

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

| 输出文件 | 覆盖内容 | 说明 |
|---------|---------|------|
| fcs.csv | 快充站充电功率 | 12 站 × 时序，峰值约 580kW（总和），早高峰 8:00-12:00 |
| scs.csv | 慢充站充电功率 | 12 站 × 时序 |
| bus.csv | 母线电压、有功/无功负荷 | 12 节点配电网状态 |
| line.csv | 线路有功/无功、电流 | 配电线路潮流 |
| utn.csv | 交通网络统计 | 车辆出行数据 |
| gen.csv | 发电机有功/无功 | 电源侧数据 |

### 7.3 结果检查

**快充站总负荷检查**（v2sim-viewer 绘图输出）：
- 负荷曲线形状：日间单峰（8:00-12:00 峰值约 580kW），夜间趋近 0
- 各站负荷不均：CS3、CS4、CS8 承担主要负荷
- 第二天负荷显著低于第一天（仿真前期车辆活跃度高）

**查看命令**：
```bash
v2sim-viewer -d "<案例路径>/ux_12nodes/results"
# 勾选"快充站" → 点击"绘制"
```

---

## 8. 证据等级评定

| 维度 | 等级 | 说明 |
|------|------|------|
| 安装 | **E3** | pip install 成功，import 验证通过 |
| 车辆生成 | **E3** | 命令执行成功，输出文件生成 |
| 仿真运行 | **E3** | 17280 步正常完成，exit code 0，耗时 9 秒 |
| 充电负荷输出 | **E3** | fcs.csv 有合理数值，峰值形状符合预期 |
| 配电网输出 | **E2** | bus.csv/line.csv 有输出，未深入校核电气数值 |
| V2G 功能 | **E1** | 配置中存在 V2G 参数，未单独验证放电场景 |
| SUMO 后端 | **E0** | 未安装独立 SUMO，sumo_* 案例未运行 |

**证据等级定义**：
- E0：未尝试
- E1：有代码/配置但未执行
- E2：执行但输出未深入校核
- E3：执行成功且输出经初步合理性检查
- E4：输出经交叉验证或与基准对比

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
# 1. 创建干净环境
conda create -n v2sim_test python=3.12 -y
conda activate v2sim_test

# 2. 安装
pip install v2sim==1.4.4

# 3. 验证安装
python -c "import v2sim; print(v2sim.__version__)"
# 预期输出: 1.4.4

# 4. 下载案例
# 浏览器下载 https://github.com/hesl-seu/v2sim/archive/refs/heads/main.zip
# 解压后进入 cases/ux_12nodes/

# 5. 生成车辆
v2sim-gen-trip -d "cases/ux_12nodes" -n-ev 500 -n-gv 500
# 预期输出: 1000/1000, 100.00%

# 6. 运行仿真（命令行）
v2sim -d "cases/ux_12nodes" --time 0 172800 10
# 预期: 仿真结束. 用时约 9 秒. Total steps: 17280

# 7. 检查输出
ls cases/ux_12nodes/results/
# 预期: bus.csv, fcs.csv, scs.csv, line.csv, gen.csv, utn.csv 等
```
