# task:
# Given an mxn matrix, return all elements of the matrix in spiral order.

# Runtime: 28 ms, faster than 95.26%
# Memory Usage: 13.8 MB, less than 99.54%
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return None
        
        n, m = len(matrix), len(matrix[0])
        
        direction = 1
        res = []
        x, y = 0, -1
        
        while n > 0 and m > 0:
            for _ in range(m):
                y += direction
                res.append(matrix[x][y])
            n -= 1
            
            for _ in range(n):
                x += direction
                res.append(matrix[x][y])
            m -= 1     
            direction *= -1
            
        return res

sol = Solution()
print(sol.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
# Output: [1,2,3,6,9,8,7,4,5]
print(sol.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]