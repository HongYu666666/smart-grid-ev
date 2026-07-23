# `pandapower.networks.synthetic_voltage_control_lv_networks`

本模块共记录 1 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.networks.synthetic_voltage_control_lv_networks.create_synthetic_voltage_control_lv_network | (network_class='rural_1') | pandapower/networks/synthetic_voltage_control_lv_networks.py#L15 | This function creates a LV network from M. Lindner, C. Aigner, R. Witzmann, F. Wirtz, I. Berber, M. Gödde and R. Frings. "Aktuelle Musternetze zur Untersuchung von Spannungsproblemen in der Niederspannung". 14. Symposium Energieinnovation TU Graz. 2014 which are representative, synthetic grids for voltage control analysis. | 输入：network_class；输出：返回值未注解 | 存在文件或序列化读写调用；具体路径和覆盖行为需按调用场景复核 | create_empty_network；create_bus；create_ext_grid；create_transformer；range；net.bus.apply；ValueError；create_std_type；len；create_buses；pd.DataFrame；append；lines.iterrows；create_load；create_sgen；create_line | 可参考：是否进入适配器边界由后续 PoC 决定 | 源码确认（静态 AST） | 自动生成 |
