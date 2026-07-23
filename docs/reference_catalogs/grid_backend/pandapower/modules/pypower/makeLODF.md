# `pandapower.pypower.makeLODF`

本模块共记录 4 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.makeLODF.makeLODF | (branch, PTDF) | pandapower/pypower/makeLODF.py#L35 | Builds the line outage distribution factor matrix. | 输入：branch, PTDF；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | np.real；sparse；diag；update_LODF_diag；np.errstate；ones；arange | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.makeLODF.makeOTDF | (PTDF, LODF, outage_branches) | pandapower/pypower/makeLODF.py#L71 | Compute the Outage Transfer Distribution Factors (OTDF) matrix. | 输入：PTDF, LODF, outage_branches；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | np.vstack | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.makeLODF.outage_results_OTDF | (OTDF, Pbus, outage_branches) | pandapower/pypower/makeLODF.py#L128 | Calculate the branch power flows for each outage scenario based on the given Outage Transfer Distribution Factors (OTDF), bus power injections (Pbus), and specified outage branches. | 输入：OTDF, Pbus, outage_branches；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | nminus1_otdf.reshape；Pbus.reshape | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.makeLODF.update_LODF_diag | (LODF) | pandapower/pypower/makeLODF.py#L29 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pypower.makeLODF.update_LODF_diag 的实现与调用链确认。 | 输入：LODF；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | jit；range | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
