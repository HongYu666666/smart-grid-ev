# `pandapower.control.controller.trafo.VmSetTapControl`

本模块共记录 2 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| class | pandapower.control.controller.trafo.VmSetTapControl.VmSetTapControl | class(CharacteristicControl) | pandapower/control/controller/trafo/VmSetTapControl.py#L10 | Controller that adjusts the setpoint of a local tap changer voltage control based on a load flow result (e.g. p_lv_mw, i_lv_ka etc.) according to a defined characteristic. | 输入：构造参数由 __init__ 或工厂函数定义；输出：类实例 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | __init__；super | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
| method | pandapower.control.controller.trafo.VmSetTapControl.VmSetTapControl.__init__ | (self, net, controller_index, characteristic_index, variable='p_hv_mw', tol=0.001, in_service=True, order=0, level=0, drop_same_existing_ctrl=False, matching_params=None, **kwargs) | pandapower/control/controller/trafo/VmSetTapControl.py#L24 | 待人工补充：源码未提供可直接确认的功能说明；需结合 pandapower.control.controller.trafo.VmSetTapControl.VmSetTapControl.__init__ 的实现与调用链确认。 | 输入：net, controller_index, characteristic_index, variable, tol, in_service, order, level, drop_same_existing_ctrl, matching_params, **kwargs；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | __init__；super | 需要适配：可作为新系统数据模型、求解、控制或错误契约的参考 | 源码确认（静态 AST） | 自动生成 |
