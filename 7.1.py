# task:
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to
# go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Constraints: 
#   -231 <= x <= 231 - 1

# Runtime: 65 ms, faster than 5.22%
# Memory Usage: 13.9 MB, less than 99.95%
class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(x)[::-1]) if x >= 0 else (int(str(abs(x))[::-1]) * -1)
        return 0 if (result > 2147483647 or result < -2147483648) else result


sol = Solution()
print(sol.reverse(-123))