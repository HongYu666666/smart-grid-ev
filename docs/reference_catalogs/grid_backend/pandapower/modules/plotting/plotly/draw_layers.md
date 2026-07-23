# `pandapower.plotting.plotly.draw_layers`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.plotting.plotly.draw_layers.draw_layers | (traces, num_layers=0, on_map=False, map_style='basic', showlegend=True, figsize=1, aspectratio='auto', filename=None, auto_open=True, **kwargs) | pandapower/plotting/plotly/draw_layers.py#L45 | plots all the traces (which can be created using :func:`create_bus_trace`, :func:`create_line_trace`, :func:`create_trafo_trace`) to PLOTLY (see https://plot.ly/python/) | 输入：traces, num_layers, on_map, map_style, showlegend, figsize, aspectratio, filename, auto_open, **kwargs；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | Figure；kwargs.get；_in_ipynb；fig.add_annotation；init_notebook_mode；_on_map_test；logger.warning；Layout；kwargs.pop；dropna；np.array；max；plot；trace.keys；trace.pop；isinstance | 仅内部参考：不进入首轮后端适配器 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.plotting.plotly.draw_layers.version_check | () | pandapower/plotting/plotly/draw_layers.py#L34 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.plotting.plotly.draw_layers.version_check 的实现与调用链确认。 | 输入：无显式输入；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | UserWarning；version.parse；locals；globals | 仅内部参考：不进入首轮后端适配器 | 源码确认（静态 AST） | 自动生成 |
