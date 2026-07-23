# `pandapower.opf.validate_opf_input`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.opf.validate_opf_input._check_necessary_opf_parameters | (net, logger) | pandapower/opf/validate_opf_input.py#L4 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.opf.validate_opf_input._check_necessary_opf_parameters 的实现与调用链确认。 | 输入：net, logger；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | opf_col.items；pd.concat；any；pd.Series；len；logger.info；KeyError；UserWarning；cost_check_df.duplicated；str；net.bus.min_vm_pu.isnull；net.bus.max_vm_pu.isnull；controllable.fillna；missing_val.append；controllable.astype；logger.error | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
