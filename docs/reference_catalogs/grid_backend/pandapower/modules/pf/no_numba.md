# `pandapower.pf.no_numba`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pf.no_numba.jit | (*args: Any, **kwargs: Any) -> Union[Callable[[Callable[P, R]], Callable[P, R]], Callable[..., Callable[P, R]]] | pandapower/pf/no_numba.py#L13 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pf.no_numba.jit 的实现与调用链确认。 | 输入：*args, **kwargs；输出：Union[Callable[[Callable[P, R]], Callable[P, R]], Callable[..., Callable[P, R]]] | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | len；callable | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.pf.no_numba.marker | (*args: Any, **kwargs: Any) -> Callable[..., Any] | pandapower/pf/no_numba.py#L29 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.pf.no_numba.marker 的实现与调用链确认。 | 输入：*args, **kwargs；输出：Callable[..., Any] | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | 静态扫描未发现直接函数调用 | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
