from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        max_index = max(range(len(height)), key=height.__getitem__)

        result = 0

        i = 0
        for j in range(1, max_index + 1):
            if height[j] >= height[i]:
                result += height[i] * (j - i) - sum(height[i:j])
                i = j

        i = len(height) - 1
        for j in range(len(height) - 2, max_index - 1, -1):
            if height[j] >= height[i]:
                result += height[i] * (i - j) - sum(height[i:j:-1])
                i = j

        return result



height = [2, 0, 2]
print(Solution().trap(height))