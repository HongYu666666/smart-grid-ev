# `pandapower.pf.iwamoto_multiplier`

本模块共记录 3 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pf.iwamoto_multiplier._evaluate_Yx | (Ybus, V, pv, pq) | pandapower/pf/iwamoto_multiplier.py#L46 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pf.iwamoto_multiplier._evaluate_Yx 的实现与调用链确认。 | 输入：Ybus, V, pv, pq；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | conj | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pf.iwamoto_multiplier._get_iwamoto_multiplier | (Ybus, J, F, dV, dx, pq, pv) | pandapower/pf/iwamoto_multiplier.py#L24 | Calculates the iwamato multiplier to increase convergence | 输入：Ybus, J, F, dV, dx, pq, pv；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | c0.dot；print；_evaluate_Yx；c1.dot；c2.dot；roots | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pf.iwamoto_multiplier._iwamoto_step | (Ybus, J, F, dx, pq, npv, npq, dVa, dVm, Vm, Va, pv, j1, j2, j3, j4, j5, j6) | pandapower/pf/iwamoto_multiplier.py#L9 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pf.iwamoto_multiplier._iwamoto_step 的实现与调用链确认。 | 输入：Ybus, J, F, dx, pq, npv, npq, dVa, dVm, Vm, Va, pv, j1, j2, j3, j4, j5, j6；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | _get_iwamoto_multiplier；exp | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
