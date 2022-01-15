# task:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.


# Runtime: 716 ms, faster than 90.58%
# Memory Usage: 17.7 MB, less than 35.31%

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        print(nums[:-2])
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return list(map(list, res))

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))