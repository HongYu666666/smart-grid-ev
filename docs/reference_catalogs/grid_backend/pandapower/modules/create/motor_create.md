# `pandapower.create.motor_create`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.create.motor_create.create_motor | (net: pandapowerNet, bus: Int, pn_mech_mw: float, cos_phi: float, efficiency_percent: float=100.0, loading_percent: float=100.0, name: str \| None=None, lrc_pu: float=nan, scaling: float=1.0, vn_kv: float=nan, rx: float=nan, index: Int \| None=None, in_service: bool=True, cos_phi_n: float=nan, efficiency_n_percent: float=nan, **kwargs) -> Int | pandapower/create/motor_create.py#L18 | Adds a motor to the network. | 输入：net, bus, pn_mech_mw, cos_phi, efficiency_percent, loading_percent, name, lrc_pu, scaling, vn_kv, rx, index, in_service, cos_phi_n, efficiency_n_percent, **kwargs；输出：Int | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | _check_element；_get_index_with_check；_set_entries | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
