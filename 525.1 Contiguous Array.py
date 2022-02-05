# task: Hard
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of
# 0 and 1.

# Runtime: 1149 ms, faster than 40.35%
# Memory Usage: 19.2 MB, less than 29.95%
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        hash = {}
        count = 0
        for i in range(len(nums)):
            current = nums[i]
            if current == 0:
                count -= 1 # decrement our count if our current element is 0
            else:
                # increment our count if current element is 1
             count += 1

            if count == 0:
                # if count is 0, we have a new subarray with length+1
                max_length = i+1
            if count in hash:
                max_length = max(max_length, i-hash[count]) 
            else:
                hash[count] = i
        return max_length

sol = Solution()
print(sol.findMaxLength(nums = [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 2, 3]))