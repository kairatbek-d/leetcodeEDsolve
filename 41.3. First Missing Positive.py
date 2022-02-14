# task:
# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses constant extra space.

from typing import List


class Solution:
    # O(n) time
    # Runtime: 1156 ms, faster than 50.04%
    # Memory Usage: 59.6 MB, less than 96.23%
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
        
    # O(nlgn) time
    # Runtime: 1107 ms, faster than 54.11%
    # Memory Usage: 59.4 MB, less than 99.21%
    def firstMissingPositive2(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res

sol = Solution()
print(sol.firstMissingPositive(nums = [2, 2]))
print(sol.firstMissingPositive2(nums = [2, 2]))