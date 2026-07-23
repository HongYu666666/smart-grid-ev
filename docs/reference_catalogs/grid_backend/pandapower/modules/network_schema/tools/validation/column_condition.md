# `pandapower.network_schema.tools.validation.column_condition`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.network_schema.tools.validation.column_condition.create_lower_equals_column_check | (first_element: str, second_element: str) -> pa.Check | pandapower/network_schema/tools/validation/column_condition.py#L5 | Create a Pandera check that validates one column is less than or equal to another. | 输入：first_element, second_element；输出：pa.Check | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | pa.Check；all；fillna | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
