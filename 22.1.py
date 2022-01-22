# task:
# Given n pairs of parentheses, write a function to generate all combinations of well-formed
# parentheses.


# Runtime: 43 ms, faster than 46.82%
# Memory Usage: 14.7 MB, less than 11.30%
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]

sol = Solution()
print(sol.generateParenthesis(3))