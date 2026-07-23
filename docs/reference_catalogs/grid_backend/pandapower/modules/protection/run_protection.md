# `pandapower.protection.run_protection`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.protection.run_protection.calculate_protection_times | (net, scenario='sc') | pandapower/protection/run_protection.py#L3 | Calculate protection times for short-circuit and power-flow scenarios | 输入：net, scenario；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | pd.DataFrame.from_dict；ValueError；p.protection_function；protection_results.append | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
