# task:
# Given a string containing just the characters '(' and ')', find the length of the longest valid
# (well-formed) parentheses substring.


# Runtime: 61 ms, faster than 42.61%
# Memory Usage: 14.3 MB, less than 94.06%
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [0]
        longest = 0
        
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]
        return longest

sol = Solution()
print(sol.longestValidParentheses(s = "(((((((((()()"))