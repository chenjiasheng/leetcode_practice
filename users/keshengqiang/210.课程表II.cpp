方案一：
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> inLableNum;
        inLableNum.resize(numCourses);

        for (const auto& item : prerequisites) {
            inLableNum[item[0]]++;
        }

        queue<int> nodes;
        for (int i = 0; i < numCourses; i++) {
            if (inLableNum[i] == 0) {
                nodes.push(i);
            }
        }

        vector<int> res;
        while (!nodes.empty()) {
            auto item = nodes.front();
            nodes.pop();
            res.push_back(item);

            for (auto& item1 : prerequisites) {
                if (item1[1] == item) {
                    inLableNum[item1[0]]--;
                    if (inLableNum[item1[0]] == 0) {
                        nodes.push(item1[0]);
                    }
                }
            }
        }

        return res.size() == numCourses ? res : vector<int>();
    }
};


方案二：
class Solution {
    vector<vector<int>> nodes;
    vector<int> visit;
    bool isValid = true;
    vector<int> result;
public:
    void dfs(int index)
    {
        visit[index] = 1;
        for (auto it : nodes[index]) {
            if (!visit[it]) {
                dfs(it);
                if (!isValid) {
                    return;
                }
            } else if (visit[it] == 1) {
                isValid = false;
                return;
            }
        }

        visit[index] = 2;
        result.push_back(index);
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        nodes.resize(numCourses);
        visit.resize(numCourses);
        for (auto& it : prerequisites) {
            nodes[it[1]].push_back(it[0]);
        }

        for (int i = 0; i < numCourses && isValid; i++) {
            if (!visit[i]) {
                dfs(i);
            }
        }

        if (!isValid) {
            return {};
        }

        reverse(result.begin(), result.end());
        return result;
    }
};