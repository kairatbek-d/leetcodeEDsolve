# task:
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and
# '*' where:
    # '?' Matches any single character.
    # '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Runtime: 252 ms, faster than 84.26%
# Memory Usage: 13.9 MB, less than 99.31%
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]

sol = Solution()
print(sol.isMatch(s = "aa", p = "*"))