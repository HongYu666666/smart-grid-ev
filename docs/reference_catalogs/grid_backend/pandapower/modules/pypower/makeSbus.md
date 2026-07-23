# `pandapower.pypower.makeSbus`

本模块共记录 4 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.makeSbus._get_Cg | (gen_on, bus) | pandapower/pypower/makeSbus.py#L40 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pypower.makeSbus._get_Cg 的实现与调用链确认。 | 输入：gen_on, bus；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | sparse；ones；range | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.makeSbus._get_Sbus | (baseMVA, bus, gen_on, Cg, vm=None) | pandapower/pypower/makeSbus.py#L16 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pypower.makeSbus._get_Sbus 的实现与调用链确认。 | 输入：baseMVA, bus, gen_on, Cg, vm；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | _get_Sload | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.makeSbus._get_Sload | (bus, vm) | pandapower/pypower/makeSbus.py#L23 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pypower.makeSbus._get_Sload 的实现与调用链确认。 | 输入：bus, vm；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | 静态扫描未发现直接函数调用 | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.makeSbus.makeSbus | (baseMVA, bus, gen, vm=None) | pandapower/pypower/makeSbus.py#L49 | Builds the vector of complex bus power injections. | 输入：baseMVA, bus, gen, vm；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | find；_get_Cg；_get_Sbus | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
