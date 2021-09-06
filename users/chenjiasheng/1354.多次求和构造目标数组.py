from typing import List
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [-x for x in target]
        heapq.heapify(heap)
        heap_sum = -sum(heap)

        while -heap[0] != 1:
            print([-x for x in heap])
            max_value = -heap[0]
            others_sum = heap_sum - max_value
            if others_sum == 0:
                return False
            if max_value < others_sum + 1:
                return False
            sub = (max_value - 1) // others_sum * others_sum
            new_value = max_value - sub
            heap_sum -= sub
            heapq.heapreplace(heap, -new_value)

        return True


if __name__ == '__main__':
    solution = Solution()
    cases = [
        [1],
        [1,1,1],
        [3],
        [1,1,1,2],
        [9,3,5],
        [8,5],
        [9,5],
        [9,1,1],
        [1000000001,1,3],
        [1000000001,1,4],
        [2,900000002]
    ]
    for case in cases:
        print(case, solution.isPossible(case))
