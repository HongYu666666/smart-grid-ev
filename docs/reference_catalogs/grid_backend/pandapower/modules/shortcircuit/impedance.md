# `pandapower.shortcircuit.impedance`

本模块共记录 4 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.shortcircuit.impedance._calc_rx | (net, ppci, bus_idx) | pandapower/shortcircuit/impedance.py#L23 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.shortcircuit.impedance._calc_rx 的实现与调用链确认。 | 输入：net, ppci, bus_idx；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | np.square；_calc_zbus_diag；np.diag | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.shortcircuit.impedance._calc_ybus | (ppci) | pandapower/shortcircuit/impedance.py#L43 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.shortcircuit.impedance._calc_ybus 的实现与调用链确认。 | 输入：ppci；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | makeYbus；any；ValueError；np.isnan | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.shortcircuit.impedance._calc_zbus | (net, ppci) | pandapower/shortcircuit/impedance.py#L52 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.shortcircuit.impedance._calc_zbus 的实现与调用链确认。 | 输入：net, ppci；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | inv；_clean_up；warnings.catch_warnings；warnings.simplefilter；toarray；Ybus.toarray；inv_sparse | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.shortcircuit.impedance._calc_zbus_diag | (net, ppci, bus_idx=None) | pandapower/shortcircuit/impedance.py#L67 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.shortcircuit.impedance._calc_zbus_diag 的实现与调用链确认。 | 输入：net, ppci, bus_idx；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | np.zeros；range；enumerate；ybus_fact | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
