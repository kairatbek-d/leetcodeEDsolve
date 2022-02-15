# task:
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how
# much water it can trap after raining.

# Runtime: 174 ms, faster than 11.58%
# Memory Usage: 15.9 MB, less than 15.01%
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [0] * n, [0] * n
        
        for i in range(1, n):
            maxLeft[i] = max(height[i-1], maxLeft[i-1])
        for i in range(n-2, -1, -1):
            maxRight[i] = max(height[i+1], maxRight[i+1])
            
        ans = 0
        for i in range(n):
            waterLevel = min(maxLeft[i], maxRight[i])
            if waterLevel > height[i]:
                ans += waterLevel - height[i]
        return ans

sol = Solution()
print(sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))