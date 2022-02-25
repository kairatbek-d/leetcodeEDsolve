# task:
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack
# each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any
# order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both
# indicate a queen and an empty space, respectively.

# Runtime: 88 ms, faster than 63.36%
# Memory Usage: 14.5 MB, less than 54.31%
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
        return answer

sol = Solution()
print(sol.solveNQueens(n = 4))
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(sol.solveNQueens(n = 1))
# Output: [["Q"]]