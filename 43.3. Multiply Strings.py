# task:
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and
# num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Runtime: 269 ms, faster than 17.73% 
# Memory Usage: 13.9 MB, less than 93.17%
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1)+len(num2))
        for i in range(len(num1)-1, -1, -1):
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                tmp = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0')) + carry
                carry = (res[i+j+1]+tmp) // 10
                res[i+j+1] = (res[i+j+1]+tmp) % 10
            res[i] += carry
        res = ''.join(map(str, res))
        return '0' if not res.lstrip('0') else res.lstrip('0')

sol = Solution()
print(sol.multiply(num1 = "2", num2 = "3"))