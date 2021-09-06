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
public:
    int minSwapsCouples(vector<int>& row) {
        int res = 0;
        int n = row.size();
        int total = n / 2;

        UnionFind uf(total);

        for (int i = 0; i < n; i+=2) {
            int groupId_1 = row[i] / 2;
            int groupId_2 = row[i + 1] / 2;
            if (groupId_1 != groupId_2) {
                uf.merge(groupId_1, groupId_2);
            }
        }
        vector<int> couples(total);
        for (int i = 0; i < total; i++) {
            couples[uf.find(i)]++;
        }
        for (int couple : couples) {
            if (couple != 0) {
                res += couple - 1;
            }
        }

        return res;
    }
};
