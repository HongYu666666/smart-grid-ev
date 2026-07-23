# `pandapower.create.ext_grid_create`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.create.ext_grid_create.create_ext_grid | (net: pandapowerNet, bus: Int, vm_pu: float=1.0, va_degree: float=0.0, name: str \| None=None, in_service: bool=True, s_sc_max_mva: float=nan, s_sc_min_mva: float=nan, rx_max: float=nan, rx_min: float=nan, max_p_mw: float=nan, min_p_mw: float=nan, max_q_mvar: float=nan, min_q_mvar: float=nan, index: Int \| None=None, r0x0_max: float=nan, x0x_max: float=nan, controllable: bool \| float=nan, slack_weight: float=1.0, **kwargs) -> Int | pandapower/create/ext_grid_create.py#L24 | 校验母线后向 net.ext_grid 写入外部电网/平衡节点及短路和功率边界，返回元件索引。 | 输入：net, bus, vm_pu, va_degree, name, in_service, s_sc_max_mva, s_sc_min_mva, rx_max, rx_min, max_p_mw, min_p_mw, max_q_mvar, min_q_mvar, index, r0x0_max, x0x_max, controllable, slack_weight, **kwargs；输出：Int | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | _check_element；_get_index_with_check；_set_entries；_set_value_if_not_nan | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 人工复核 |
