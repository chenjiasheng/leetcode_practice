## 注意：
1. 请各自在users/目录下新建自己的目录，以便提交作业。例如：
`users/chenjiasheng/1759.统计同构子字符串的数目.py`

2. 编程规范检查工具，没有听说这个工具或者不会配置的，请单独联系我。
## 培训计划：
- 基本数据结构：array, list, map, tree and graph  √
- 递归 √
- DFS √
- BFS √
- 单调栈与单调队列 √
- 二分搜索 √
- 堆（优先级队列） √
- 树状数组 √
- 并查集 4月19日 √
- 拓扑排序和有向图最长路径 4月26日 √
- dijkstra算法 5月17日 √
- 欧拉图 5月17日 √
- 有序容器 8月26日 √
- 最小生成树 8月31日 √
- 链表、树和图的序列化，大数取模，对拍 9月6日
- 差分与累计和 9月6日


## 培训记录：
### 20210419：并查集
#### 讲解纪要：
- 并查集的用途：成环检测，元素划分
- 并查集三个接口：INIT, FIND, UNION
- FIND函数利用递归做路径压缩
- UNION函数判断节点size降低合并代价
#### 作业布置：
- 例题：    
547.省份数量  
684.冗余连接  
685.冗余连接 II    
- 作业：  
765.情侣牵手
### 20210426：拓扑排序和有向图最长路径
#### 讲解纪要：
##### 拓扑排序的两种算法
- 后序DFS  
    后序DFS保证父节点一定更晚输出，注意得到的列表要逆序
- 逐步移除入度为0的节点  
    维护所有节点的入度*indegrees*和入度为0的节点列表*q*，逐步移除入度为0的节点同时更新*indegrees*和*q*
##### 有向图最长路径的两种算法
- DFS方法  
    - 每节点的代价都初始化为0  
    - 遍历每个节点，若节点代价是0，说明节点未被处理过。  
    - 否则递归的获取所有入向邻居节点的代价，取其最大值作为本节点代价。
    - 注意节点代价至少为1。
- 拓扑排序法  
    - 先对节点做拓扑排序
    - 然后按照此顺序遍历所有节点
    - 设置节点的代价为所有入向邻居节点代价的最大值
#### 作业布置：
- 例题：  
210.课程表 II  
329.矩阵中的最长递增路径  
- 作业：  
1203.项目管理  
每道题都要用两种方法各做一遍
### 20210517：dijkstra算法与欧拉图 5月17日
#### 讲解纪要：
##### dijkstra算法
- dijkstra算法用于**带非负权**的**有向图**或**无向图**的**单源**最短路径
- 权重非负保证了当前最短的路径将是全局最短路径，以后不会再发现更短的路径了
- 利用优先级队列来自动维护已发现而未定的路径
- 对于一个节点可以以不同的距离值作为key值推入优先级队列，在出队时再检查是否丢弃
- dijkstra算法是一种特殊的BFS：优先级队列 vs. 普通队列，距离短优先 vs. 跳数少优先。
##### 欧拉图
- 欧拉路径和欧拉回路：从某一源点S出发，若能刚好经过每条边一次到达目的点T，S到T的路径成为欧拉路径。若S和T相同，则成为欧拉回路。
- 欧拉回路和欧拉路径的存在性判断：
    - 无向图欧拉环路：a) 图是联通的 b) 所有节点度数都是偶数
    - 有向图欧拉环路：a) 对应的无向图是联通的 b) 所有节点的出度等于入度
    - 无向图欧拉路径：a) 图是联通的 b) 有且仅有一对节点S和T的度数是奇数，其他节点度数是偶数
    - 有向图欧拉路径：a) 对应的无向图是联通的 b) 有且仅有一对节点S和T，S的出度比入度大1、T的入度比出度大1，其他节点出度等于入度
- 欧拉回路和欧拉路径的搜索方法：
    - 从*S*出发，DFS后序遍历
    - 一边遍历一遍删除边
#### 作业布置：
- 例题：  
1514.概率最大的路径   
753.破解保险箱  
- 作业：  
743.网络延迟时间  
1129.颜色交替的最短路径  
332.重新安排行程
  
### 20210826: 有序容器
#### 讲解纪要：
- 了解有序容器的原理  
  有序容器底层一般是平衡二叉树例如RBT实现的，在树的节点上额外维护子树size信息，在树的左旋右旋更新时，子树size信息可以以极低的代价一起更新。
- Python标准库没有平衡二叉树，C++的set/map和Java的TreeSet和TreeMap虽然底层是树实现的，但是它们并没有维护子树size信息，也没有暴露order_of_key和find_by_order接口
- Python的sortedcontainers库和C++的pbds库是leetcode平台可用的有序容器实现
- order_of_key接口：logN时间查询key的次序，对应python的SortedList的bisect_left方法。 
- find_by_order接口：logN时间找到第order小的元素，对应python SortedList的直接取下标操作。

- 利用有序容器，很多题目的思路可以变得简单清晰
#### 作业布置：
- 例题：  
315.计算右侧小于当前元素的个数
- 作业：  
327.区间和的个数

  
### 20210831: 最小生成树
#### 讲解纪要：
- 无向图的生成树是包含所有顶点的无环子图（即树）。
- 无向图的最小生成树是边的权重之和最小的生成树。
- 两种算法，Kruskal和Prim算法
###### Kruskal算法：
- Kruskal将所有的边排序，然后逐条边判断这条边生成树中是否会导致成环，如果不成环则添加。
- Kruskal算法依赖UFS并查集。
###### Prim算法：
- Prim算法从随机的顶点出发，每次选择生成树外的离树最近的点，加入到生成树中。
- 树外的点离生成树的距离，如果跟源点无直连边则初始化为INF
- 每次有一个树外的点加入到生成树中时，更新该点的邻居节点到树的距离
- 节点到树的距离用优先级队列（小根点）维护，类似于Dijkstra算法

#### 作业布置：
- 例题：  
1584.连接所有点的最小费用
- 作业：  
1135.最低成本联通所有城市