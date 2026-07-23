# `pandapower.opf.run_pandamodels`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.opf.run_pandamodels._call_pandamodels | (buffer_file, julia_file, dev_mode) | pandapower/opf/run_pandamodels.py#L60 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.opf.run_pandamodels._call_pandamodels 的实现与调用链确认。 | 输入：buffer_file, julia_file, dev_mode；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | Main.seval；Base.find_package；logger.info；Pkg.Registry.update；Pkg.add；Pkg.build；Pkg.resolve；Pkg.develop；Pkg.activate；ImportError；Pkg.instantiate | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.opf.run_pandamodels._runpm | (net: pandapowerNet, delete_buffer_file: bool=True, pm_file_path: str \| None=None, pdm_dev_mode: bool=False, **kwargs) | pandapower/opf/run_pandamodels.py#L11 | Converts the pandapower net to a pm json file, saves it to disk, runs a PandaModels.jl, and reads the results back to the pandapower net | 输入：net, delete_buffer_file, pm_file_path, pdm_dev_mode, **kwargs；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | convert_to_pm_structure；dump_pm_json；logger.debug；_call_pandamodels；logger.info；read_pm_results_to_net；os.remove；round | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
