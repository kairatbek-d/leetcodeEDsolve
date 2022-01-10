# task:
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and
# '*' where:
    #  '.' Matches any single character.​​​​
    # '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


# Runtime: 63 ms, faster than 45.64%
# Memory Usage: 14.7 MB, less than 15.41%
import functools

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @functools.cache
        def fwd(i, j):
            if i == len(s) and j == len(p):
                return True
            
            elif j == len(p):
                return False
            
            match = (i < len(s) and 
                     p[j] in [s[i], '.'])
            
            if (j + 1 < len(p) and
                p[j + 1] == '*'):
                
				# check whether it's best to skip * or match a character to it, if possible
				# start with 0 chars matched
                return (fwd(i, j + 2) or
                        match and fwd(i + 1, j))
            
            elif match:
                
                return fwd(i + 1, j + 1)
            
            else:
                return False
            
        @functools.cache
        def bwd(i, j):
            if i == -1 and j == -1:
                return True
            
            elif j == -1:
                return False
            
            if (p[j] == '*'):
                match = (i >= 0 and 
                         p[j - 1] in [s[i], '.'])
                
				# check whether it's best to skip * or match a character to it, if possible
				# start with 0 chars matched
                return (bwd(i, j - 2) or
                        match and bwd(i - 1, j))
            
            elif (i >= 0 and 
                  p[j] in [s[i], '.']):
                
                return bwd(i - 1, j - 1)
            
            else:
                return False
            
            
        return fwd(0, 0)
        # return bwd(len(s) - 1, len(p) - 1)

sol = Solution()
print(sol.isMatch(s = "aa", p = "a"))

# s = "aab", p = "c*a*b" # True
# s = "aa", p = "a" # False
# s = "aa", p = "a*" # True
# s = "ab", p = ".*" # True