# task:
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Runtime: 47 ms, faster than 28.28%
# Memory Usage: 14.4 MB, less than 24.87%

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs)) # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        prefix = ""
        for i in l: # ('f', 'f', 'f') continue
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))