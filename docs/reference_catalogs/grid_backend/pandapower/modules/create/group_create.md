# `pandapower.create.group_create`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.create.group_create.create_group | (net: pandapowerNet, element_types, element_indices, name: str='', reference_columns=None, index: int \| None=None, **kwargs) | pandapower/create/group_create.py#L23 | Add a new group to net['group'] dataframe. | 输入：net, element_types, element_indices, name, reference_columns, index, **kwargs；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | _group_parameter_list；_check_elements_existence；np.array；_set_multiple_entries；len；_get_index_with_check | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.create.group_create.create_group_from_dict | (net, elements_dict, name: str='', reference_column=None, index: int \| None=None, **kwargs) | pandapower/create/group_create.py#L79 | Wrapper function of :func:`create_group`. | 输入：net, elements_dict, name, reference_column, index, **kwargs；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | create_group；elements_dict.keys；elements_dict.values | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
