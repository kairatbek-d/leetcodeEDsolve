# task:
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in
# any order.

from functools import reduce
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Runtime: 58 ms, faster than 45.08%
        # Memory Usage: 13.9 MB, less than 94.76%
        # return list(itertools.permutations(nums))

        # Runtime: 76 ms, faster than 14.52%
        # Memory Usage: 14 MB, less than 94.76%
        # return map(list, itertools.permutations(nums))

        # Runtime: 78 ms, faster than 12.15%
        # Memory Usage: 14 MB, less than 94.76%
        return reduce(lambda P, n: [p[:i] + [n] + p[i:] for p in P for i in range(len(p)+1)], nums, [[]])

sol = Solution()
print(sol.permute(nums = [1,2,3]))
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(sol.permute(nums = [0,1]))
# Output: [[0,1],[1,0]]