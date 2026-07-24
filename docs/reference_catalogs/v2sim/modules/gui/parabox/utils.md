# `v2sim.gui.parabox.utils`

本模块共记录 5 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| class | v2sim.gui.parabox.utils.RedirectStdout | class | v2sim/gui/parabox/utils.py#L12 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.parabox.utils.RedirectStdout 的实现与调用链确认。 | 输入：构造参数由 __init__ 或工厂函数定义；输出：类实例 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | self.q.put | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.gui.parabox.utils.RedirectStdout.__init__ | (self, q: mp.Queue, id: int) | v2sim/gui/parabox/utils.py#L13 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.parabox.utils.RedirectStdout.__init__ 的实现与调用链确认。 | 输入：q, id；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | 静态扫描未发现直接函数调用 | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.gui.parabox.utils.RedirectStdout.flush | (self) | v2sim/gui/parabox/utils.py#L20 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.parabox.utils.RedirectStdout.flush 的实现与调用链确认。 | 输入：无显式输入；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | 静态扫描未发现直接函数调用 | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.gui.parabox.utils.RedirectStdout.write | (self, text) | v2sim/gui/parabox/utils.py#L17 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.parabox.utils.RedirectStdout.write 的实现与调用链确认。 | 输入：text；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | self.q.put | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | v2sim.gui.parabox.utils.work | (root: str, par: Dict[str, Any], alt: Dict[str, str], out: str, recv: RedirectStdout) | v2sim/gui/parabox/utils.py#L24 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.parabox.utils.work 的实现与调用链确认。 | 输入：root, par, alt, out, recv；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | par.update；time.time；AltCommand；work；recv.q.put_nowait；int；ClientOptions；MsgPack；alt.items | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
