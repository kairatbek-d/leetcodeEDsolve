# task:
# Given an integer array numss of length n and an integer target, find three integers in numss
# such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.


# Runtime: 128 ms, faster than 71.12%
# Memory Usage: 14.4 MB, less than 11.26%

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result


sol = Solution()
print(sol.threeSumClosest(nums = [0,2,1,-3], target = 1))