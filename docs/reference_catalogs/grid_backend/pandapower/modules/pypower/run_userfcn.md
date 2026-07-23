# `pandapower.pypower.run_userfcn`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.run_userfcn.run_userfcn | (userfcn, stage, *args2) | pandapower/pypower/run_userfcn.py#L9 | Runs the userfcn callbacks for a given stage. | 输入：userfcn, stage, *args2；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | range；len | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
