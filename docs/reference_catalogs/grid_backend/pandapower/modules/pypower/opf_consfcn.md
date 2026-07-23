# `pandapower.pypower.opf_consfcn`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.opf_consfcn.opf_consfcn | (x, om, Ybus, Yf, Yt, ppopt, il=None, *args) | pandapower/pypower/opf_consfcn.py#L21 | Evaluates nonlinear constraints and their Jacobian for OPF. | 输入：x, om, Ybus, Yf, Yt, ppopt, il, *args；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | om.get_ppc；om.get_idx；len；makeSbus；arange；dSbus_dV；sparse；lil_matrix；vstack；exp；zeros；dAbr_dV；conj；hstack；dIbr_dV；dSbr_dV | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
