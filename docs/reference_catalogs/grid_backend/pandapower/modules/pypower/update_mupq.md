# `pandapower.pypower.update_mupq`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.update_mupq.update_mupq | (baseMVA, gen, mu_PQh, mu_PQl, data) | pandapower/pypower/update_mupq.py#L11 | Updates values of generator limit shadow prices. | 输入：baseMVA, gen, mu_PQh, mu_PQl, data；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | 静态扫描未发现直接函数调用 | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
