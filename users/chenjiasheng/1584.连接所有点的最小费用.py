import heapq

class Solution1(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)

        def distance(ij):
            i, j = ij
            a, b = points[i], points[j]
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        edges = [(i, j) for i in range(n) for j in range(n) if i < j]
        edges.sort(key=distance)

        class UFS:
            def __init__(self, n):
                self.parents = list(range(n))
                self.sizes = [1] * n

            def find(self, x):
                if self.parents[x] != x:
                    self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

            def union(self, x, y):
                x = self.find(x)
                y = self.find(y)
                if x == y:
                    return
                if self.sizes[x] < self.sizes[y]:
                    x, y = y, x
                self.parents[y] = x
                self.sizes[x] += self.sizes[y]

        ufs = UFS(n)
        mst = []
        for edge in edges:
            i, j = edge
            if ufs.find(i) == ufs.find(j):
                continue
            ufs.union(i, j)
            mst.append(edge)
            if len(mst) == n - 1:
                break

        cost = sum(distance(edge) for edge in mst)
        return cost


class Solution(object):
    def minCostConnectPoints(self, points):
        points = [tuple(p) for p in points]

        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        p0 = points[0]
        heap = [(distance(p0, p), p) for p in points[1:]]
        heapq.heapify(heap)
        remain = {p: distance(p0, p) for p in points[1:]}

        cost = 0

        while len(heap) != 0:
            d, p = heapq.heappop(heap)
            if p not in remain:
                continue
            cost += remain[p]
            for p1 in remain:
                new_distance = distance(p1, p)
                if new_distance < remain[p1]:
                    remain[p1] = new_distance
                    heapq.heappush(heap, (new_distance, p1))

            del remain[p]

        return cost



points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(Solution().minCostConnectPoints(points))

points = [[3,12],[-2,5],[-4,1]]
print(Solution().minCostConnectPoints(points))

points = [[0,0],[1,1],[1,0],[-1,1]]
print(Solution().minCostConnectPoints(points))

points = [[-1000000,-1000000],[1000000,1000000]]
print(Solution().minCostConnectPoints(points))

points = [[0,0]]
print(Solution().minCostConnectPoints(points))
