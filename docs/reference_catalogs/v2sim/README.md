# V2Sim 参考代码目录

## 固定对象

| 字段 | 值 |
| --- | --- |
| 项目 | [hesl-seu/v2sim](https://github.com/hesl-seu/v2sim) |
| 版本 | `v1.4.4` / PyPI `1.4.4` |
| 提交 | `5cf6777ac6780f2247802533941204e4a95bc2ce` |
| wheel SHA256 | `8f6dd9b4822af0545806d29d0c8371cccad2594a36e5aa91e2dc9cec4ab2198e` |
| 许可 | BSD-3-Clause |
| 扫描范围 | 固定提交下 `v2sim/` 的 114 个 Python 源码文件 |
| 排除范围 | `__pycache__/`、非 Python 文件、函数/方法内部嵌套定义 |
| 目录用途 | 案例复现与后续适配阅读参考，不是新系统代码或验收 baseline |

## 目录内容

- `symbols.csv`：1755 个唯一函数、类和类方法，包含合同要求的 12 个字段；
- `coverage.md`：源码文件、符号类型、排除项、多处定义合并和复核统计；
- `modules/`：按真实源码路径生成的人类可读逐符号目录；
- `manual_review.md`：场景加载、时间推进、交通、车辆、充电、配网插件和结果入口的人工复核结论；
- `manual_review_symbols.txt`、`manual_review_summaries.tsv`：48 个核心符号的可重放人工复核策略与摘要；
- `sampled_modules.txt`：9 个内部支撑模块、298 个符号的抽检范围。

`symbols.csv` 字段为 `kind`、`qualified_name`、`signature`、`source_anchor`、`visibility`、`summary`、`inputs_outputs`、`side_effects`、`dependencies`、`development_relevance`、`evidence_status`、`review_status`。所有字段均非空；没有 docstring 的符号保留带源码定位的“待人工补充”说明。

## 重新生成

先在临时目录获取同一固定提交：

```bash
V2SIM_CATALOG_TMP="$(mktemp -d /tmp/v2sim-catalog-XXXXXX)"
git clone --depth 1 --branch v1.4.4 \
  https://github.com/hesl-seu/v2sim.git \
  "$V2SIM_CATALOG_TMP/source"
test "$(git -C "$V2SIM_CATALOG_TMP/source" rev-parse HEAD)" = \
  "5cf6777ac6780f2247802533941204e4a95bc2ce"
```

在仓库根目录运行：

```bash
python tools/reference_catalog/generate_python_catalog.py \
  --source-root "$V2SIM_CATALOG_TMP/source" \
  --package v2sim \
  --output docs/reference_catalogs/v2sim \
  --project V2Sim \
  --version v1.4.4 \
  --commit 5cf6777ac6780f2247802533941204e4a95bc2ce \
  --exclude-dir __pycache__ \
  --manual-review-file \
    docs/reference_catalogs/v2sim/manual_review_symbols.txt \
  --manual-summary-file \
    docs/reference_catalogs/v2sim/manual_review_summaries.tsv \
  --sampled-module-file \
    docs/reference_catalogs/v2sim/sampled_modules.txt
```

生成器在解析失败、空功能说明、重复限定名、人工复核符号缺失或人工摘要缺失时返回非零退出码。Reviewer 应在同一固定提交上重跑并比较 `symbols.csv` 和 `coverage.md`；预期为 114 files / 1755 symbols / 0 duplicates / 0 empty summaries / 0 parse errors。
