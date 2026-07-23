# V2Sim 代码目录

## 项目信息

| 属性 | 值 |
|------|---|
| 项目 | V2Sim — Open-Source V2G Simulation Platform |
| 版本 | 1.4.4 (PyPI) |
| 仓库 | https://github.com/hesl-seu/v2sim |
| 许可 | BSD-3-Clause |
| 扫描范围 | `v2sim/` Python 包全部 `.py` 生产源码 |
| 排除项 | `__pycache__/`、`.pyc` 文件 |

## 扫描统计

| 指标 | 值 |
|------|---|
| 扫描文件数 | 95 |
| 类(class) | 181 |
| 函数/方法(function) | 1653 |
| 总符号数 | 1834 |
| 未解析文件 | 0 |

## 生成命令

```python
# 在 Python 3.12 环境中执行，v2sim 1.4.4 已安装
import ast, csv, os

pkg_dir = '<site-packages>/v2sim'  # 实际路径: D:\liulanqi\anaconda3\Lib\site-packages\v2sim
results = []

for root, dirs, files in os.walk(pkg_dir):
    dirs[:] = [d for d in dirs if d != '__pycache__']
    for f in files:
        if not f.endswith('.py'):
            continue
        filepath = os.path.join(root, f)
        relpath = os.path.relpath(filepath, pkg_dir).replace('\\', '/')
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as fh:
            tree = ast.parse(fh.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                results.append([relpath, 'class', node.name, node.lineno])
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                results.append([relpath, 'function', node.name, node.lineno])

with open('symbols.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['file', 'type', 'name', 'line'])
    w.writerows(results)
```

## 文件结构

```
docs/reference_catalogs/v2sim/
├── README.md          # 本文件
├── symbols.csv        # 全量符号清单 (1834 行)
├── coverage.md        # 覆盖率与排除项说明
└── modules/           # 按模块整理的功能说明
    ├── core.md        # 核心仿真引擎
    ├── sim.md         # 交通仿真（UXsim/SUMO）
    ├── hub.md         # 充电站管理
    ├── veh.md         # 车辆模型
    ├── net.md         # 路网模型
    ├── plugins.md     # 插件系统（含配电网）
    ├── gen.md         # 数据生成
    ├── plot.md        # 结果绘图
    └── gui.md         # GUI 界面
```

## 使用方法

1. `symbols.csv` 包含所有符号的文件、类型、名称和行号
2. `modules/*.md` 按功能模块整理核心符号的功能说明
3. 核心模块（core, sim, hub, veh, plugins）已人工复核
4. GUI、plot 等辅助模块为抽检状态
