package Cjs.Lesson1;

class UnionFind{
    int[] parent;
    int[] size;
    int count;

    UnionFind(int n){
        count = n;
        parent = new int[n];
        size = new int[n];
        for (int i=0; i<n; i++){
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int x){
        while(x != parent[x]){
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public void union(int x, int y){
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY){
            return;
        }

        if (size[rootX] > size[rootY]){
            parent[rootY] = rootX;
            size[rootX] += size[rootY];
        } else {
            parent[rootX] = rootY;
            size[rootY] += size[rootX];
        }
        count--;
    }

    public boolean isConnected(int x, int y){
        return find(x) == find(y);
    }
}