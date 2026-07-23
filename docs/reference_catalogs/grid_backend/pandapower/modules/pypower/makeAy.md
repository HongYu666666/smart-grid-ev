# `pandapower.pypower.makeAy`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.makeAy.makeAy | (baseMVA, ng, gencost, pgbas, qgbas, ybas) | pandapower/pypower/makeAy.py#L15 | Make the A matrix and RHS for the CCV formulation. | 输入：baseMVA, ng, gencost, pgbas, qgbas, ybas；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | find；sum；sparse；array；zeros；astype；any；enumerate；range；Ay.tocsr；diff；print | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
