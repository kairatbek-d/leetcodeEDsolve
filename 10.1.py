# task:
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and
# '*' where:
    #  '.' Matches any single character.​​​​
    # '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


# Runtime: 81 ms, faster than 35.16%
# Memory Usage: 14.4 MB, less than 61.02%
from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        is_non_empty = lambda i : i > -1
        is_empty = lambda i: not is_non_empty(i)
        
        # use python built-in cache as memoization for DP
        @cache
        def dp(src, pattern):
            
            if is_empty(src) and is_empty(pattern):
                
                # Accept on perfect match
                return True
            
            elif ( is_empty(src) and p[pattern] != '*') or is_empty(pattern):
                
                # Reject on invalid boundary cases
                
                # source string is empty with no wildcard star *  in pattern, or
                # pattern string is empty
                return False
            
            elif ( s[src] == p[pattern] ) or ( p[pattern] == '.' ):
                
                # Either current character is the same, or current character is matched with '.'
                # go to next round dp(src-1, pattern-1)
                return dp(src-1, pattern-1)
            
            elif p[pattern] == '*':
                
                # deinfe L = leading character of '*' in pattern
                L = p[pattern-1]
                
                if is_non_empty(src) and ( ( s[src] == L ) or ( L == '.' ) ):
                    
                    # Type_1: L* match current character once, pattern discards * after this round
                    # Type_2: L* match current character more than once, pattern keeps * after this round
                    # Type_3: L* match nothing, pattern discard L* after this round
                    return dp(src, pattern-1) or dp(src-1, pattern) or dp(src, pattern-2)
                
                else:
                    # Type_3: L* match nothing, pattern discard L* after this round
                    return dp(src, pattern-2)
            
            else:
                
                # Reject
                # current p[pattern] is not wildcard symbol, and s[src] != p[pattern]
                return False
        
        # --------------------------------------------
        tail_source_idx, tail_pattern_idx = len(s)-1, len(p)-1
        
        return dp(tail_source_idx, tail_pattern_idx)

sol = Solution()
print(sol.isMatch(s = "aab", p = ".*"))