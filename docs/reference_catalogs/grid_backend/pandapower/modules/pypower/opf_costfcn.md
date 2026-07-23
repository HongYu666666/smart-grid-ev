# `pandapower.pypower.opf_costfcn`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.opf_costfcn.opf_costfcn | (x, om, return_hessian=False) | pandapower/pypower/opf_costfcn.py#L17 | Evaluates objective function, gradient and Hessian for OPF. | 输入：x, om, return_hessian；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | om.get_ppc；om.get_cost_params；om.get_idx；om.getN；len；find；range；zeros；any；sparse；sum；flatten；issparse；dot；array；polycost | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
