# `pandapower.plotting.plotly.mapbox_plot`

本模块共记录 3 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.plotting.plotly.mapbox_plot._get_mapbox_token | () | pandapower/plotting/plotly/mapbox_plot.py#L50 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.plotting.plotly.mapbox_plot._get_mapbox_token 的实现与调用链确认。 | 输入：无显式输入；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | deprecated；os.path.join；open；mapbox_file.read | 仅内部参考：不进入首轮后端适配器 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.plotting.plotly.mapbox_plot._on_map_test | (x, y) | pandapower/plotting/plotly/mapbox_plot.py#L13 | checks if bus_geodata can be located on a map using geopy | 输入：x, y；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | Nominatim；geolocator.reverse；ImportError；logger.error | 仅内部参考：不进入首轮后端适配器 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.plotting.plotly.mapbox_plot.set_mapbox_token | (token) | pandapower/plotting/plotly/mapbox_plot.py#L41 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.plotting.plotly.mapbox_plot.set_mapbox_token 的实现与调用链确认。 | 输入：token；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | deprecated；os.path.join；open；mapbox_file.write | 仅内部参考：不进入首轮后端适配器 | 源码确认（静态 AST） | 自动生成 |
