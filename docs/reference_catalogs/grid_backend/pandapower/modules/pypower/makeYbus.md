# `pandapower.pypower.makeYbus`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.makeYbus.branch_vectors | (branch, nl) | pandapower/pypower/makeYbus.py#L87 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pypower.makeYbus.branch_vectors 的实现与调用链确认。 | 输入：branch, nl；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | errstate；ones；nonzero；real；any；exp；conj | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.makeYbus.makeYbus | (baseMVA, bus, branch) | pandapower/pypower/makeYbus.py#L22 | Builds the bus admittance matrix and branch admittance matrices. | 输入：baseMVA, bus, branch；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | branch_vectors；astype；csr_matrix；hstack；Y.eliminate_zeros；Y.sum_duplicates；Y.sort_indices；real；ones；range | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
