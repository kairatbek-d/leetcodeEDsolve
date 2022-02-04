# task:
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending
# position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.


# Runtime: 148 ms, faster than 18.44%
# Memory Usage: 15.4 MB, less than 85.57%
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]

sol = Solution()
print(sol.searchRange(nums = [], target = 0))