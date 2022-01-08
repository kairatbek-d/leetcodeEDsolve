# task:
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


# Runtime: 60 ms, faster than 72.87%
# Memory Usage: 14.2 MB, less than 77.61%
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        l = len(y)
        z = 0
        aver = l // 2
        while z < aver:
            if y[z] != y[l-1-z]:
                break
            z+=1
        return z == aver

sol = Solution()
print(sol.isPalindrome(121))