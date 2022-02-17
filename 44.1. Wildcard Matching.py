# task:
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and
# '*' where:
    # '?' Matches any single character.
    # '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Runtime: 605 ms, faster than 74.52%
# Memory Usage: 14.2 MB, less than 93.39%
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        transfer = {}
        state = 0
        
        for char in p:
            if char == '*':
                transfer[state, char] = state
            else:
                transfer[state, char] = state + 1
                state += 1
        
        accept = state
        states = {0}
        
        for char in s:
            states = {transfer.get((at, token)) for at in states if at is not None for token in (char, '*', '?')}
        
        return accept in states

sol = Solution()
print(sol.isMatch(s = "aa", p = "*"))