# task:
# Given n pairs of parentheses, write a function to generate all combinations of well-formed
# parentheses.


# Runtime: 37 ms, faster than 54.71%
# Memory Usage: 14.5 MB, less than 88.76%
from typing import List


class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left-1, right, ans, string + "(")
        if right:
            self.dfs(left, right-1, ans, string + ")")


sol = Solution()
print(sol.generateParenthesis(3))