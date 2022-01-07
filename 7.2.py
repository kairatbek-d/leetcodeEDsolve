# task:
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to
# go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Constraints: 
#   -231 <= x <= 231 - 1

# Runtime: 28 ms, faster than 90.32%
# Memory Usage: 14.3 MB, less than 34.39% 
class Solution:
    def reverse(self, x: int) -> int:
        t=0
        if(x<0):
            t=str(abs(x))
            t=t[::-1]
            t=int(t)
            t=t-2*t
        else:
            t=str(x)
            t=t[::-1]
            t=int(t)
        if(t<=((2**31)-1) and t>=(-2**31)):
            return(t)
        else:
            return 0


sol = Solution()
print(sol.reverse(-123))