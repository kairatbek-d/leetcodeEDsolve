# task:
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how
# much water it can trap after raining.

# Runtime: 140 ms, faster than 24.96%
# Memory Usage: 15.8 MB, less than 34.62%
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftCursor, rightCursor = 0, len(height)-1
        leftMax, rightMax, storedWater = 0, 0, 0
        
        while (leftCursor <= rightCursor):
            leftMax = max(leftMax, height[leftCursor])
            rightMax = max(rightMax, height[rightCursor])
            if leftMax < rightMax:
                storedWater += leftMax - height[leftCursor]
                leftCursor += 1
            else:
                storedWater += rightMax - height[rightCursor]
                rightCursor -= 1
                
        return storedWater

sol = Solution()
print(sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))