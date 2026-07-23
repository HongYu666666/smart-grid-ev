# `pandapower.pypower.bustypes`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.bustypes.bustypes | (bus, gen, vsc=None) | pandapower/pypower/bustypes.py#L23 | Builds index lists of each type of bus (C{REF}, C{PV}, C{PQ}). | 输入：bus, gen, vsc；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | find；isin | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.bustypes.bustypes_dc | (bus_dc) | pandapower/pypower/bustypes.py#L62 | Builds index lists of each type of bus (DC_REF, DC_P). | 输入：bus_dc；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | find | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
