from typing import List
import collections


class SolutionDfs:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        roots = set(range(n))
        adj = collections.defaultdict(list)
        for v, u in prerequisites:
            adj[u].append(v)
            if v in roots:
                roots.remove(v)
        white, gray, black = 0, 1, 2
        colors = [white] * n
        topo_seq = []

        def dfs():
            for root in roots:
                dfs_visit(root)

        def dfs_visit(u):
            if colors[u] == black:
                return
            if colors[u] == gray:
                print(111)
                raise RuntimeError()
            colors[u] = gray
            for v in adj[u]:
                dfs_visit(v)
            topo_seq.append(u)
            colors[u] = black

        try:
            dfs()
        except RuntimeError:
            return []
        if len(topo_seq) < n:
            return []
        return topo_seq[::-1]


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(set)
        indegrees = [0] * numCourses
        for u, v in prerequisites:
            edges[v].add(u)
            indegrees[u] += 1

        result = []
        free_nodes = {i for i in range(numCourses) if indegrees[i] == 0}
        while len(free_nodes) != 0:
            u = free_nodes.pop()
            result.append(u)
            for v in edges[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    free_nodes.add(v)

        if len(result) != numCourses:
            return []

        return result


solution = Solution()
print(solution.findOrder(4, [[2, 1], [3, 2], [1, 3], [1, 0]]))
