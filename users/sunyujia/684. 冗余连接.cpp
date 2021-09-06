class Solution {
public:
    int findRoot(vector<int> &parent, int node) {
        int nodeRoot = node;
        while (parent[nodeRoot] != -1) {
            nodeRoot = parent[nodeRoot];
        }

        return nodeRoot;
    }

    void unionRoot(vector<int> &parent, int node1, int node2) {
        int node1Root = findRoot(parent, node1);
        int node2Root = findRoot(parent, node2);

        parent[node1Root] = node2Root;
    }

    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int nodeCount = edges.size();
        vector<int> parent(nodeCount + 1, -1);

        for (const auto &edge : edges) {
            int node1 = edge[0];
            int node2 = edge[1];

            if (findRoot(parent, node1) != findRoot(parent, node2)) {
                unionRoot(parent, node1, node2);
            } else {
                return edge;
            }
        }

        return {};
    }
};
