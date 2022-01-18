# task:
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a],
# nums[b], nums[c], nums[d]] such that:
    # 0 <= a, b, c, d < n
    # a, b, c, and d are distinct.
    # nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.


# Runtime: 1732 ms, faster than 24.94%
# Memory Usage: 14.2 MB, less than 77.15%

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        seen = set()
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    lastNumber = target - nums[i] - nums[j] - nums[k]
                    if lastNumber in seen:
                        arr = sorted([nums[i], nums[j], nums[k], lastNumber])
                        ans.add((arr[0], arr[1], arr[2], arr[3]))
            seen.add(nums[i])
        return ans


sol = Solution()
print(sol.fourSum(nums = [1,0,-1,0,-2,2], target = 0))