# task:
# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of
# haystack.
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an
# interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is
# consistent to C's strstr() and Java's indexOf().

# Time Limit Exceeded - if simle logic
# Runtime: 48 ms, faster than 68.78%
# Memory Usage: 14.2 MB, less than 99.17%
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            print(i, haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

sol = Solution()
print(sol.strStr(haystack = "hello", needle = "ll"))