# `pandapower.plotting.colormaps`

本模块共记录 3 个函数、类或方法。

| kind | qualified_name | signature | source_anchor | summary | inputs_outputs | side_effects | dependencies | development_relevance | evidence_status | review_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| function | pandapower.plotting.colormaps.cmap_continuous | (cmap_list) | pandapower/plotting/colormaps.py#L53 | Can be used to create a continuous colormap. | 输入：cmap_list；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | LinearSegmentedColormap.from_list；Normalize；UserWarning | 仅内部参考：不进入首轮后端适配器 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.plotting.colormaps.cmap_discrete | (cmap_list) | pandapower/plotting/colormaps.py#L16 | Can be used to create a discrete colormap. | 输入：cmap_list；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | boundaries.append；ListedColormap；BoundaryNorm；UserWarning；cmap_colors.append；ValueError | 仅内部参考：不进入首轮后端适配器 | 源码确认（静态 AST） | 自动生成 |
| function | pandapower.plotting.colormaps.cmap_logarithmic | (min_value, max_value, colors) | pandapower/plotting/colormaps.py#L84 | Can be used to create a logarithmic colormap. The colormap itself has a linear segmentation of the given colors. The values however will be matched to the colors based on a logarithmic normalization (c.f. matplotlib.colors.LogNorm for more information on how the logarithmic normalization works). | 输入：min_value, max_value, colors；输出：返回值未注解 | 可能修改传入对象、网络表或仿真状态；调用前后状态需由适配器校验 | len；np.arange；LinearSegmentedColormap.from_list；LogNorm；UserWarning；list；np.log；zip | 仅内部参考：不进入首轮后端适配器 | 源码确认（静态 AST） | 自动生成 |
