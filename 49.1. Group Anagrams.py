# task:
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.

# Runtime: 164 ms, faster than 36.89%
# Memory Usage: 18.2 MB, less than 41.90%
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()

sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(sol.groupAnagrams(strs = [""]))
# Output: [[""]]