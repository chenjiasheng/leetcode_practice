package Cjs.Lesson1;

import java.util.Arrays;

//  在本问题中, 树指的是一个连通且无环的无向图。
//  输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。
//  附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
//  结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v]，满足u < v，表示连接顶点u和v的无向图的边。
//  返回一条可以删去的边，使得结果图是一个有着N个节点的树。
//  如果有多个答案，则返回二维数组中最后出现的边。答案边[u, v] 应满足相同的格式u < v。

public class Case684 {
    public int[] solution1UnionFind(int[][] edges){
        if (edges.length == 0){
            return new int[0];
        }

        int n = edges.length;
        UnionFind uf = new UnionFind(n);
        int count = uf.count;
        for (int[] curEdge: edges){
            uf.union(curEdge[0]-1, curEdge[1]-1);
            if (uf.count != count){
                count = uf.count;
            } else {
                return curEdge;
            }
        }
        return edges[n-1];
    }

    public int[] findRedundantConnection(int[][] edges){
        return solution1UnionFind(edges);
    }

    public static void main(String[] args) {
        Case684 test = new Case684();
        int[][] edges;

        edges = new int[][] {{1,2},{1,3},{2,3}};
        System.out.println(Arrays.toString(test.findRedundantConnection(edges))); // [2,3]

        edges = new int[][] {{1,2},{2,3},{3,4},{1,4},{1,5}};
        System.out.println(Arrays.toString(test.findRedundantConnection(edges))); // [1,4]
    }
}
