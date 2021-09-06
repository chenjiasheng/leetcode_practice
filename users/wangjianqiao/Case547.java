package Cjs.Lesson1;

//  有 n 个城市，其中一些彼此相连，另一些没有相连。
//  如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
//  省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
//  给你一个 n x n 的矩阵 isConnected ，
//  其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
//  返回矩阵中 省份 的数量。

public class Case547 {
    public int solution1UnionFind(int[][] isConnected){
        int n = isConnected.length;
        UnionFind uf = new UnionFind(n);
        for (int i=0; i<n; i++){
            for (int j=i; j<n; j++){
                if (isConnected[i][j] == 1){
                    uf.union(i,j);
                }
            }
        }
        return uf.count;
    }

    public int findCircleNum(int[][] isConnected){
        return solution1UnionFind(isConnected);
    }

    public static void main(String[] args) {
        Case547 test = new Case547();
        int[][] isConnected;

        isConnected = new int[][] {
                {1,1,0},
                {1,1,0},
                {0,0,1}
        };
        System.out.println(test.findCircleNum(isConnected)); // 2

        isConnected = new int[][] {
                {1,0,0},
                {0,1,0},
                {0,0,1}
        };
        System.out.println(test.findCircleNum(isConnected)); // 3
    }
}
