# `v2sim.gui.progbox`

本模块共记录 5 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| class | v2sim.gui.progbox.ProgBox | class(Tk) | v2sim/gui/progbox/__init__.py#L5 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.progbox.ProgBox 的实现与调用链确认。 | 输入：构造参数由 __init__ 或工厂函数定义；输出：类实例 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | __init__；self.title；self.geometry；Treeview；tree.heading；tree.column；tree.pack；Queue；self.after；d.items；self.destroy；self._Q.put；tree.insert；self._Q.empty；d.update；super | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.gui.progbox.ProgBox.__init__ | (self, keys: List[str], title: str='Progress Box', width: int=300, height: int=500) | v2sim/gui/progbox/__init__.py#L6 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.progbox.ProgBox.__init__ 的实现与调用链确认。 | 输入：keys, title, width, height；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | __init__；self.title；self.geometry；Treeview；tree.heading；tree.column；tree.pack；Queue；self.after；tree.insert；super | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.gui.progbox.ProgBox._upd | (self) | v2sim/gui/progbox/__init__.py#L28 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.progbox.ProgBox._upd 的实现与调用链确认。 | 输入：无显式输入；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | d.items；self.after；self._Q.empty；d.update；self._Q.get；self.tree.insert；self.tree.item；str | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.gui.progbox.ProgBox.close | (self) | v2sim/gui/progbox/__init__.py#L41 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.progbox.ProgBox.close 的实现与调用链确认。 | 输入：无显式输入；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | self.destroy | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.gui.progbox.ProgBox.set_val | (self, d: Dict[str, Any]) | v2sim/gui/progbox/__init__.py#L44 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.progbox.ProgBox.set_val 的实现与调用链确认。 | 输入：d；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | self._Q.put | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
