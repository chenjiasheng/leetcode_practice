class Solution {
public:
	vector<int> parent;
	void Init(int len) {
		parent.resize(len + 1);
		for (int i = 1; i < len; i++) {
			parent[i] = i;
		}
	}
    int Find(int i){
        if(parent[i] == i){
            return i;
        }
        parent[i] = Find(parent[i]);
        return parent[i];
    }

    void Union(int a,int b){
        parent[Find(a)] = Find(b);
    }
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        Init(edges.size());

        for(int i = 0; i < edges.size(); i++) {
            if(Find(edges[i][0]) == Find(edges[i][1])){
                return edges[i];
            } else {
                Union(edges[i][0], edges[i][1]);
            }
        }
        return {};
    }
};