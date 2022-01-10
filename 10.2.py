# task:
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and
# '*' where:
    #  '.' Matches any single character.​​​​
    # '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


# Runtime: 77 ms, faster than 36.38%
# Memory Usage: 14.4 MB, less than 38.12%
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return not re.match(f"^{p}$", s) is None

sol = Solution()
print(sol.isMatch(s = "aab", p = "c*a*b"))