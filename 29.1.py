# task:
# Given two integers dividend and divisor, divide two integers without using multiplication,
# division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part.
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the
# 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly
# greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31,
# then return -2^31.


# Runtime: 49 ms, faster than 33.01%
# Memory Usage: 13.9 MB, less than 97.85%
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1): return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (dividend > 0) == (divisor > 0) else -res
sol = Solution()
print(sol.divide(dividend = 10, divisor = 3))