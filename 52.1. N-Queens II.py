# task:
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack
# each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Runtime: 36 ms, faster than 99.15%
# Memory Usage: 14 MB, less than 73.98%
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return len(result)

sol = Solution()
print(sol.totalNQueens(n = 4))
# Output: 2
print(sol.totalNQueens(n = 1))
# Output: 1