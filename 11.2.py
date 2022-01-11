# task:
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


# Time Limit Exceeded
# Time Complexity: O(n^2)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                curr = min(height[i], height[j]) * (j-i)
                res = max(res, curr)
        return res

sol = Solution()
print(sol.maxArea([1,1]))