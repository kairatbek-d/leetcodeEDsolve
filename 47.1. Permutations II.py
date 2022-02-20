# task:
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations
# in any order.

# Runtime: 52 ms, faster than 97.86%
# Memory Usage: 14.3 MB, less than 83.46%
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

sol = Solution()
print(sol.permuteUnique(nums = [1,1,2]))
# Output: [[1,1,2],[1,2,1],[2,1,1]]
print(sol.permuteUnique(nums = [1,2,3]))
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]