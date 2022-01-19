# task:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
# the input string is valid.

# An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.


# Runtime: 28 ms, faster than 90.02%
# Memory Usage: 14.4 MB, less than 36.11%
class Solution:
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

sol = Solution()
print(sol.isValid(s="()"))