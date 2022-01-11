# task:
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


# Runtime: 1060 ms, faster than 17.27%
# Memory Usage: 27.6 MB, less than 23.04%
# Time: O(n) Space: O(1)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = res = 0
        r = len(height) - 1
        
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if (height[l] < height[r]): l += 1
            else: r -= 1
                
        return res

sol = Solution()
print(sol.maxArea([1,1]))