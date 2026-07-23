# `pandapower.pypower.opf_execute`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.opf_execute.opf_execute | (om, ppopt) | pandapower/pypower/opf_execute.py#L32 | Executes the OPF specified by an OPF model object. | 输入：om, ppopt；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | om.build_cost_params；om.get_idx；om.userdata；ppver；stdout.write；dcopf_solver；om.getN；zeros；pipsopf_solver；stderr.write；array；arange；om.compute_cost；len；update_mupq；opf_costfcn | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
