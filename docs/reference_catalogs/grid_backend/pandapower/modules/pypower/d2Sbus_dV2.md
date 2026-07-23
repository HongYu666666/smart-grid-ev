# `pandapower.pypower.d2Sbus_dV2`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.d2Sbus_dV2.d2Sbus_dV2 | (Ybus, V, lam) | pandapower/pypower/d2Sbus_dV2.py#L12 | Computes 2nd derivatives of power injection w.r.t. voltage. | 输入：Ybus, V, lam；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | len；arange；sparse；conj；Ybus.T.conjugate；diagV.conj；ones；abs | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
