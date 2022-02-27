# task:
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the
# largest sum and return its sum.
# A subarray is a contiguous part of an array.

# Runtime: 718 ms, faster than 93.01%
# Memory Usage: 28.6 MB, less than 33.26%
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        x = 0
        total = nums[0]
        for i in nums:
            x += i
            if x > total:
                total = x
            if x < 0:
                x= 0
        return total

        # maxSum = nowSum = nums[0]
        
        # for num in nums[1:]:
        #     if nowSum <=0:
        #         nowSum = num
        #     else:
        #         nowSum += num
                
        #     if nowSum>maxSum:
        #         maxSum = nowSum
                    
        # return maxSum

sol = Solution()
print(sol.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
print(sol.maxSubArray(nums = [1]))
# Output: 1