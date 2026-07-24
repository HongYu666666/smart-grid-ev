# `v2sim.gui.mainbox.utils`

本模块共记录 6 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | v2sim.gui.mainbox.utils.errwrapper | (func) | v2sim/gui/mainbox/utils.py#L33 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.mainbox.utils.errwrapper 的实现与调用链确认。 | 输入：func；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | functools.wraps；func；showerr；print；open；f.write；str；traceback.format_exc；type | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | v2sim.gui.mainbox.utils.showerr | (msg: str) | v2sim/gui/mainbox/utils.py#L11 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.mainbox.utils.showerr 的实现与调用链确认。 | 输入：msg；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | MB.showerror | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | v2sim.gui.mainbox.utils.showwarn | (msg: str) | v2sim/gui/mainbox/utils.py#L14 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.mainbox.utils.showwarn 的实现与调用链确认。 | 输入：msg；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | MB.showwarning | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | v2sim.gui.mainbox.utils.try_float | (s: str, name: str) -> float | v2sim/gui/mainbox/utils.py#L21 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.mainbox.utils.try_float 的实现与调用链确认。 | 输入：s, name；输出：float | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | float；ValueError | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | v2sim.gui.mainbox.utils.try_int | (s: str, name: str) -> int | v2sim/gui/mainbox/utils.py#L17 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.mainbox.utils.try_int 的实现与调用链确认。 | 输入：s, name；输出：int | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | int；ValueError | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | v2sim.gui.mainbox.utils.try_split | (s: str, name: str, sep: str=',') -> List[str] | v2sim/gui/mainbox/utils.py#L25 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.gui.mainbox.utils.try_split 的实现与调用链确认。 | 输入：s, name, sep；输出：List[str] | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | s.split；p.strip；ValueError | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
