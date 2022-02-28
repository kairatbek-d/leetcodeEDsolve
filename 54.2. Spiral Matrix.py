# task:
# Given an mxn matrix, return all elements of the matrix in spiral order.

# Runtime: 48 ms, faster than 39.10%
# Memory Usage: 13.8 MB, less than 92.72%
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

sol = Solution()
print(sol.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
# Output: [1,2,3,6,9,8,7,4,5]
print(sol.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]