# task:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two
# sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Для двух отсортированных массивов nums1 и nums2 размера m и n соответственно вернуть медиану двух
# отсортированных массивов.
# Общая сложность времени выполнения должна быть O (log (m + n)).


from typing import List


# Runtime: 93 ms, faster than 52.31%
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for nums in nums1:
            nums2.append(nums)
        nums2.sort()
        if len(nums2)%2!=0:
            median =nums2[int(len(nums2)/2)]
        else:
            median =(nums2[int(len(nums2)/2)]+nums2[int(len(nums2)/2)-1])/2
        return median


sol = Solution()
print(sol.findMedianSortedArrays([1,2], [3,4]))