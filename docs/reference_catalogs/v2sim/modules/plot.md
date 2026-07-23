# plot/ — 结果绘图模块

> 复核状态：抽检 [sampled]

## 功能

读取仿真结果 CSV 文件，生成时序曲线图（PNG）。

## 核心组件

| 符号 | 功能 |
|------|------|
| PlotReader | 读取结果 CSV 并解析 |
| plot_fcs() | 绘制快充站负荷曲线 |
| plot_scs() | 绘制慢充站负荷曲线 |
| plot_bus() | 绘制母线电压曲线 |
| plot_line() | 绘制线路潮流曲线 |
| plot_gen() | 绘制发电机出力曲线 |

## 对应命令行工具

```bash
v2sim-plot -d <results_dir>
v2sim-advplot -d <results_dir>
```
