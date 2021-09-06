class UnionFind {
public:
    vector<int> parents;
    int count;
    UnionFind(int n)
    {
        count = n;
        parents.resize(n);
        for (int i = 1; i < n; i++)
            parents[i] = i;
    }

    int find(int x)
    {
        if (parents[x] != x)
            parents[x] = find(parents[x]);

        return parents[x];
    }

    void unite(int x, int y)
    {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY)
            return;
        
        parents[rootX] = rootY;
        count--;
    }

    int getCount()
    {
        return count;
    }
};

class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        int len = row.size();
        if (len <= 0 || len == 1)
            return 0;
        int couples =  len >> 1;
        UnionFind uf(couples);
        for (int i = 0; i < len; i += 2)
            uf.unite(row[i] >> 1, row[i+1] >> 1);

        return couples - uf.getCount();
    }
};