# task:
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations
# in any order.

# Runtime: 48 ms, faster than 99.48%
# Memory Usage: 14 MB, less than 98.34%
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break              #handles duplication
            ans = new_ans
        return ans

sol = Solution()
print(sol.permuteUnique(nums = [1,1,2]))
# Output: [[1,1,2],[1,2,1],[2,1,1]]
print(sol.permuteUnique(nums = [1,2,3]))
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]