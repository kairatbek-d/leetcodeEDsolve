# task:
# Given a string s, find the length of the longest substring without repeating characters.

# Для строки s найдите длину самой длинной подстроки без повторяющихся символов.


# Runtime: 68 ms, faster than 56.47% TOP
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        maximum=0
        for i in s:
            if i in seen:
                maximum = max(maximum, len(seen))
                seen = seen[seen.index(i)+1:] #slice 'seen' after the repeated element
            seen.append(i)
        maximum = max(maximum, len(seen))
        return maximum

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))