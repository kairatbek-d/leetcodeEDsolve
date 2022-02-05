# task: Hard
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of
# 0 and 1.

# Runtime: 1330 ms, faster than 25.62%
# Memory Usage: 19.4 MB, less than 21.71%
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index = {0: -1}
        balance = maxlen = 0
        for i, num in enumerate(nums):
            balance += num - 0.5
            maxlen = max(maxlen, i - index.setdefault(balance, i))
        return maxlen

        # return reduce(lambda(f,b,m),(i,x):(f,b+x-.5,max(m,i-f.setdefault(b+x-.5,i))),enumerate(nums),({0:-1},0,0))[2]

sol = Solution()
print(sol.findMaxLength(nums = [0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 2, 3]))