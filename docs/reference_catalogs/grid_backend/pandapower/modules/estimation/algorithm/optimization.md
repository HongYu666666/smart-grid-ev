# `pandapower.estimation.algorithm.optimization`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| class | pandapower.estimation.algorithm.optimization.OptAlgorithm | class(BaseAlgorithm) | pandapower/estimation/algorithm/optimization.py#L20 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.estimation.algorithm.optimization.OptAlgorithm 的实现与调用链确认。 | 输入：构造参数由 __init__ 或工厂函数定义；输出：类实例 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | minimize；get_estimator；eppci.update_E；Exception | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | pandapower.estimation.algorithm.optimization.OptAlgorithm.estimate | (self, eppci: ExtendedPPCI, estimator='wls', verbose=True, **kwargs) | pandapower/estimation/algorithm/optimization.py#L21 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.estimation.algorithm.optimization.OptAlgorithm.estimate 的实现与调用链确认。 | 输入：eppci, estimator, verbose, **kwargs；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | minimize；get_estimator；eppci.update_E；Exception | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
