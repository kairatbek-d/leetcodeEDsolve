# task:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they
# add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Учитывая массив целых чисел nums и целочисленную цель, верните индексы двух чисел, чтобы они в сумме
# равнялись цели.
# Вы можете предположить, что каждый вход будет иметь ровно одно решение, и вы не можете использовать один
# и тот же элемент дважды.
# Вы можете вернуть ответ в любом порядке.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # my OWN solution -> 9740 ms and 5.01%
        # answer = []
        # for x in range(len(nums)):
        #     for y in range(len(nums)):
        #         if x != y and nums[x] + nums[y] == target:
        #             answer.extend([x, y])
        #             return answer

        # my second OWN+extra solution -> 4000 ms and 26.61%
        # for x in range(0, len(nums)-1):
        #     for y in range(x+1, len(nums)):
        #         if nums[x] + nums[y] == target:
        #             return [x, y]

        # from discussion 0(n) solution using hashmap -> 121 ms and 40.90%
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            
            if remaining in seen:
                return [i, seen[remaining]]
            
            seen[value] = i

sol = Solution()
print(sol.twoSum([3, 2, 4], 6))