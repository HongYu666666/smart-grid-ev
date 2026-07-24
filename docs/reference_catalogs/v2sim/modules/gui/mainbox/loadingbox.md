# `v2sim.gui.mainbox.loadingbox`

本模块共记录 3 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| class | v2sim.gui.mainbox.loadingbox.LoadingBox | class(Toplevel) | v2sim/gui/mainbox/loadingbox.py#L7 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.mainbox.loadingbox.LoadingBox 的实现与调用链确认。 | 输入：构造参数由 __init__ 或工厂函数定义；输出：类实例 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | __init__；self.title；self.geometry；self.attributes；self.columnconfigure；enumerate；configure；grid；self.cks.append；self.rowconfigure；self._pQ.delegate；super；Label | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.gui.mainbox.loadingbox.LoadingBox.__init__ | (self, items: List[str], parentQ: EventQueue, **kwargs) | v2sim/gui/mainbox/loadingbox.py#L8 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.mainbox.loadingbox.LoadingBox.__init__ 的实现与调用链确认。 | 输入：items, parentQ, **kwargs；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | __init__；self.title；self.geometry；self.attributes；self.columnconfigure；enumerate；grid；self.cks.append；self.rowconfigure；super；Label | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.gui.mainbox.loadingbox.LoadingBox.setText | (self, itm: str, val: str) | v2sim/gui/mainbox/loadingbox.py#L26 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.mainbox.loadingbox.LoadingBox.setText 的实现与调用链确认。 | 输入：itm, val；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | configure；self._pQ.delegate | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
