# pandapower 参考代码目录

## 固定对象

| 字段 | 值 |
| --- | --- |
| 项目 | [e2nIEE/pandapower](https://github.com/e2nIEE/pandapower) |
| 版本 | `v3.5.4` |
| 提交 | `be3f13b6db3632fe690f997654d15c9173a14839` |
| 发布页 | <https://github.com/e2nIEE/pandapower/releases/tag/v3.5.4> |
| 扫描范围 | 固定提交下 `pandapower/` 的生产 Python 源码 |
| 排除范围 | `pandapower/test/`、缓存和构建产物 |
| 目录用途 | 后续 PoC 阅读与适配参考，不是新系统代码或验收 baseline |

## 目录内容

- `symbols.csv`：全部可解析模块级函数、类和类方法，含私有/内部符号；
- `coverage.md`：源码文件、符号类型、排除项、解析失败、重复定义合并和复核统计；
- `modules/`：按源码模块生成的人类可读目录；
- `manual_review.md`：模型创建、求解、控制、时序、结果和错误入口的人工复核结论；
- `manual_review_symbols.txt`、`manual_review_summaries.tsv`：可重放的人工复核策略与摘要；
- `sampled_modules.txt`：内部支撑模块抽检范围。

## 重新生成

先在临时目录获取同一固定提交：

```bash
PANDAPOWER_CATALOG_TMP="$(mktemp -d /tmp/pandapower-catalog-XXXXXX)"
git clone --depth 1 --branch v3.5.4 \
  https://github.com/e2nIEE/pandapower.git \
  "$PANDAPOWER_CATALOG_TMP/pandapower"
test "$(git -C "$PANDAPOWER_CATALOG_TMP/pandapower" rev-parse HEAD)" = \
  "be3f13b6db3632fe690f997654d15c9173a14839"
```

在仓库根目录运行：

```bash
python tools/reference_catalog/generate_python_catalog.py \
  --source-root "$PANDAPOWER_CATALOG_TMP/pandapower" \
  --package pandapower \
  --output docs/reference_catalogs/grid_backend/pandapower \
  --project pandapower \
  --version v3.5.4 \
  --commit be3f13b6db3632fe690f997654d15c9173a14839 \
  --exclude-dir test \
  --exclude-dir __pycache__ \
  --manual-review-file \
    docs/reference_catalogs/grid_backend/pandapower/manual_review_symbols.txt \
  --manual-summary-file \
    docs/reference_catalogs/grid_backend/pandapower/manual_review_summaries.tsv \
  --sampled-module-file \
    docs/reference_catalogs/grid_backend/pandapower/sampled_modules.txt
```

生成器在解析失败、空功能说明、重复限定名、人工复核符号缺失或人工摘要缺失时返回非零退出码。Reviewer 应比较重新生成前后的 `symbols.csv` 和 `coverage.md`；同一提交的结果应无遗漏、无重复且保持稳定。
