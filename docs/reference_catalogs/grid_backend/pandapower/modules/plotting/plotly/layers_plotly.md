# `pandapower.plotting.plotly.layers_plotly`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.plotting.plotly.layers_plotly.layers_plotly | (net, bus_groups, respect_switches=True, use_line_geo=None, colors_dict=None, on_map=False, map_style='basic', figsize=1, aspectratio='auto', line_width=2, bus_size=10, auto_open=True) | pandapower/plotting/plotly/layers_plotly.py#L12 | Plot pandapower network buses grouped into layers in plotly If no geodata is available, artificial geodata is generated. For advanced plotting see the tutorial | 输入：net, bus_groups, respect_switches, use_line_geo, colors_dict, on_map, map_style, figsize, aspectratio, line_width, bus_size, auto_open；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | create_nxgraph；connected_components；pd.Series；unique_layers.sort_values；unique_layers.reset_index；range；len；get_plotly_color_palette；layers.items；vlev_bus_dict.items；create_trafo_trace；draw_layers；vlev_bus_dict.get；unique；set；dict | 仅内部参考：不进入首轮后端适配器 | 源码确认（静态 AST） | 自动生成 |
