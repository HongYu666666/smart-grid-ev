# `pandapower.networks.lv_schutterwald`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.networks.lv_schutterwald.lv_schutterwald | (separation_by_sub=False, include_heat_pumps=False, **kwargs) | pandapower/networks/lv_schutterwald.py#L17 | Loads the Schutterwald network, a generic 0.4 kV network serviced by 14 MV/LV transformer stations of the Oberrhein network. The network supplies 1506 customers with the option of including 1251 heat pumps. | 输入：separation_by_sub, include_heat_pumps, **kwargs；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | from_json；runpp；os.path.join；drop_elements；create_nxgraph；enumerate；list；select_subnet；subnets.append；connected_components | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
