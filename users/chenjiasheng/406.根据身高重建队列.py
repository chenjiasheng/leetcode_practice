from typing import List
import bisect


class BinaryIndexTree:
    def __init__(self, n):
        self.n = n
        self.lst = [0] * n
        self.bit = [0] * (n + 1)

    @staticmethod
    def lsb(x):
        return x & (-x)

    def update(self, i, x):
        diff = x - self.lst[i]
        self.lst[i] = x
        while i < self.n:
            self.bit[i + 1] += diff
            i = i + self.lsb(i + 1)

    def sum(self, i):
        result = 0
        while i > 0:
            result += self.bit[i]
            i = i - self.lsb(i)
        return result

    def __getitem__(self, i):
        return self.sum(i + 1)

    def __len__(self):
        return self.n


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        sorted_people = sorted(people, key=lambda p: (p[0], -p[1]))

        bit = BinaryIndexTree(n)
        for i in range(n):
            bit.update(i, 1)

        indices = []
        for p in sorted_people:
            pos = bisect.bisect_right(bit, p[1])
            indices.append(pos)
            bit.update(pos, 0)

        result = [None] * n
        for index, person in zip(indices, sorted_people):
            result[index] = person

        return result


people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(Solution().reconstructQueue(people))

people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
print(Solution().reconstructQueue(people))
