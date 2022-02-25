# task:
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack
# each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any
# order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both
# indicate a queen and an empty space, respectively.

# Runtime: 88 ms, faster than 63.36%
# Memory Usage: 14.4 MB, less than 93.07%
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

sol = Solution()
print(sol.solveNQueens(n = 4))
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(sol.solveNQueens(n = 1))
# Output: [["Q"]]