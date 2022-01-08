# task:
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


# Runtime: 64 ms, faster than 61.51%
# Memory Usage: 14.3 MB, less than 15.78%
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        l = list()
        n = 0
        while(x > 9):
            l.append(x % 10)
            x //= 10
            n += 1

        l.append(x)
        p = 0
        while (p < n):
            if(l[p] != l[n]):
                return False
            p += 1
            n -= 1

        return True

sol = Solution()
print(sol.isPalindrome(121))