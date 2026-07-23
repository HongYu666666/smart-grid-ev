# `pandapower.pypower.qps_pypower`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.qps_pypower.qps_pypower | (H, c=None, A=None, l=None, u=None, xmin=None, xmax=None, x0=None, opt=None) | pandapower/pypower/qps_pypower.py#L19 | Quadratic Program Solver for PYPOWER. | 输入：H, c, A, l, u, xmin, xmax, x0, opt；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | qps_pips | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
