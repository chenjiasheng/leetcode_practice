from sortedcontainers import SortedList


class Solution(object):
    def countSmaller(self, nums):
        lst = SortedList()
        result = []
        for x in nums[::-1]:
            result.append(lst.bisect_left(x))
            lst.add(x)
        return result[::-1]


nums = [5,2,6,1]
print(Solution().countSmaller(nums))
