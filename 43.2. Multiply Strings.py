# task:
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and
# num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Runtime: 151 ms, faster than 46.81%
# Memory Usage: 13.9 MB, less than 93.17%
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        
        for n1 in num1:
            temp = 0
            for n2 in num2:
                temp = temp * 10 + int(n1) * int(n2)
            ans = ans * 10 + temp

        return str(ans)

sol = Solution()
print(sol.multiply(num1 = "2", num2 = "3"))