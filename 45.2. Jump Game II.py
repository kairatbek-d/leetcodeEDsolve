# task:
# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# Runtime: 170 ms, faster than 68.56% 
# Memory Usage: 15 MB, less than 81.37%
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        Nlen, curr, nxt, ans, i = len(nums) - 1, -1, 0, 0, 0
        while nxt < Nlen:
            if i > curr:
                ans += 1
                curr = nxt
            nxt = max(nxt, nums[i] + i)
            i += 1
        return ans

sol = Solution()
print(sol.jump(nums = [2,3,1,1,4]))
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1,
# then 3 steps to the last index.
print(sol.jump(nums = [2,3,1,1,4]))
# Output: 2