# `pandapower.pypower.dcopf_solver`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.dcopf_solver.dcopf_solver | (om, ppopt, out_opt=None) | pandapower/pypower/dcopf_solver.py#L32 | Solves a DC optimal power flow. | 输入：om, ppopt, out_opt；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | om.get_ppc；om.get_cost_params；array；om.userdata；om.get_idx；find；om.getN；om.linear_constraints；om.getv；int；len；zeros；dot；vstack；sparse；qps_pypower | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
