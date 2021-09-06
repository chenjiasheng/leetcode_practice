class UnionFind {
public:
    vector<int> parents;
    UnionFind(int size)
    {
        parents.resize(size);
        for (int i = 0; i < size; i++)
            parents[i] = i;
    }

    int find (int idx)
    {
        if (parents[idx] != idx)
            parents[idx] = find(parents[idx]);
        return parents[idx];
    }

    void unite(int idx1, int idx2)
    {
        int rootX = find(idx1);
        int rootY = find(idx2);
        parents[rootX] = rootY;
    }
};

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        UnionFind uf(n);
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if ( isConnected[i][j] == 1 )
                    uf.unite(i, j);
            }
        }

        int count = 0;
        for (int k = 0; k < n; k++) {
            if (uf.find(k) == k)
                count++;
        }

        return count;

    }
};