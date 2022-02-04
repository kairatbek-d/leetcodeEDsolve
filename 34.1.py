# task:
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending
# position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.


# Runtime: 119 ms, faster than 39.30%
# Memory Usage: 15.3 MB, less than 85.57%
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) // 2
                l, r = search(lo, mid), search(mid+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        return [-1, -1] if len(nums) == 0 else search(0, len(nums)-1)

sol = Solution()
print(sol.searchRange(nums = [], target = 0))