# task:
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Runtime: 46 ms, faster than 43.39%
# Memory Usage: 13.9 MB, less than 88.71%
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

sol = Solution()
print(sol.myPow(x = 2.00000, n = 10))
# x = 2.00000, n = 10
print(sol.myPow(x = 2.10000, n = 3))
# Output: 9.26100