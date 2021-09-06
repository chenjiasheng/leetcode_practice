from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negative = defaultdict(int)
        positive = defaultdict(int)
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            elif num < 0:
                negative[-num] += 1
            elif num > 0:
                positive[num] += 1

        def solve(dict1, dict2):
            keys1 = sorted(dict1.keys())
            keys2 = sorted(dict2.keys())
            result2 = []
            for x in keys1:
                for y in keys2:
                    z = x - y
                    if z < y:
                        break
                    elif z == y:
                        if z in dict2 and dict2[z] >= 2:
                            result2.append([x, y, y])
                    else:
                        if z in dict2 and dict2[z] >= 1:
                            result2.append([x, y, z])
            return result2

        result = []
        result1 = solve(negative, positive)
        for r in result1:
            result.append((-r[0], r[1], r[2]))

        result2 = solve(positive, negative)
        for r in result2:
            result.append((-r[2], -r[1], r[0]))

        if zero_count > 0:
            for x in negative:
                if x in positive:
                    result.append((-x, 0, x))

        if zero_count >= 3:
            result.append((0, 0, 0))

        return result


nums = [0,0,1,2,3,-1,-2,-3, 1, -1]
print(Solution().threeSum(nums))


