class Solution {
    vector<int> set;
public:
    int find_parent(int n){
        while(set[n] != n){
            n=set[n];
        }
        return n;
    }

    void quick_union(int n, int m){
        int pn = find_parent(n);
        int pm = find_parent(m);
        set[pm] = pn;
    }

    bool isSameParent(int n, int m){
        int pn = find_parent(n);
       int pm = find_parent(m);
        return pm == pn;
    }

    bool union1(vector<vector<int>>& edges, int n){
        set = vector<int> (edges.size()+1);
        for(int i=1; i < set.size(); i++)
            set[i] = i;
        for(int i = 0; i < edges.size(); i++){
            if(i == n)
                continue;
            quick_union(edges[i][0],edges[i][1]);
        }
        int u = edges[n][0];
        int v = edges[n][1];

        if(isSameParent(u, v))
            return true;
        else
            return false;
    }

    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        vector<int> indegree(edges.size() + 1, 0);
        vector<int> outdegree(edges.size() + 1, 0);
        vector<int> visited(edges.size() + 1, 0);

        for (int i = 0; i < edges.size(); i++) {
            int &m = edges[i][0];
            int &n = edges[i][1];

            outdegree[m]++;
            indegree[n]++;

            if (indegree[n] > 1) {
                if (union1(edges, i)) {
                    return {edges[i][0], edges[i][1]};
                } else {
                    int j = visited[n];
                    return {edges[j][0], edges[j][1]};
                }
            } else {
                visited[n] = i;
            }
        }

        for(int i = edges.size() - 1; i >= 0; i--){
            if (union1(edges, i)) {
                return {edges[i][0], edges[i][1]};
            }
        }
        return {};
    }
};
