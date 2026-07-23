# `pandapower.pypower.d2AIbr_dV2`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.d2AIbr_dV2.d2AIbr_dV2 | (dIbr_dVa, dIbr_dVm, Ibr, Ybr, V, lam) | pandapower/pypower/d2AIbr_dV2.py#L13 | Computes 2nd derivatives of \|complex current\|**2 w.r.t. V. | 输入：dIbr_dVa, dIbr_dVm, Ibr, Ybr, V, lam；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | range；sparse；d2Ibr_dV2；len；Ibr.conj；dIbr_dVa.conj；dIbr_dVm.conj | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
