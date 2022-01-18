# task:
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a],
# nums[b], nums[c], nums[d]] such that:
    # 0 <= a, b, c, d < n
    # a, b, c, and d are distinct.
    # nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.


# Runtime: 97 ms, faster than 89.14%
# Memory Usage: 14.3 MB, less than 77.15%

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results


sol = Solution()
print(sol.fourSum(nums = [1,0,-1,0,-2,2], target = 0))