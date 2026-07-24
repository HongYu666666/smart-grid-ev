# `v2sim.gui.viewerbox.srd`

本模块共记录 5 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| class | v2sim.gui.viewerbox.srd.SelectResultsDialog | class(SelectItemDialog) | v2sim/gui/viewerbox/srd.py#L21 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.viewerbox.srd.SelectResultsDialog 的实现与调用链确认。 | 输入：构造参数由 __init__ 或工厂函数定义；输出：类实例 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | __init__；self.tree.column；get_clog_mtime；new_items.append；item.absolute；super；_L；format_time | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.gui.viewerbox.srd.SelectResultsDialog.__init__ | (self, items: List[Path]) | v2sim/gui/viewerbox/srd.py#L22 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.viewerbox.srd.SelectResultsDialog.__init__ 的实现与调用链确认。 | 输入：items；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | __init__；self.tree.column；get_clog_mtime；new_items.append；item.absolute；super；_L；format_time | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.gui.viewerbox.srd.SelectResultsDialog.folder | (self) -> Union[Path, None] | v2sim/gui/viewerbox/srd.py#L35 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.viewerbox.srd.SelectResultsDialog.folder 的实现与调用链确认。 | 输入：无显式输入；输出：Union[Path, None] | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | 静态扫描未发现直接函数调用 | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | v2sim.gui.viewerbox.srd.format_time | (ts) | v2sim/gui/viewerbox/srd.py#L15 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.viewerbox.srd.format_time 的实现与调用链确认。 | 输入：ts；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | strftime；_L；datetime.datetime.fromtimestamp | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | v2sim.gui.viewerbox.srd.get_clog_mtime | (folder: Path) | v2sim/gui/viewerbox/srd.py#L8 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.viewerbox.srd.get_clog_mtime 的实现与调用链确认。 | 输入：folder；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | clog_path.is_file；clog_path.stat | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
