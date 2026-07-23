# `pandapower.pypower.dSbr_dV`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.dSbr_dV.dSbr_dV | (branch, Yf, Yt, V) | pandapower/pypower/dSbr_dV.py#L13 | Computes partial derivatives of power flows w.r.t. voltage. | 输入：branch, Yf, Yt, V；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | real.astype；len；arange；issparse；abs；sparse；flatten；asmatrix；range；conj；diag；zeros；item；asarray | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
