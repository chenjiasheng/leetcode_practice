from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        inf = m * n + 1
        dp = [[[inf for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]
        for i in range(k + 1):
            dp[0][0][i] = 0
        q = deque([[0, 0, 0]])
        while len(q) != 0:
            row, col, used = q.popleft()
            if row == m - 1 and col == n - 1:
                return dp[row][col][used]

            up = row - 1, col
            down = row + 1, col
            left = row, col - 1
            right = row, col + 1
            for row1, col1 in [up, down, left, right]:
                if not (0 <= row1 < m and 0 <= col1 < n):
                    continue
                if grid[row1][col1] <= k - used:
                    used1 = used + grid[row1][col1]
                    if dp[row1][col1][used1] == inf:
                        dp[row1][col1][used1] = dp[row][col][used] + 1
                        q.append([row1, col1, used1])

        return -1

print(Solution().shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 0))