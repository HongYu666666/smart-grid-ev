# `pandapower.pypower.gausspf`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.gausspf.gausspf | (Ybus, Sbus, V0, ref, pv, pq, ppopt=None) | pandapower/pypower/gausspf.py#L15 | Solves the power flow using a Gauss-Seidel method. | 输入：Ybus, Sbus, V0, ref, pv, pq, ppopt；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | V0.copy；abs；len；linalg.norm；ppoption；sys.stdout.write；conj；list；range；tmp.item | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
