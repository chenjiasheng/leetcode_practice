package Cjs.Lesson1;

import java.util.Arrays;

//  在本问题中，有根树指满足以下条件的 有向图。
//    该树只有一个根节点，所有其他节点都是该根节点的后继。
//    该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。
//  输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。
//  附加的边包含在 1 到 n 中的两个不同顶点间，这条附加的边不属于树中已存在的边。
//  结果图是一个以边组成的二维数组edges。
//  每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是 vi 的一个父节点。
//  返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。
//  若有多个答案，返回最后出现在给定二维数组的答案。

public class Case685 {

    public boolean isRootTree(int[][] edges, int removeIndex){
        UnionFind uf = new UnionFind(edges.length);
        for (int i = 0; i<edges.length; i++){
            if (i == removeIndex){
                continue;
            }
            uf.union(edges[i][0]-1, edges[i][1]-1);
        }
        return uf.count == 1;
    }

    public int[] solution1UnionFind(int[][] edges){
        int n = edges.length;
        if (n == 0){
            return new int[0];
        }

//        判断是否有入度为2的节点
        int[] inDegree = new int[n];
        int node = -1;
        for (int i=0; i < n; i++){
            inDegree[edges[i][1]-1] += 1;
            if (inDegree[edges[i][1]-1] == 2){
                node = edges[i][1];
                break;
            }
        }

        if (node != -1){
//            有入度为2的节点
            int firstEdgeIndex = -1;
            int secondEdgeIndex = -1;
            for (int i = 0; i<n; i++){
                if(edges[i][1] == node){
                    firstEdgeIndex = secondEdgeIndex;
                    secondEdgeIndex = i;
                }
            }
            if (isRootTree(edges, secondEdgeIndex)){
                return edges[secondEdgeIndex];
            } else {
                return edges[firstEdgeIndex];
            }
        } else {
//            没有入度为2的节点，当无向图处理
            UnionFind uf = new UnionFind(n);
            int count = uf.count;
            for(int[] curEdge: edges){
                uf.union(curEdge[0]-1, curEdge[1]-1);
                if(count != uf.count){
                    count = uf.count;
                } else {
                    return curEdge;
                }
            }
            return edges[n-1];
        }
    }

    public int[] findRedundantDirectedConnection(int[][] edges) {
        return solution1UnionFind(edges);
    }

    public static void main(String[] args) {
        Case685 test = new Case685();
        int[][] edges;

        edges = new int[][] {{1,2},{1,3},{2,3}};
        System.out.println(Arrays.toString(test.findRedundantDirectedConnection(edges))); // [2,3]

        edges = new int[][] {{1,2},{2,3},{3,4},{1,4},{1,5}};
        System.out.println(Arrays.toString(test.findRedundantDirectedConnection(edges))); // [1,4]

        edges = new int[][] {{2,1},{3,1},{4,2},{1,4}};
        System.out.println(Arrays.toString(test.findRedundantDirectedConnection(edges))); // [2,1]

        edges = new int[][] {{2,1},{1,3},{4,2},{1,4}};
        System.out.println(Arrays.toString(test.findRedundantDirectedConnection(edges))); // [1,4]
    }
}
