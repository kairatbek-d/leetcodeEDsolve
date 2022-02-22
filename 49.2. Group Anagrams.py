# task:
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.

# Runtime: 148 ms, faster than 48.59%
# Memory Usage: 17.8 MB, less than 54.29%
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return groups.values()

sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(sol.groupAnagrams(strs = [""]))
# Output: [[""]]