# `pandapower.pf.run_dc_pf`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pf.run_dc_pf._run_dc_pf | (ppci, recycle: dict \| bool=False) | pandapower/pf/run_dc_pf.py#L27 | Runs a decoupled (dc) powerflow to initialize all the values. :param ppci: the internal ppci structure :param recycle: Flag to use results from a previous powerflow | 输入：ppci, recycle；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | perf_counter；np.concatenate；astype；np.unique；np.zeros_like；np.add.at；dcpf；zeros；bincount；real；_store_results_from_pf_in_ppci；isinstance；np.array_equal；_get_pf_variables_from_ppci；makeBdc；np.real | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
