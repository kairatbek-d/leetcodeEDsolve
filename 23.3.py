# task:
# Given n pairs of parentheses, write a function to generate all combinations of well-formed
# parentheses.


# Runtime: 54 ms, faster than 30.43%
# Memory Usage: 14.6 MB, less than 40.69%
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l - r < 0 or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(x)
            s.append((x+"(", l+1, r))
            s.append((x+")", l, r+1))
        return res

sol = Solution()
print(sol.generateParenthesis(3))