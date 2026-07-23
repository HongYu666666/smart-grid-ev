# `pandapower.opf.pm_storage`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.opf.pm_storage.add_storage_opf_settings | (net, ppci, pm) | pandapower/opf/pm_storage.py#L3 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.opf.pm_storage.add_storage_opf_settings 的实现与调用链确认。 | 输入：net, ppci, pm；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | item；int；str | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.opf.pm_storage.read_pm_storage_results | (net) | pandapower/opf/pm_storage.py#L56 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.opf.pm_storage.read_pm_storage_results 的实现与调用链确认。 | 输入：net；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | list；net.res_ts_opt.keys；pd.DataFrame；str | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
