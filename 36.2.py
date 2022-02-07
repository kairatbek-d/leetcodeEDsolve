# task:
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the
# following rules:
    # Each row must contain the digits 1-9 without repetition.
    # Each column must contain the digits 1-9 without repetition.
    # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
    # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    # Only the filled cells need to be validated according to the mentioned rules.

# Runtime: 92 ms, faster than 93.25%
# Memory Usage: 14 MB, less than 90.40%
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first
        # big = set()
        # for i in range(0,9):
        #     for j in range(0,9):
        #         if board[i][j]!='.':
        #             cur = board[i][j]
        #             if (i,cur) in big or (cur,j) in big or (i/3,j/3,cur) in big:
        #                 return False
        #             big.add((i,cur))
        #             big.add((cur,j))
        #             big.add((i/3,j/3,cur))
        # return True

        # second
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(c,j),(i,c),(i/3,j/3,c)]
        return len(seen) == len(set(seen))

sol = Solution()
print(sol.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(sol.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(sol.isValidSudoku(board = 
[[".",".",".",".","5",".",".","1","."]
,[".","4",".","3",".",".",".",".","."]
,[".",".",".",".",".","3",".",".","1"]
,["8",".",".",".",".",".",".","2","."]
,[".",".","2",".","7",".",".",".","."]
,[".","1","5",".",".",".",".",".","."]
,[".",".",".",".",".","2",".",".","."]
,[".","2",".","9",".",".",".",".","."]
,[".",".","4",".",".",".",".",".","."]])) # expected false