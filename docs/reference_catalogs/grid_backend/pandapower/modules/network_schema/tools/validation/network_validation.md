# `pandapower.network_schema.tools.validation.network_validation`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.network_schema.tools.validation.network_validation.validate_network | (net: pandapowerNet) | pandapower/network_schema/tools/validation/network_validation.py#L14 | Validate pandapower network element dataframes using schemas from the schema folder. | 输入：net；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | importlib.util.spec_from_file_location；importlib.util.module_from_spec；loader.exec_module；Path；getattr；_bus_index_validation；logger.warning；os.path.exists；_dynamic_import；schema.validate；pa.errors.SchemaError | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
