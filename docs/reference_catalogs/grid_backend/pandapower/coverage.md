# 覆盖率与完整性报告

- 项目：`pandapower`
- 固定版本：`v3.5.4`
- 固定提交：`be3f13b6db3632fe690f997654d15c9173a14839`
- 扫描根目录：`pandapower/`
- 已解析生产源码文件：365
- 解析失败文件：0
- 排除 Python 文件：146
- 符号总数：2319
- 函数：1484
- 类：174
- 方法：661
- 人工复核：37
- 模块抽检：156
- 自动生成：2126
- 空功能说明：0
- 重复限定名：0
- 已合并的多处定义：13
- 人工复核策略中未找到的符号：0
- 人工复核符号缺少人工摘要：0

## 排除规则

- 排除目录：`__pycache__`, `test`
- 测试、示例、vendored、生成代码和构建产物仅在明确命中上述目录时排除。
- `pypower/` 是 pandapower 运行时求解链的一部分，本次未作为 vendored 代码排除。

## 完整性判定

- 可解析源码限定名与目录限定名集合：一致。
- 所有符号功能说明非空：是。
- 人工复核策略中的符号均被扫描：是。

## 解析失败

- 无。

## 重复限定名

- 无。

## 已合并的多处定义

- `pandapower.auxiliary._read_from_object_attribute`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.auxiliary.element_types_to_ets`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.auxiliary.ets_to_element_types`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.auxiliary.get_indices`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.auxiliary.read_from_net`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.auxiliary.write_to_net`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.build_branch.get_trafo_values`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.control.controller.trafo.DiscreteTapControl.DiscreteTapControl.vm_set_pu`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.control.util.auxiliary.log_same_type_existing_controllers`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.control.util.characteristic.LogSplineCharacteristic.x_vals`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.control.util.characteristic.LogSplineCharacteristic.y_vals`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.converter.powerfactory.pf_export_functions.create_network_dict`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。
- `pandapower.file_io.to_json`：同一运行时限定名的 getter/setter、兼容分支或重定义已合并，源码锚点全部保留。

## 未命中的人工复核符号

- 无。

## 缺少人工摘要的复核符号

- 无。
