class UnionFind
{
private:
    vector<int> father;
    vector<int> len;
    int cnt = 0;
public:
    UnionFind(int n)
    {
        father.resize(n);
        len.resize(n);
        cnt = n;

        for (int i = 0; i < n; i++) {
            father[i] = i;
            len[i] = 1;
        }
    }

    int find(int x) {
        if (father[x] != x) {
            return father[x] = find(father[x]);
        } else {
            return x;
        }
    }

    void merge(int x, int y) {
        x = find(x);
        y = find(y);

        if (x == y) return;

        if (len[x] < len[y]) {
            father[x] = y;
            len[y] += len[x];
        } else {
            father[y] = x;
            len[x] += len[y];
        }
        cnt--;
    }

    int count(){return cnt;}
};


class Solution {
    vector<int> visited;
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        int res = 0;
        visited.resize(n, false);

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(isConnected, i, n);
                res++;
            }
        }

        return res;
    }

    void dfs(vector<vector<int>> &isConnected, int i, int n) {
        for (int j = 0; j < n; j++) {
            if (isConnected[i][j] && i!=j && !visited[j]) {
                visited[j] = true;
                dfs(isConnected, j, n);
            }
        }
    }
};
