# `pandapower.pypower.pipsopf_solver`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.pipsopf_solver.pipsopf_solver | (om, ppopt, out_opt=None) | pandapower/pypower/pipsopf_solver.py#L29 | Solves AC optimal power flow using PIPS. | 输入：om, ppopt, out_opt；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | om.get_ppc；om.get_idx；om.getN；om.linear_constraints；om.getv；makeYbus；find；len；pips；zeros；opf_costfcn；opf_consfcn；opf_hessfcn；exp；astype；conj | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
