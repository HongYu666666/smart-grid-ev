# `pandapower.network_structure`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.network_structure.get_std_type_structure_dict | () -> dict | pandapower/network_structure.py#L839 | This function returns the structure dict of the std_types | 输入：无显式输入；输出：dict | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | dtype；pd.Int64Dtype | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.network_structure.get_structure_dict | () -> dict | pandapower/network_structure.py#L6 | This function returns the structure dict of the network | 输入：无显式输入；输出：dict | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | dtype；pd.Int64Dtype | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
