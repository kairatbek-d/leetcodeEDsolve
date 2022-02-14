# task:
# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# Runtime: 1304 ms, faster than 39.02%
# Memory Usage: 59.6 MB, less than 96.23%
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0
                
        for i in range(n):
            if 1 <= nums[i] % (n + 1) <= n:
                ind = nums[i] % (n + 1) - 1
                nums[ind] += n + 1
          
        for i in range(n):
            if nums[i] <= n:
                return i + 1
        
        return n + 1

sol = Solution()
print(sol.firstMissingPositive(nums = [2, 2]))