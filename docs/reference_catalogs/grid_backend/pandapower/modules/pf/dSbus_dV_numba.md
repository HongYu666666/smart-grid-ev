# `pandapower.pf.dSbus_dV_numba`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pf.dSbus_dV_numba.dSbus_dV | (Ybus, V, I=None) | pandapower/pf/dSbus_dV_numba.py#L71 | Calls functions to calculate dS/dV depending on whether Ybus is sparse or not | 输入：Ybus, V, I；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | issparse；dSbus_dV_numba_sparse；dSbus_dV_dense；zeros；sparse；len；abs | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pf.dSbus_dV_numba.dSbus_dV_numba_sparse | (Yx, Yp, Yj, V, Vnorm, Ibus) | pandapower/pf/dSbus_dV_numba.py#L19 | Computes partial derivatives of power injection w.r.t. voltage. | 输入：Yx, Yp, Yj, V, Vnorm, Ibus；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | jit；zeros；Yx.copy；range；len；conj | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
