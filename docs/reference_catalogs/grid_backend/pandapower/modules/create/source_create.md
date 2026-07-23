# `pandapower.create.source_create`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.create.source_create.create_source_dc | (net: pandapowerNet, bus_dc: Int, vm_pu: float=1.0, index: Int \| None=None, name: str \| None=None, in_service: bool=True, type: str \| None=None, **kwargs) | pandapower/create/source_create.py#L17 | Creates a dc voltage source in a dc grid with an adjustable set point | 输入：net, bus_dc, vm_pu, index, name, in_service, type, **kwargs；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | _check_element；_get_index_with_check；_set_entries | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
