# `pandapower.networks.create_examples`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.networks.create_examples.example_multivoltage | () | pandapower/networks/create_examples.py#L83 | Returns the multivoltage example network from the pandapower tutorials. | 输入：无显式输入；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | create_empty_network；create_bus；range；pd.DataFrame；hv_lines.iterrows；mv_lines.iterrows；lv_lines.iterrows；get_element_index；create_transformer_from_parameters；create_transformer3w_from_parameters；create_sgen；mv_sgens.iterrows；lv_sgens.iterrows；hv_loads.iterrows；mv_loads.iterrows；lv_loads.iterrows | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.networks.create_examples.example_simple | () | pandapower/networks/create_examples.py#L16 | Returns the simple example network from the pandapower tutorials. | 输入：无显式输入；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | create_empty_network；create_bus；create_ext_grid；create_transformer；create_line；create_switch；create_load；create_gen；create_sgen；create_shunt | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
