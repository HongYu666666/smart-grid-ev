# `pandapower.create.measurement_create`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.create.measurement_create.create_measurement | (net: pandapowerNet, meas_type: MeasurementType, element_type: MeasurementElementType, value: float, std_dev: float, element: int, side: int \| Literal['from', 'to'] \| Literal['hv', 'mv', 'lv'] \| None=None, check_existing: bool=False, index: Int \| None=None, name: str \| None=None, **kwargs) -> Int | pandapower/create/measurement_create.py#L20 | Creates a measurement, which is used by the estimation module. Possible types of measurements are: v, p, q, i, va, ia | 输入：net, meas_type, element_type, value, std_dev, element, side, check_existing, index, name, **kwargs；输出：Int | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | _get_index_with_check；_set_entries；UserWarning；meas_type.lower；len；pd.isnull | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
