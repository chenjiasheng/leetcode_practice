from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = {(i, 1): 0 for i in range(n)}
        max_elem = {(i, 1): arr[i] for i in range(n)}
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                max_elem[(i, l)] = max(max_elem[(i, l-1)], arr[i + l - 1])
                for j in range(1, l):
                    value = dp[(i, j)] + dp[(i + j, l - j)] + max_elem[(i, j)] * max_elem[(i + j, l - j)]
                    if (i, l) not in dp:
                        dp[(i, l)] = value
                    else:
                        dp[(i, l)] = min(dp[(i, l)], value)
        return dp[(0, n)]


arr = [1,2,3,4,5]
print(Solution().mctFromLeafValues(arr))
