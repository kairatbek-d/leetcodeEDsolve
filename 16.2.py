# task:
# Given an integer array numss of length n and an integer target, find three integers in numss
# such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.


# Runtime: 144 ms, faster than 56.77%
# Memory Usage: 14.3 MB, less than 43.68%

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if abs(s-target) < abs(res-target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else: # break early 
                    return res
        return res


sol = Solution()
print(sol.threeSumClosest(nums = [0,2,1,-3], target = 1))