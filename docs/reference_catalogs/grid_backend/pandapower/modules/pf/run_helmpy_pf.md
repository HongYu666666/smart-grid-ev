# `pandapower.pf.run_helmpy_pf`

本模块共记录 3 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pf.run_helmpy_pf._build_helm_case | (ppci) | pandapower/pf/run_helmpy_pf.py#L23 | Build a HELMpy :code:`CaseData` object from a pandapower internal ppc (ppci). | 输入：ppci；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | copy；len；CaseData；np.copy；range；process_branches；pd.DataFrame；sort；int | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pf.run_helmpy_pf._get_slack_weights | (ppci) | pandapower/pf/run_helmpy_pf.py#L101 | Collect pandapower's distributed-slack participation factors as a per-bus array. | 输入：ppci；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | len；np.zeros；astype；np.add.at；np.any | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pf.run_helmpy_pf._runpf_helmpy_pf | (ppci, options, **kwargs) | pandapower/pf/run_helmpy_pf.py#L125 | Runs a HELM (Holomorphic Embedding Load flow Method) based power flow, provided by the optional HELMpy package. | 输入：ppci, options, **kwargs；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | perf_counter；bool；options.get；_build_helm_case；helm；run.V_complex_profile.copy；np.deg2rad；_get_pf_variables_from_ppci；_get_numba_functions；_get_Y_bus；np.abs；np.angle；internal.update；_store_results_from_pf_in_ppci；_get_slack_weights；np.exp | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
