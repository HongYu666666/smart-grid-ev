# `pandapower.pypower.dIbr_dV`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.dIbr_dV.dIbr_dV | (branch, Yf, Yt, V) | pandapower/pypower/dIbr_dV.py#L12 | Computes partial derivatives of branch currents w.r.t. voltage. | 输入：branch, Yf, Yt, V；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | range；issparse；len；abs；sparse；asmatrix；flatten；diag；asarray | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.dIbr_dV.dIbr_dV_new | (branch, Yf, Yt, V) | pandapower/pypower/dIbr_dV.py#L64 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pypower.dIbr_dV.dIbr_dV_new 的实现与调用链确认。 | 输入：branch, Yf, Yt, V；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | issparse；range；sparse；flatten；len；abs；asarray；conj；asmatrix | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
