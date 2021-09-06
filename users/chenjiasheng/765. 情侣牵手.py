from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
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

        for i in range(0, n, 2):
            union(i, i+1)

        for k in range(0, n, 2):
            i, j = row[k], row[k+1]
            union(i, j)

        result = 0
        for i in range(n):
            if parents[i] == i:
                assert sizes[i] % 2 == 0
                result += sizes[i] // 2 - 1
        return result


row = [3,2,0,1]
solution = Solution()
print(solution.minSwapsCouples(row))
