# task:
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


# Runtime: 704 ms, faster than 86.67%
# Memory Usage: 27.7 MB, less than 5.65%
# Time: O(n) Space: O(1)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, i, j = 0, 0, len(height)-1
        while i != j:
            if height[j] > height[i]:
                area = height[i] * (j - i)
                i += 1
            else:
                area = height[j] * (j - i)
                j -= 1
            max_area = max(max_area, area)
        return max_area

sol = Solution()
print(sol.maxArea([1,1]))