# 327. 区间和的个数
# 给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 区间和的个数 。
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
import bisect
from typing import List
from sortedcontainers import SortedList


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        acc = [0]
        for x in nums:
            acc.append(acc[-1] + x)

        lst = SortedList()
        result = 0
        for x in acc:
            # result += bisect.bisect_right(lst, x - lower) - bisect.bisect_left(lst, x - upper)
            result += lst.bisect_right(x-lower) - lst.bisect_left(x-upper)
            lst.add(x)

        return result

nums = [-2,5,-1]
lower = -2
upper = 2
print(Solution().countRangeSum(nums, lower, upper))

nums = [0]
lower = 0
upper = 0
print(Solution().countRangeSum(nums, lower, upper))
