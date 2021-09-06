from typing import List
from collections import deque


class Solution:
    """
    给定一m行n列的网格，用一m*n长度的字符串grid表示
    字符串的每个字符，'0'表示空白，'1'表示障碍物，’2‘表示地铁站
    空白可以自由同行，障碍物不能通行，地铁站可以同行、并且所有地铁站两两之间的距离视为1
    求给定两点(row1, col1)和(row2, col2)之间的最短路径的长度.
    不可达返回-1
    """
    def shortest_path(self, grid: str, m: int, n: int,
                      source: List[int], dest: List[int]):
        inf = (m * n) + 1

        def index2coord(point):
            return point // n, point % n

        def coord2index(coord):
            return coord[0] * n + coord[1]

        barriers = {i for i in range(len(grid)) if grid[i] == '1'}
        stations = {i for i in range(len(grid)) if grid[i] == '2'}

        s = coord2index(source)
        d = coord2index(dest)
        distances = [inf] * (m * n)
        distances[s] = 0
        queue = deque([s])

        def get_neighbors(point):
            row, col = index2coord(point)
            up = row - 1, col
            down = row + 1, col
            left = row, col - 1
            right = row, col + 1
            for p in [up, down, left, right]:
                if 0 <= p[0] < m and 0 <= p[1] < n and p not in barriers:
                    yield coord2index(p)

            if point not in stations:
                return
            for p in stations:
                if p != point:
                    yield p

        while len(queue) != 0:
            point = queue.popleft()
            if point == d:
                return distances[d]
            neighbors = get_neighbors(point)
            for neighbor in neighbors:
                if distances[neighbor] == inf:
                    distances[neighbor] = distances[point] + 1
                    queue.append(neighbor)


        return -1

    @staticmethod
    def main():
        ans = Solution().shortest_path(
            grid='0000011200011102',
            m=4, n=4,
            source=[0, 0],
            dest=[3, 3]
        )
        print(ans)


Solution.main()
