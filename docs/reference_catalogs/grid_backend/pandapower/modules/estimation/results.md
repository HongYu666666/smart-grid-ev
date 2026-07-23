# `pandapower.estimation.results`

本模块共记录 3 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.estimation.results._calc_power_flow | (ppci, V) | pandapower/estimation/results.py#L15 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.estimation.results._calc_power_flow 的实现与调用链确认。 | 输入：ppci, V；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | _get_pf_variables_from_ppci；pfsoln；np.multiply；np.conj | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.estimation.results._extract_result_ppci_to_pp | (net, ppc, ppci) | pandapower/estimation/results.py#L31 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.estimation.results._extract_result_ppci_to_pp 的实现与调用链确认。 | 输入：net, ppc, ppci；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | _copy_results_ppci_to_ppc；init_results；_extract_results_se；get_values；np.nonzero | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.estimation.results.eppci2pp | (net, ppc, eppci) | pandapower/estimation/results.py#L79 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.estimation.results.eppci2pp 的实现与调用链确认。 | 输入：net, ppc, eppci；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | _calc_power_flow；_extract_result_ppci_to_pp | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
