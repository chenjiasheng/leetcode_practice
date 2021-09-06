#define N 1010

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
		if (idx1Root == idx2Root)
			return;
        parents[idx1Root] = idx2Root;
    }

    bool isUnion (int idx1, int idx2)
    {
        return find(idx1) == find(idx2);
    }
};

class Solution {
public:
	vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
		int inDegree[N] = {0}; // 记录节点入度
        int n = edges.size(); // 边的数量
        for (int i = 0; i < n; i++) {
            inDegree[edges[i][1]]++; // 统计入度
        }

        vector<int> vec; // 记录入度为2的边（如果有的话就两条边）
        // 找入度为2的节点所对应的边，注意要倒叙，因为优先返回最后出现在二维数组中的答案
        for (int i = n - 1; i >= 0; i--) {
            if (inDegree[edges[i][1]] == 2) {
                vec.push_back(i);
            }
        }
		
        // 如果有入度为2的节点，那么一定是两条边里删一个，看删哪个可以构成树
		UnionFind uf(N);
        if (vec.size() > 0) {
            if (isTreeAfterRemoveEdge(uf, edges, vec[0]))
                return edges[vec[0]];
            else
                return edges[vec[1]];
        }

        // 明确没有入度为2的情况，那么一定有有向环，找到构成环的边返回就可以了
        return getRemoveEdge(uf, edges);
    }
	
private:
    // 在有向图里找到删除的那条边，使其变成树
    vector<int> getRemoveEdge(UnionFind& uf, const vector<vector<int>>& edges) {
        int n = edges.size(); // 边的数量
        for (int i = 0; i < n; i++) { // 遍历所有的边
            if (uf.isUnion(edges[i][0], edges[i][1])) { // 构成有向环了，就是要删除的边
                return edges[i];
            }
            uf.unite(edges[i][0], edges[i][1]);
        }

        return {};
    }

    // 删一条边之后判断是不是树
    bool isTreeAfterRemoveEdge(UnionFind& uf, const vector<vector<int>>& edges, int deleteEdge) {
        int n = edges.size(); // 边的数量
        for (int i = 0; i < n; i++) {
            if (i == deleteEdge)
				continue;
            if (uf.isUnion(edges[i][0], edges[i][1])) // 构成有向环了，一定不是树
                return false;

            uf.unite(edges[i][0], edges[i][1]);
        }

        return true;
    }	
};