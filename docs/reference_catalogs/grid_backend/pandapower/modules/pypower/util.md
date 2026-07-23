# `pandapower.pypower.util`

本模块共记录 3 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.util.feval | (func, *args, **kw_args) | pandapower/pypower/util.py#L22 | Evaluates the function C{func} using positional arguments C{args} and keyword arguments C{kw_args}. | 输入：func, *args, **kw_args；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | eval | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.util.have_fcn | (name) | pandapower/pypower/util.py#L29 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pypower.util.have_fcn 的实现与调用链确认。 | 输入：name；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | __import__ | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.util.sub2ind | (shape, I, J, row_major=False) | pandapower/pypower/util.py#L11 | Returns the linear indices of subscripts | 输入：shape, I, J, row_major；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | ind.astype | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
