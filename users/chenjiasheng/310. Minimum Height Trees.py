from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adjs = [set() for _ in range(n)]
        for u, v in edges:
            adjs[u].add(v)
            adjs[v].add(u)

        leaves = [u for u in range(n) if len(adjs[u]) == 1]
        while True:
            if len(leaves) == 1 or (len(leaves) == 2 and (leaves[0] in adjs[leaves[1]])):
                return leaves

            new_leaves = []
            for u in leaves:
                assert len(adjs[u]) == 1
                v = next(iter(adjs[u]))
                adjs[u].remove(v)
                adjs[v].remove(u)
                if len(adjs[v]) == 1:
                    new_leaves.append(v)

            leaves = new_leaves

n = 4
edges = [[1,0],[1,2],[1,3]]
print(Solution().findMinHeightTrees(n, edges))

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(Solution().findMinHeightTrees(n, edges))

n = 3
edges = [[0,1], [1,2]]
print(Solution().findMinHeightTrees(n, edges))

n = 4
edges = [[1,0], [1,2], [1,3]]
print(Solution().findMinHeightTrees(n, edges))

n = 2
edges = [[0,1]]
print(Solution().findMinHeightTrees(n, edges))








