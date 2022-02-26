# task:
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack
# each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Runtime: 70 ms, faster than 65.70%
# Memory Usage: 14.2 MB, less than 53.71%
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def queensToBoard(queens):
            board = [["."] * n for i in range(n)]
            for r, c in queens:
                board[r][c] = "Q"
            return ["".join(row) for row in board]
                
        
        def backtrack(currRow, queens, diagonals, antiDiagonals, cols, answer):
            """
            queens would look like [(r,c), ...]
            """
            if currRow == n:
                answer.append(queensToBoard(queens))
                return
            for col in range(n):
                currDiagonal = currRow - col
                currAntiDiagonal = currRow + col
                if (col not in cols
                    and currDiagonal not in diagonals
                    and currAntiDiagonal not in antiDiagonals):
                    queens.append((currRow, col))
                    cols.add(col)
                    diagonals.add(currDiagonal)
                    antiDiagonals.add(currAntiDiagonal)
                    backtrack(currRow+1, queens, diagonals, antiDiagonals, cols, answer)
                    cols.remove(col)
                    diagonals.remove(currDiagonal)
                    antiDiagonals.remove(currAntiDiagonal)
                    queens.pop()
        
        answer = []
        backtrack(0, [], set(), set(), set(), answer)
        return len(answer)

sol = Solution()
print(sol.totalNQueens(n = 4))
# Output: 2
print(sol.totalNQueens(n = 1))
# Output: 1