# `pandapower.optimal_powerflow`

本模块共记录 3 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.optimal_powerflow._add_dcline_constraints | (om, net) | pandapower/optimal_powerflow.py#L86 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.optimal_powerflow._add_dcline_constraints 的实现与调用链确认。 | 输入：om, net；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | om.get_ppc；net.dcline.in_service.sum；sparse；enumerate；om.add_constraints；zip | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.optimal_powerflow._optimal_powerflow | (net, verbose, suppress_warnings, **kwargs) | pandapower/optimal_powerflow.py#L29 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.optimal_powerflow._optimal_powerflow 的实现与调用链确认。 | 输入：net, verbose, suppress_warnings, **kwargs；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | ppoption；_add_auxiliary_elements；_pd2ppc；_copy_results_ppci_to_ppc；_extract_results；_clean_up；logger.error；verify_results；init_results；len；add_userfcn；_run_pf_before_opf；opf；printpf；OPFNotConverged；warnings.catch_warnings | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.optimal_powerflow._run_pf_before_opf | (net, ppci) | pandapower/optimal_powerflow.py#L112 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.optimal_powerflow._run_pf_before_opf 的实现与调用链确认。 | 输入：net, ppci；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | _run_newton_raphson_pf | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
