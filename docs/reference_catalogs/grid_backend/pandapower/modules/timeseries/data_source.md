# `pandapower.timeseries.data_source`

本模块共记录 4 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| class | pandapower.timeseries.data_source.DataSource | class(JSONSerializableClass) | pandapower/timeseries/data_source.py#L16 | The DataSource class is a skeleton for data sources such as pandas DataFrames Controllers call get_time_step_values(time) in each time step to get values from the data source | 输入：构造参数由 __init__ 或工厂函数定义；输出：类实例 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | NotImplementedError | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| method | pandapower.timeseries.data_source.DataSource.__repr__ | (self) | pandapower/timeseries/data_source.py#L25 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.timeseries.data_source.DataSource.__repr__ 的实现与调用链确认。 | 输入：无显式输入；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | 静态扫描未发现直接函数调用 | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| method | pandapower.timeseries.data_source.DataSource.__str__ | (self) | pandapower/timeseries/data_source.py#L22 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.timeseries.data_source.DataSource.__str__ 的实现与调用链确认。 | 输入：无显式输入；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | 静态扫描未发现直接函数调用 | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| method | pandapower.timeseries.data_source.DataSource.get_time_step_value | (self, time_step, profile_name, scale_factor=1.0) | pandapower/timeseries/data_source.py#L28 | This method retrieves values of the data source according to the given parameters. For actual parameters look into the DataSource you are actually using. | 输入：time_step, profile_name, scale_factor；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | NotImplementedError | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
