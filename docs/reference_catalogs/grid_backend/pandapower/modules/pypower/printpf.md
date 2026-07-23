# `pandapower.pypower.printpf`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.printpf.printpf | (baseMVA, bus=None, gen=None, branch=None, f=None, success=None, et=None, fd=None, ppopt=None) | pandapower/pypower/printpf.py#L28 | Prints power flow results. | 输入：baseMVA, bus, gen, branch, f, success, et, fd, ppopt；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | isinstance；astype；zeros；arange；find；ones；sort；len；exp；fd.write；min；argmin；max；argmax；range；any | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
