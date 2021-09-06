from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents = list(range(n))
        sizes = [1] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return
            if sizes[x] < sizes[y]:
                x, y = y, x
            parents[y] = x
            sizes[x] += sizes[y]
            sizes[y] = 0

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    union(i, j)

        result = 0
        for i in range(n):
            if parents[i] == i:
                result += 1

        return result


isConnected = [[1,0,0],[0,1,0],[0,0,1]]
solution = Solution()
result = solution.findCircleNum(isConnected)
print(result)

