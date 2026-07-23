# `pandapower.pypower.dSbus_dV`

本模块共记录 3 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.dSbus_dV.dSbus_dV | (Ybus, V) | pandapower/pypower/dSbus_dV.py#L19 | Computes partial derivatives of power injection w.r.t. voltage. | 输入：Ybus, V；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | issparse；dSbus_dV_sparse；dSbus_dV_dense | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.dSbus_dV.dSbus_dV_dense | (Ybus, V) | pandapower/pypower/dSbus_dV.py#L40 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pypower.dSbus_dV.dSbus_dV_dense 的实现与调用链确认。 | 输入：Ybus, V；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | asarray；diag；conj；flatten；abs | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.dSbus_dV.dSbus_dV_sparse | (Ybus, V) | pandapower/pypower/dSbus_dV.py#L29 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pypower.dSbus_dV.dSbus_dV_sparse 的实现与调用链确认。 | 输入：Ybus, V；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | range；sparse；len；conj；abs | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
