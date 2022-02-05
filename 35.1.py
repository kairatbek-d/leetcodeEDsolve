# task:
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Runtime: 113 ms, faster than 5.31%
# Memory Usage: 14.8 MB, less than 92.53%
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        beg, end = 0, len(nums)
        while beg < end:
            mid = (beg + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                beg = mid + 1
        return beg

sol = Solution()
print(sol.searchInsert(nums = [1,3,5,6], target = 5))