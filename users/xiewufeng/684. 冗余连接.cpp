class UnionFind {
public:
    vector<int> parents;
    UnionFind(int size) {
        parents.resize(size);
        for (int i = 1; i < size; i++) {
            parents[i] = i;
        }
    }

    int find(int idx)
    {
        if (parents[idx] != idx) {
            parents[idx] = find(parents[idx]);
        }

        return parents[idx];
    }

    void unite(int idx1, int idx2)
    {
        int idx1Root = find(idx1);
        int idx2Root = find(idx2);
        parents[idx1Root] = idx2Root;
    }

    bool isUnion (int idx1, int idx2)
    {
        return find(idx1) == find(idx2);
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        vector<int> ret;
        int num = edges.size();
        UnionFind uf(num + 1);
        
        for (auto& edge : edges) {
            if (uf.isUnion(edge[0], edge[1])) {
                return {edge[0], edge[1]};
            }

            uf.unite(edge[0], edge[1]);
        }

        return ret;
    }
};