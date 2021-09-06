from typing import List
import heapq
import math

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjs = [[] for _ in range(n)]
        for (u, v), prob in zip(edges, succProb):
            w = -math.log(prob)
            adjs[u].append([v, w])
            adjs[v].append([u, w])

        INF = 10**10
        ds = [INF for _ in range(n)]
        ds[start] = 0
        q = [(0, start)]
        while len(q) != 0:
            d, u = heapq.heappop(q)
            if d != ds[u]:
                assert d > ds[u]
                continue
            if u == end:
                return math.exp(-ds[u])
            for v, w in adjs[u]:
                alt = ds[u] + w
                if alt < ds[v]:
                    ds[v] = alt
                    heapq.heappush(q, (d + w, v))

        return 0


n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
print(Solution().maxProbability(n, edges, succProb, start, end))

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.3]
start = 0
end = 2
print(Solution().maxProbability(n, edges, succProb, start, end))


n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2
print(Solution().maxProbability(n, edges, succProb, start, end))


n = 1
edges = []
succProb = []
start = 0
end = 0
print(Solution().maxProbability(n, edges, succProb, start, end))


n = 4
edges = [[3,0],[3,2],[0,1],[2,1]]
succProb = [math.exp(-x) for x in [3,1,2,5]]
start = 1
end = 3
print(Solution().maxProbability(n, edges, succProb, start, end))

