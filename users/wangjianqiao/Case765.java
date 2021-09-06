package Cjs.Lesson1;

//  N对情侣坐在连续排列的2N个座位上，想要牵到对方的手。
//  计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。
//  一次交换可选择任意两人，让他们站起来交换座位。
//  人和座位用0到2N-1的整数表示，情侣们按顺序编号，第一对是(0, 1)，第二对是(2, 3)，以此类推，最后一对是(2N-2, 2N-1)。
//  这些情侣的初始座位row[i]是由最初始坐在第i个座位上的人决定的。

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

public class Case765 {
    public int solution1UnionFind(int[] row){
        int n = row.length / 2;
        if (n < 2){
            return 0;
        }

        List<int[]> graph = new ArrayList<>();
        for (int i=0; i<n; i++){
            int x = row[2*i] / 2;
            int y = row[2*i+1] / 2;
            if (x == y){
                continue;
            }
            graph.add(new int[] {x,y});
        }

        UnionFind uf = new UnionFind(n);
        for (int[] pair: graph){
            uf.union(pair[0], pair[1]);
        }

        HashMap<Integer, Integer> map = new HashMap<>();
        for (int[] pair: graph){
            for (int p: pair){
                int root = uf.find(p);
                int size = uf.size[root];
                if (!map.containsKey(root)){
                    map.put(root, size-1);
                }
            }
        }

        int ans = 0;
        for (int key: map.keySet()){
            ans += map.get(key);
        }
        return ans;
    }

    public int minSwapsCouples(int[] row){
        return solution1UnionFind(row);
    }

    public static void main(String[] args) {
        Case765 test = new Case765();
        int[] row;

        row = new int[] {0,2,1,3};
        System.out.println(test.minSwapsCouples(row)); // 1

        row = new int[] {3,2,0,1};
        System.out.println(test.minSwapsCouples(row)); // 0
    }
}
