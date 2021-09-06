from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        temp_edges = [[x - 1, y - 1] for x, y in edges]
        res = self.findRedundantDirectedConnectionInner(temp_edges)
        return [res[0]+1, res[1]+1]

    def findRedundantDirectedConnectionInner(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = list(range(n))
        s = [0] * n

        bad_node = -1
        has_parent = [False] * n
        for u, v in edges:
            if has_parent[v]:
                bad_node = v
                break
            has_parent[v] = True

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            if s[x] < s[y]:
                x, y = y, x
            p[y] = x
            s[x] += s[y]
            return True

        if bad_node != -1:
            bad_edges = []
            for u, v in edges:
                if v == bad_node:
                    bad_edges.append([u, v])
                    continue
                union(u, v)
            assert len(bad_edges) == 2
            u, v = bad_edges[0]
            if find(u) != find(v):
                return bad_edges[1]
            else:
                return bad_edges[0]
        else:
            for u, v in edges:
                if not union(u, v):
                    return [u, v]


edges = [[3,1], [1,2], [2,3], [2,4]]
solution = Solution()
result = solution.findRedundantDirectedConnection(edges)
print(result)


edges = [[1,2], [1,3], [2,4], [3,4]]
solution = Solution()
result = solution.findRedundantDirectedConnection(edges)
print(result)

edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
solution = Solution()
result = solution.findRedundantDirectedConnection(edges)
print(result)


