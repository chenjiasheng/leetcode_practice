class Solution {
public:
    vector<int> parent;
    void init(int length) {
        parent.resize(length);
        for (int i = 0; i < length; i++) {
            parent[i] = i;
        }
    }
    int find(int x) {
        if (x >= parent.size()) {
            return x;
        }
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    bool Union(int x, int y) {
        auto root_x = find(x);
        auto root_y = find(y);
        if (root_x != root_y) {
            parent[root_x] = root_y;
            return true;
        }

        return false;
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        init(isConnected.size());
        int count = isConnected.size();
        for (int i = 0; i < isConnected.size(); i++) {
            for (int j = i + 1; j < isConnected[i].size(); j++) {
                if (isConnected[i][j] == 1 && Union(i, j)) {
                    count--;
                }
            }
        }

        return count;
    }
};