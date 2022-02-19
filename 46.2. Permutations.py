# task:
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in
# any order.

# Runtime: 53 ms, faster than 53.63%
# Memory Usage: 14 MB, less than 94.76%
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]

sol = Solution()
print(sol.permute(nums = [1,2,3]))
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(sol.permute(nums = [0,1]))
# Output: [[0,1],[1,0]]