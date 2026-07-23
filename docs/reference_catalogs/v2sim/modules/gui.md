# gui/ — GUI 界面模块

> 复核状态：抽检 [sampled]

## 功能

基于 Tkinter 的图形用户界面，包含欢迎页、主界面、结果查看器等。

## 核心入口

| 符号 | 功能 | 对应命令 |
|------|------|---------|
| WelcomeBox | 欢迎界面（项目选择） | v2sim-gui |
| MainBox | 主仿真界面（配置+运行） | v2sim-gui → 打开项目 |
| ViewerBox | 结果查看器（绘图+统计） | v2sim-viewer |
| ParaBox | 并行仿真界面 | v2sim-para |
| PlgBox | 插件管理界面 | — |
| ConvertBox | 案例转换界面 | v2sim-convert |

## 说明

GUI 模块约 500 个符号，主要为界面控件和事件处理。
对新系统无直接复用价值，仅作为了解 V2Sim 用户交互方式的参考。
