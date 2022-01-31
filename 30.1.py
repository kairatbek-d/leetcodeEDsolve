# task:
# You are given a string s and an array of strings words of the same length. Return all starting
# indices of substring(s) in s that is a concatenation of each word in words exactly once, in any
# order, and without any intervening characters.
# You can return the answer in any order.


# Runtime: 128 ms, faster than 81.77%
# Memory Usage: 14.2 MB, less than 95.54%
from typing import List


class Solution:
    def _findSubstring(self, l, r, n, k, t, s, req, ans):
        curr = {}
        while r + k <= n:
            w = s[r:r + k]
            r += k
            if w not in req:
                l = r
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > req[w]:
                    curr[s[l:l + k]] -= 1
                    l += k
                if r - l == t:
                    ans.append(l)
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        for i in range(min(k, n - t + 1)):
            self._findSubstring(i, i, n, k, t, s, req, ans)
        return ans

sol = Solution()
print(sol.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
print(sol.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))