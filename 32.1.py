# task:
# Given a string containing just the characters '(' and ')', find the length of the longest valid
# (well-formed) parentheses substring.


# Runtime: 58 ms, faster than 46.56%
# Memory Usage: 14.7 MB, less than 44.05%
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp, stack = [0]*(len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    print(stack)
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1
                    print(dp)
        return max(dp)

sol = Solution()
print(sol.longestValidParentheses(s = "(((((((((()()"))