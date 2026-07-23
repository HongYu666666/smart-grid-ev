# `pandapower.converter.matpower.to_mpc`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.converter.matpower.to_mpc._ppc2mpc | (ppc) | pandapower/converter/matpower/to_mpc.py#L50 | Convert network in Pypower/Matpower format Convert 0-based python to 1-based Matlab | 输入：ppc；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | copy.deepcopy；np.any；str | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.converter.matpower.to_mpc.to_mpc | (net, filename=None, **kwargs) | pandapower/converter/matpower/to_mpc.py#L19 | This function converts a pandapower net to a matpower case files (.mat) version 2. Note: python is 0-based while Matlab is 1-based. | 输入：net, filename, **kwargs；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | to_ppc；_ppc2mpc；savemat | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
