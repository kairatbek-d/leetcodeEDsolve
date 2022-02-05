# task:
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.


# Runtime: 89 ms, faster than 16.09%
# Memory Usage: 14.7 MB, less than 92.53%
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([x for x in nums if x < target])

sol = Solution()
print(sol.searchInsert(nums = [1,3,5,6], target = 5))