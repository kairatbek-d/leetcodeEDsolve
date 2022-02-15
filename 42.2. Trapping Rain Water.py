# task:
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how
# much water it can trap after raining.

# Runtime: 196 ms, faster than 8.16%
# Memory Usage: 17.1 MB, less than 6.46%
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        waterLevel = []
        left = 0
        for h in height:
            left = max(left, h) 
            waterLevel += [left] # over-fill it to left max height
        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            waterLevel[i] = min(waterLevel[i], right) - h # drain to the right height
        return sum(waterLevel)

sol = Solution()
print(sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))