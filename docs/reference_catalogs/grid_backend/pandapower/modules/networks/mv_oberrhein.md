# `pandapower.networks.mv_oberrhein`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.networks.mv_oberrhein.mv_oberrhein | (scenario='load', cosphi_load=0.98, cosphi_pv=1.0, include_substations=False, separation_by_sub=False, **kwargs) | pandapower/networks/mv_oberrhein.py#L19 | Loads the Oberrhein network, a generic 20 kV network serviced by two 25 MVA HV/MV transformer stations. The network supplies 141 MV/LV substations and 6 MV loads through four MV feeders. The network layout is meshed, but the network is operated as a radial network with 6 open sectioning points. | 输入：scenario, cosphi_load, cosphi_pv, include_substations, separation_by_sub, **kwargs；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | astype；runpp；from_json；np.tan；create_nxgraph；select_subnet；os.path.join；np.arccos；ValueError；list；connected_components | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
