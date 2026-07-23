# net.py — 路网模型

> 复核状态：人工复核 [reviewed]

## 核心类

| 符号 | 功能 | 说明 |
|------|------|------|
| RoadNet | 道路网络 | 管理节点、边和路由 |
| Node | 路网节点 | 位置坐标、属性 |
| Edge | 路网边 | 长度、车道数、速度限制 |
| SubNet | 子网络 | 分区管理（并行仿真用） |
| Grid | 电网网格 | 配电网节点映射 |

## 关键方法

| 方法 | 所属 | 功能 | 输入 | 输出 |
|------|------|------|------|------|
| load_from_xml() | RoadNet | 从 XML 加载路网 | 文件路径 | RoadNet 实例 |
| get_route() | RoadNet | 获取两点间路径 | origin, dest | 路径节点列表 |
| get_distance() | RoadNet | 获取路径距离 | origin, dest | float (m) |
| get_edges() | RoadNet | 获取所有边 | — | Edge 列表 |
| get_nodes() | RoadNet | 获取所有节点 | — | Node 列表 |
| partition() | RoadNet | 路网分区 | 分区数 | SubNet 列表 |
