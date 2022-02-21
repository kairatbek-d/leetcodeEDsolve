# task:
# You are given an nxn 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

# Runtime: 27 ms, faster than 98.50%
# Memory Usage: 14 MB, less than 73.48%
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        depth = n // 2
        for i in range(depth):
            rlen, opp = n - 2 * i - 1, n - 1 - i
            for j in range(rlen):
                temp = matrix[i][i+j]
                matrix[i][i+j] = matrix[opp-j][i]
                matrix[opp-j][i] = matrix[opp][opp-j]
                matrix[opp][opp-j] = matrix[i+j][opp]
                matrix[i+j][opp] = temp
        return matrix

sol = Solution()
print(sol.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
# Output: [[7,4,1],[8,5,2],[9,6,3]]
print(sol.rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]