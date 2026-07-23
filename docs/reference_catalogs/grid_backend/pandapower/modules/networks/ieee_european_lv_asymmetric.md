# `pandapower.networks.ieee_european_lv_asymmetric`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.networks.ieee_european_lv_asymmetric.ieee_european_lv_asymmetric | (scenario='on_peak_566', **kwargs) | pandapower/networks/ieee_european_lv_asymmetric.py#L12 | Loads the IEEE European LV network, a generic 0.416 kV network serviced by one 0.8 MVA MV/LV transformer station. The network supplies 906 LV buses and 55 1-PH loads The network layout is mostly radial. | 输入：scenario, **kwargs；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | from_json；os.path.join；ValueError | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
