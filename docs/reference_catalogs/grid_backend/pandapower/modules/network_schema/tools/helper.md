# `pandapower.network_schema.tools.helper`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.network_schema.tools.helper.create_docu_csv_from_schema | (schema: pa.DataFrameSchema) | pandapower/network_schema/tools/helper.py#L42 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.network_schema.tools.helper.create_docu_csv_from_schema 的实现与调用链确认。 | 输入：schema；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | schema.to_json；json.loads；items；pd.DataFrame；pd.set_option；print；df.to_csv；columns_info.append；col_details.get；get_checks；_get_metadata | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.network_schema.tools.helper.get_dtypes | (schema: pa.DataFrameSchema, required_only: bool=True) -> dict | pandapower/network_schema/tools/helper.py#L4 | Extract column data types from a Pandera DataFrame schema. | 输入：schema, required_only；输出：dict | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | schema.columns.items | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
