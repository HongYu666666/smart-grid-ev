# `pandapower.pypower.pips`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.pypower.pips.pips | (f_fcn, x0=None, A=None, l=None, u=None, xmin=None, xmax=None, gh_fcn=None, hess_fcn=None, opt=None) | pandapower/pypower/pips.py#L25 | Primal-dual interior point method for NLP (nonlinear programming). Minimize a function F(X) beginning from a starting point M{x0}, subject to optional linear and nonlinear constraints and variable bounds:: | 输入：f_fcn, x0, A, l, u, xmin, xmax, gh_fcn, hess_fcn, opt；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | isinstance；eye；find；f_fcn；len；zeros；ones；df.copy；hist.append；full；array；vstack；gh_fcn；max；norm；dot | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
