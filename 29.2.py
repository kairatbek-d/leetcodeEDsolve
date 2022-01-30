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


# Runtime: 79 ms, faster than 5.12%
# Memory Usage: 13.8 MB, less than 99.96%
class Solution:
    # With bitwise operators:
    def divideWith(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum << 1) <= dividend:
                the_sum <<= 1
                current_quotient <<= 1            
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))

    # Without bitwise operators:
    def divideWithout(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)
        quotient = 0
        the_sum = divisor
        
        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum + the_sum) <= dividend:
                the_sum += the_sum
                current_quotient += current_quotient
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient
        
        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))
    
# How it works
# For example, we divide(5000, 14):
# After the first inner loop: the_sum = 3584 which is 14 multiplied 256 times.
# We can't multiply any more — because after 256 is coming 256 + 256 = 512 and 14 * 512 = 7168
# which is larger than our dividend, so we exit the inner loop,
# Reducing dividend: dividend = 5000 - 3584 = 1416
# And moving to another cycle of outer loop
# After the second inner loop: the_sum = 896 which is 14 multiplied 64 times.
# Third: the_sum = 448 which is 14 multiplied 32 times.
# And so on
# Finally we have: quotient = 256 + 64 + 32 + 4 + 1 = 357

sol = Solution()
print(sol.divideWith(dividend = 10, divisor = 3))
print(sol.divideWithout(dividend = 10, divisor = 3))