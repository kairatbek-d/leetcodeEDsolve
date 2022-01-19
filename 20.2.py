# task:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
# the input string is valid.

# An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.


# Runtime: 69 ms, faster than 5.15%
# Memory Usage: 14.4 MB, less than 36.11%
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        n = len(s)
        if n == 0:
            return True
        if n % 2 != 0:
            return False
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        if s == '':
            return True
        else:
            return False

sol = Solution()
print(sol.isValid(s="()"))