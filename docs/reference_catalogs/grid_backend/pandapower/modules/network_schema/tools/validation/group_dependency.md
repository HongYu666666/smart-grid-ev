# `pandapower.network_schema.tools.validation.group_dependency`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.network_schema.tools.validation.group_dependency.create_column_dependency_checks_from_metadata | (names: list, schema_columns: dict) -> list | pandapower/network_schema/tools/validation/group_dependency.py#L85 | Create dependency validation checks for columns based on their metadata. | 输入：names, schema_columns；输出：list | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | len；checks.append；schema_columns.items；pa.Check；getattr；col_schema.metadata.get；create_column_group_dependency_validation_func | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.network_schema.tools.validation.group_dependency.create_column_group_dependency_validation_func | (columns) | pandapower/network_schema/tools/validation/group_dependency.py#L5 | Creates a validator function that ensures column group dependency. | 输入：columns；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | set；list；isna；na_mask.sum；all；len | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
