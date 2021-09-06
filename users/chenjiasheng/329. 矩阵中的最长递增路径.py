from typing import List
import collections


class SolutionTopologySort:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        n = rows * cols

        adj = collections.defaultdict(list)
        inv_adj = collections.defaultdict(list)
        indegrees = [0] * n

        def init(u):
            row, col = u // cols, u % cols
            up = row - 1, col
            down = row + 1, col
            left = row, col - 1
            right = row, col + 1

            for row2, col2 in [up, down, left, right]:
                if not (0 <= row2 < rows and 0 <= col2 < cols):
                    continue
                v = row2 * cols + col2
                if matrix[row2][col2] > matrix[row][col]:
                    adj[u].append(v)
                    indegrees[v] += 1
                if matrix[row2][col2] < matrix[row][col]:
                    inv_adj[u].append(v)

        for u in range(n):
            init(u)

        topology_sorted = []

        def topology_sort():
            free_nodes = [i for i in range(n) if indegrees[i] == 0]
            while len(free_nodes) != 0:
                u = free_nodes.pop()
                topology_sorted.append(u)
                for v in adj[u]:
                    indegrees[v] -= 1
                    if indegrees[v] == 0:
                        free_nodes.append(v)

        topology_sort()

        # get distances
        dists = [0] * n
        for u in topology_sorted:
            if len(inv_adj[u]) != 0:
                dists[u] = max(dists[v] + 1 for v in inv_adj[u])

        return max(dists) + 1


class SolutionDFS:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        n = rows * cols

        inv_adj = collections.defaultdict(list)
        def init(u):
            row, col = u // cols, u % cols
            up = row - 1, col
            down = row + 1, col
            left = row, col - 1
            right = row, col + 1

            for row2, col2 in [up, down, left, right]:
                if not (0 <= row2 < rows and 0 <= col2 < cols):
                    continue
                v = row2 * cols + col2
                if matrix[row2][col2] < matrix[row][col]:
                    inv_adj[u].append(v)
        for u in range(n):
            init(u)

        dp = [0] * n
        def longest_path(u):
            if dp[u] == 0:
                d = 1
                for v in inv_adj[u]:
                    d = max(d, longest_path(v) + 1)
                dp[u] = d
            return dp[u]
        for u in range(n):
            longest_path(u)
        return max(dp)


Solution = SolutionDFS
print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
