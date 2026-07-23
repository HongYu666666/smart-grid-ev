# `pandapower.pypower.opf_hessfcn`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.opf_hessfcn.opf_hessfcn | (x, lmbda, om, Ybus, Yf, Yt, ppopt, il=None, cost_mult=1.0) | pandapower/pypower/opf_hessfcn.py#L29 | Evaluates Hessian of Lagrangian for AC OPF. | 输入：x, lmbda, om, Ybus, Yf, Yt, ppopt, il, cost_mult；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | om.get_ppc；om.get_cost_params；om.get_idx；len；zeros；find；qcost.any；sparse；d2Sbus_dV2；vstack；arange；exp；array；issparse；astype；dSbr_dV | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
