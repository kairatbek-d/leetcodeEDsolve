# task:
# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of
# haystack.
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an
# interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is
# consistent to C's strstr() and Java's indexOf().


# Runtime: 68 ms, faster than 41.44%
# Memory Usage: 16.9 MB, less than 5.14%
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def kmp(str_):
            b, prefix = 0, [0]
            for i in range(1, len(str_)):
                while b > 0 and str_[i] != str_[b]:
                    b = prefix[b - 1]
                if str_[b] == str_[i]:
                    b += 1
                else:
                    b = 0
                prefix.append(b)
            return prefix

        str_ = kmp(needle + '#' + haystack)
        n = len(needle)
        if n == 0:
            return n
        for i in range(n + 1, len(str_)):
            if str_[i] == n:
                return i - 2 * n
        return -1

sol = Solution()
print(sol.strStr(haystack = "hello", needle = "ll"))