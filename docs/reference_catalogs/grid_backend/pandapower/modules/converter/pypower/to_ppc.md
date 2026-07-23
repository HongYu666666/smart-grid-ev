# `pandapower.converter.pypower.to_ppc`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.converter.pypower.to_ppc.to_ppc | (net, calculate_voltage_angles=True, trafo_model='t', switch_rx_ratio=2, check_connectivity=True, voltage_depend_loads=False, init='results', mode=None, take_slack_vm_limits=True) | pandapower/converter/pypower/to_ppc.py#L18 | This function converts a pandapower net to a pypower case file. | 输入：net, calculate_voltage_angles, trafo_model, switch_rx_ratio, check_connectivity, voltage_depend_loads, init, mode, take_slack_vm_limits；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | _add_ppc_options；_pd2ppc；zip；delete；_check_necessary_opf_parameters；logger.error；any；min；get_loc；UserWarning；len；net.bus.index.difference；ValueError；allclose；tolist | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
