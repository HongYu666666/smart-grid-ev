# `v2sim.app.cmd_gen_trip`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | v2sim.app.cmd_gen_trip.main | () | v2sim/app/cmd_gen_trip.py#L11 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.app.cmd_gen_trip.main 的实现与调用链确认。 | 输入：无显式输入；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | ArgChecker；params.pop_bool；print_help；params.pop_str；VTripsFromArgs；print；TrafficGenerator | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | v2sim.app.cmd_gen_trip.print_help | () | v2sim/app/cmd_gen_trip.py#L6 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.app.cmd_gen_trip.print_help 的实现与调用链确认。 | 输入：无显式输入；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | print；sys.exit；Lang.TRIPGEN_HELP_STR.format | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
