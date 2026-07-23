# `pandapower.shortcircuit.kappa`

本模块共记录 5 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.shortcircuit.kappa._add_kappa_to_ppc | (net, ppc) | pandapower/shortcircuit/kappa.py#L19 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.shortcircuit.kappa._add_kappa_to_ppc 的实现与调用链确认。 | 输入：net, ppc；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | np.where；_kappa；np.isnan；_kappa_method_c；_kappa_method_b；ValueError | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.shortcircuit.kappa._kappa | (rx) | pandapower/shortcircuit/kappa.py#L37 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.shortcircuit.kappa._kappa 的实现与调用链确认。 | 输入：rx；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | np.exp | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.shortcircuit.kappa._kappa_method_b | (net, ppc) | pandapower/shortcircuit/kappa.py#L78 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.shortcircuit.kappa._kappa_method_b 的实现与调用链确认。 | 输入：net, ppc；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | np.full；np.nonzero；np.clip；len；nxgraph_from_ppc；astype；list；_kappa；nx.all_simple_paths；sum；zip | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.shortcircuit.kappa._kappa_method_c | (net, ppc) | pandapower/shortcircuit/kappa.py#L41 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.shortcircuit.kappa._kappa_method_c 的实现与调用链确认。 | 输入：net, ppc；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | copy.deepcopy；np.nonzero；_calc_ybus；_calc_rx；_kappa；np.ix_；_calc_zbus；factorized；np.arange；ValueError；np.isnan | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.shortcircuit.kappa.nxgraph_from_ppc | (net, ppc) | pandapower/shortcircuit/kappa.py#L106 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.shortcircuit.kappa.nxgraph_from_ppc 的实现与调用链确认。 | 输入：net, ppc；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | nx.MultiGraph；mg.add_nodes_from；mg.add_edges_from；mg.add_node；list；np.size；astype；np.isnan；set；int；zip | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
