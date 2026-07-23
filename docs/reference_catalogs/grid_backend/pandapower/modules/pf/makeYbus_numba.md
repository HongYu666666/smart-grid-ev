# `pandapower.pf.makeYbus_numba`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pf.makeYbus_numba.gen_Ybus | (Yf_x, Yt_x, Ysh, col_Y, f, t, f_sort, t_sort, nb, nl, r_nl) | pandapower/pf/makeYbus_numba.py#L21 | Fast calculation of Ybus | 输入：Yf_x, Yt_x, Ysh, col_Y, f, t, f_sort, t_sort, nb, nl, r_nl；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | jit；range；np.empty；np.zeros | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pf.makeYbus_numba.makeYbus | (baseMVA, bus, branch) | pandapower/pf/makeYbus_numba.py#L116 | Builds the bus admittance matrix and branch admittance matrices. | 输入：baseMVA, bus, branch；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | branch_vectors；astype；np.hstack；tocsr；gen_Ybus；csr_matrix；np.argsort；np.arange；Y.sort_indices；Y.eliminate_zeros；np.real；coo_matrix；np.resize | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
