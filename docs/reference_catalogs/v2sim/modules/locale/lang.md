# `v2sim.locale.lang`

本模块共记录 4 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| class | v2sim.locale.lang.Lang | class | v2sim/locale/lang.py#L8 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.locale.lang.Lang 的实现与调用链确认。 | 输入：构造参数由 __init__ 或工厂函数定义；输出：类实例 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | getattr；isinstance；fmt.format；lc.__dict__.items；LangConfig.GetLangCode；Lang.load；importlib.import_module；hasattr；ValueError；key.startswith；key.endswith；locale_code.split；setattr；print | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.locale.lang.Lang.format | (item: str, **kwargs) | v2sim/locale/lang.py#L284 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.locale.lang.Lang.format 的实现与调用链确认。 | 输入：item, **kwargs；输出：返回值未注解 | 静态扫描未确认外部副作用；运行态副作用仍需在 PoC 中复核 | getattr；isinstance；fmt.format | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.locale.lang.Lang.load | (lang: str) -> bool | v2sim/locale/lang.py#L290 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.locale.lang.Lang.load 的实现与调用链确认。 | 输入：lang；输出：bool | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | lc.__dict__.items；isinstance；importlib.import_module；hasattr；ValueError；key.startswith；key.endswith；setattr；print | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
| method | v2sim.locale.lang.Lang.load_default | () | v2sim/locale/lang.py#L312 | 待人工补充：源码未提供可直接确认的功能说明；需结合 v2sim.locale.lang.Lang.load_default 的实现与调用链确认。 | 输入：无显式输入；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | LangConfig.GetLangCode；Lang.load；locale_code.split | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
