# `pandapower.pypower.makeB`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.makeB.makeB | (baseMVA, bus, branch, alg) | pandapower/pypower/makeB.py#L15 | Builds the FDPF matrices, B prime and B double prime. | 输入：baseMVA, bus, branch, alg；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | copy；zeros；ones；makeYbus | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
