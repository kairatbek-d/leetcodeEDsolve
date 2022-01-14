# task:
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Runtime: 20 ms, faster than 99.77%
# Memory Usage: 14.5 MB, less than 24.87%

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
				#since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))