# task:
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
    # Each of the digits 1-9 must occur exactly once in each row.
    # Each of the digits 1-9 must occur exactly once in each column.
    # Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Runtime: 134 ms, faster than 88.55%
# Memory Usage: 14 MB, less than 89.16%
import collections
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows, cols, triples, visit = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set), collections.deque([])
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[(r // 3, c // 3)].add(board[r][c])
                else:
                    visit.append((r, c))
        def dfs():
            if not visit:
                return True
            r, c = visit[0]
            t = (r // 3, c // 3)
            for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
                    board[r][c] = dig
                    rows[r].add(dig)
                    cols[c].add(dig)
                    triples[t].add(dig)
                    visit.popleft()
                    if dfs():
                        return True
                    else:
                        board[r][c] = "."
                        rows[r].discard(dig)
                        cols[c].discard(dig)
                        triples[t].discard(dig)
                        visit.appendleft((r, c))
            return False
        dfs()

sol = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
sol.solveSudoku(board)
print(board)