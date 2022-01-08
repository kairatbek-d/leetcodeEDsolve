# task:
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


# Runtime: 48 ms, faster than 96.15% 
# Memory Usage: 14.3 MB, less than 15.78%
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):   
            return False

        reversedNum = 0
        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10
            x = x // 10

        return True if (x == reversedNum or x == reversedNum // 10) else False

sol = Solution()
print(sol.isPalindrome(121))