# task:
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Runtime: 51 ms, faster than 23.10%
# Memory Usage: 14.2 MB, less than 81.75%

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))