# V2Sim 代码目录覆盖率

## 扫描结果（精确统计）

| 指标 | 值 |
|------|---|
| 扫描 .py 文件数 | 114 |
| 解析失败文件数 | 0 |
| 原始符号数（含重复） | 1770 |
| 去重后唯一符号数 | 1755 |
| 重复 qualified_name 数 | 13 |
| class | 181 |
| function | 158 |
| method | 1416 |
| 功能说明已填充 | 641 |
| 功能说明待人工补充 | 1114 |

## 排除项

| 排除类型 | 说明 |
|---------|------|
| `__pycache__/` | Python 编译缓存 |
| 非 .py 文件 | 数据文件、配置文件等 |
| 嵌套定义（二级以下） | 仅扫描顶层和类一级方法 |

## 去重说明

使用 `qualified_name`（模块路径.类名.方法名）作为唯一标识。
原始扫描发现 13 个重复项，已去重保留首次出现。

### 重复项示例（前10个）

- `gen.csquery._Rect.__init__` (出现 3 次)
- `gen.misc.create_veh` (出现 3 次)
- `gui.mainbox.controls.network.NetworkPanel.Enabled` (出现 2 次)
- `gui.mainbox.controls.network.NetworkPanel.saved` (出现 2 次)
- `gui.mainbox.controls.scrtv.ScrollableTreeView.AfterFunc` (出现 2 次)
- `veh.ev.EV.kf` (出现 2 次)
- `veh.ev.EV.ks` (出现 2 次)
- `veh.ev.EV.kv2g` (出现 2 次)
- `veh.veh.Vehicle.kf` (出现 2 次)
- `veh.veh.Vehicle.kr` (出现 2 次)

## 复核方法

- `evidence_status`: `auto_generated` = 工具自动生成
- `review_status`: `pending` = 待复核, `reviewed` = 已人工复核
- 核心模块（core, sim, hub, veh, net, plugins）需逐项人工复核
- 辅助模块按模块抽检 ≥5 符号
