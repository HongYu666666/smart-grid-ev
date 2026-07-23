# `pandapower.create.network_create`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.create.network_create.create_empty_network | (name: str='', f_hz: float=50.0, sn_mva: float=1, add_stdtypes: bool=True) -> pandapowerNet | pandapower/create/network_create.py#L18 | 按频率和基准容量创建空 pandapowerNet、初始化结构表/标准类型并清空各求解模式结果表。 | 输入：name, f_hz, sn_mva, add_stdtypes；输出：pandapowerNet | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | get_structure_dict；pandapowerNet；pandapowerNet.create_dataframes；add_basic_std_types；reset_results | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 人工复核 |
