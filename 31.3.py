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

# Solution!!!:
# First observe that if a list of numbers is in descending order, then there is no lexicographically next greater permutation. Hence for i in range(n-1,0,-1), we search for the first occurrence of i such that nums[i] < nums[i+1]. If no such i exists, the list is in descending order, and we use nums.reverse() to reverse the list in-place. Otherwise, if such i exists, then nums[i-1] will be updated to get the lexicographically next greater permutation. Next, we need to search for the smallest number in nums[i:] that's larger than nums[i-1], and swap it with nums[i-1]. Note that nums[i:] is sorted in descending order. Hence we start with j = i, and while j < n and nums[j] > nums[i-1], we do idx = j, j += 1. When we are out of the while loop, nums[idx] will be the smallest number in nums[i:] that's larger than nums[i]. We then swap nums[idx] and nums[i-1]. After the swap, we just need to sort nums[i:] in ascending order to get the lexicographically next greater permutation. This can be achieved fairly easily in-place, because nums[i:] is already in descending order, and we just need to invert nums[i:] in-place to sort nums[i:] in ascending order.
# To illustrate the algorithm with an example, consider nums = [2,3,1,5,4,2]. It is easy to see that i = 2 is the first i (from the right) such that nums[i] < nums[i+1]. Then we swap nums[2] = 1 with the smallest number in nums[3:] that is larger than 1, which is nums[5] = 2, after which we get nums = [2,3,2,5,4,1]. To get the lexicographically next greater permutation of nums, we just need to sort nums[3:] = [5,4,1] in-place. Finally, we reach nums = [2,3,2,1,4,5].
# Time complexity: O(n), space complexity: O(1).

# Runtime: 64 ms, faster than 30.62%
# Memory Usage: 13.9 MB, less than 94.74%
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                j = i
                while j < n and nums[j] > nums[i-1]:
                    idx = j
                    j += 1
                nums[idx], nums[i-1] = nums[i-1], nums[idx]
                for k in range((n-i)//2):
                    nums[i+k], nums[n-1-k] = nums[n-1-k], nums[i+k]
                break
        else:
            nums.reverse()
        
        return nums

sol = Solution()
nums = [1,2,3]
print(sol.nextPermutation(nums = [1,2,3]))