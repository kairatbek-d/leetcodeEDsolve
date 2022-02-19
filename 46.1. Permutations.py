# task:
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in
# any order.

# Runtime: 44 ms, faster than 73.58%
# Memory Usage: 14.1 MB, less than 85.42%
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

sol = Solution()
print(sol.permute(nums = [1,2,3]))
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(sol.permute(nums = [0,1]))
# Output: [[0,1],[1,0]]