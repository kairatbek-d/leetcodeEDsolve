# task:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two
# sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Для двух отсортированных массивов nums1 и nums2 размера m и n соответственно вернуть медиану двух
# отсортированных массивов.
# Общая сложность времени выполнения должна быть O (log (m + n)).


from typing import List


# Runtime: 80 ms, faster than 98.05%
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        size = len(nums1)
		
        if size % 2 != 0:
            mid = size // 2 
            return float(nums1[mid])
			
        else:
            mid = size // 2 
            return (nums1[mid] + nums1[mid-1]) / 2

sol = Solution()
print(sol.findMedianSortedArrays([1,2], [3,4]))