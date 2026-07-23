# V2Sim 代码目录

## 项目信息

| 属性 | 值 |
|------|---|
| 项目 | V2Sim — Open-Source V2G Simulation Platform |
| 版本 | 1.4.4 (PyPI: `pip install v2sim==1.4.4`) |
| 仓库 | https://github.com/hesl-seu/v2sim |
| 固定 tag | `v1.4.4` (commit `5cf6777ac6780f2247802533941204e4a95bc2ce`) |
| wheel SHA256 | `8f6dd9b4822af0545806d29d0c8371cccad2594a36e5aa91e2dc9cec4ab2198e` |
| 许可 | BSD-3-Clause |
| 扫描范围 | `v2sim/` Python 包全部 `.py` 生产源码（顶层定义 + 类一级方法） |
| 扫描根 | 通过 `import v2sim; Path(v2sim.__file__).parent` 自动定位，不使用硬编码路径 |
| 排除项 | `__pycache__/`、非 `.py` 文件、二级以下嵌套定义 |

## 生成命令（可重放）

```bash
# 在任何已安装 v2sim==1.4.4 的 Python 3.12 环境中执行：
python docs/reference_catalogs/v2sim/generate_catalog.py \
    --output docs/reference_catalogs/v2sim/
```

生成器通过 `import v2sim` 自动定位包路径，不依赖硬编码个人路径。

同一固定版本重新扫描应产出相同的 `symbols.csv`（行数和 qualified_name 集合一致）。

## symbols.csv 字段说明

| 字段 | 含义 |
|------|------|
| file | 相对于包根目录的文件路径 |
| qualified_name | 唯一限定名（模块.类.方法 格式） |
| type | `class` / `function` / `method` |
| name | 符号名称 |
| signature | 函数/方法签名（含参数和返回类型注解） |
| visibility | `public` / `protected` / `private` / `dunder` |
| line | 源码行号（锚点） |
| description | 功能说明（docstring 首行或"待人工补充"） |
| inputs | 输入参数（同 signature） |
| outputs | 输出说明 |
| side_effects | 副作用 |
| dependencies | 主要依赖调用 |
| dev_usage | 开发用途说明 |
| evidence_status | `auto_generated` = 工具生成 |
| review_status | `pending` = 待复核 / `reviewed` = 已人工复核 |

## 文件结构

```
docs/reference_catalogs/v2sim/
├── README.md              # 本文件
├── generate_catalog.py    # 可重放生成器脚本
├── symbols.csv            # 全量唯一符号清单
├── coverage.md            # 精确覆盖率统计
└── modules/               # 按模块整理的功能说明
    ├── core.md
    ├── sim.md
    ├── hub.md
    ├── veh.md
    ├── net.md
    ├── plugins.md
    ├── gen.md
    ├── plot.md
    └── gui.md
```

## 使用方法

1. 运行 `generate_catalog.py` 生成/更新 `symbols.csv` 和 `coverage.md`
2. `symbols.csv` 中所有符号的 `description` 均非空（无法确认的标"待人工补充"）
3. 核心模块需人工复核后将 `review_status` 改为 `reviewed`
4. `modules/*.md` 提供按功能分组的人工复核记录

## 版本重扫验证

```bash
# 重新安装相同版本并扫描
pip install v2sim==1.4.4
python docs/reference_catalogs/v2sim/generate_catalog.py --output /tmp/rescan/
diff docs/reference_catalogs/v2sim/symbols.csv /tmp/rescan/symbols.csv
# 预期: 无差异（同版本同结果）
```
