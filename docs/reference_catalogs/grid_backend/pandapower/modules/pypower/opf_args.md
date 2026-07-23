# `pandapower.pypower.opf_args`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.opf_args.opf_args | (ppc, ppopt) | pandapower/pypower/opf_args.py#L22 | Parses and initializes OPF input arguments. | 输入：ppc, ppopt；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | array；stderr.write；ppoption；issparse；len | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pypower.opf_args.opf_args2 | (ppc, ppopt) | pandapower/pypower/opf_args.py#L158 | Parses and initializes OPF input arguments. | 输入：ppc, ppopt；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | opf_args；len | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
