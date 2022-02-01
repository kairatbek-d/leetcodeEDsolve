# task:
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3],
# [1,3,2], [3,1,2], [2,3,1].
# The next permutation of an array of integers is the next lexicographically greater permutation
# of its integer. More formally, if all the permutations of the array are sorted in one container
# according to their lexicographical order, then the next permutation of that array is the
# permutation that follows it in the sorted container. If such arrangement is not possible,
# the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
    # For example, the next permutation of arr = [1,2,3] is [1,3,2].
    # Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    # While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a
    # lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.


# Runtime: 73 ms, faster than 17.75%
# Memory Usage: 14 MB, less than 94.74%
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find longest non-increasing suffix
        right = len(nums)-1
        while nums[right] <= nums[right-1] and right-1 >=0:
            right -= 1
        if right == 0:
            return self.reverse(nums,0,len(nums)-1)
        # find pivot
        pivot = right-1
        successor = 0
        # find rightmost succesor
        for i in range(len(nums)-1,pivot,-1):
            if nums[i] > nums[pivot]:
                successor = i
                break
        # swap pivot and successor
        nums[pivot],nums[successor] = nums[successor],nums[pivot]  
        # reverse suffix
        self.reverse(nums,pivot+1,len(nums)-1)
        
        return nums
        
    def reverse(self, nums, l, r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1

sol = Solution()
nums = [1,2,3]
print(sol.nextPermutation(nums = [1,2,3]))