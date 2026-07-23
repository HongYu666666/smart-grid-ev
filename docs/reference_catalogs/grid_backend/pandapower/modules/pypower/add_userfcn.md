# `pandapower.pypower.add_userfcn`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.add_userfcn.add_userfcn | (ppc, stage, fcn, args=None, allow_multiple=False) | pandapower/pypower/add_userfcn.py#L10 | Appends a userfcn to the list to be called for a case. | 输入：ppc, stage, fcn, args, allow_multiple；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | append；stderr.write；len；range | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
