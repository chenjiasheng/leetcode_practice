from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # init
        parents = list(range(len(edges)))
        sizes = [1] * len(edges)

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            else:
                if sizes[x] < sizes[y]:
                    x, y = y, x
                parents[y] = x
                sizes[x] += sizes[y]
                sizes[y] = 0
                return True

        for x, y in edges:
            if not union(x-1, y-1):
                return [x, y]


edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
solution = Solution()
result = solution.findRedundantConnection(edges)
print(result)

