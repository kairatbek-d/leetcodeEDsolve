# task:
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s
# atoi function).

# The algorithm for myAtoi(string s) is as follows:
# Read in and ignore any leading whitespace.
# 1. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if
# it is either. This determines if the final result is negative or positive respectively. Assume the result is
# positive if neither is present.
# 2. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of
# the string is ignored.
# 3. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the
# integer is 0. Change the sign as necessary (from step 2).
# 4. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it
# remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than
# 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.

# Note:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

import re
# Runtime: 47 ms, faster than 22.10%
# Memory Usage: 14.3 MB, less than 57.60%
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        if len(s) == 0:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        result = re.match("[0-9]+", s)
        if not result:
            return 0
        number = int(result.group(0))
        MAX_LIMIT = 2**31
        if number >= MAX_LIMIT:
            if sign == 1:
                return MAX_LIMIT - 1
            else:
                return - MAX_LIMIT
        return number * sign


sol = Solution()
print(sol.myAtoi("   -42"))