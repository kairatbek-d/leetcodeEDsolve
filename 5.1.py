# task:
# Given a string s, return the longest palindromic substring in s.

# Для данной строки s вернуть самую длинную палиндромную подстроку в s.


class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.ans = s[0]
        
        for idx in range(1, len(s)):
            # odd case
            start, end = self.helper(idx, idx, s)
            if (end - start + 1) > len(self.ans):
                self.ans = s[start : end + 1]
            
            # even case
            start, end = self.helper(idx - 1, idx, s)
            if (end - start + 1) > len(self.ans):
                self.ans = s[start : end + 1]

        return self.ans
    
    # recursive solution
    # Runtime: 1850 ms, faster than 33.55%
    # def helper(self, left, right, s):
    #     if left < 0:
    #         return (0, right - 1)
        
    #     if right >= len(s):
    #         return (left + 1, len(s) - 1)
        
    #     if s[left] != s[right]:
    #         return (left + 1, right - 1)
        
    #     else:
    #         return self.helper(left - 1, right + 1, s)

    # iterative solution
    # Runtime: 1443 ms, faster than 41.33%
    def helper(self, left, right, s):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        
        return left + 1, right - 1


sol = Solution()
print(sol.longestPalindrome("babad")) # aca