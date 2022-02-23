# task:
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Runtime: 40 ms, faster than 58.04%
# Memory Usage: 13.9 MB, less than 67.32%
class Solution:
    def myPow(self, x: float, n: int) -> float:
        current=0
        y=n//2
        if n==0:
            return 1
        if y>=0:
            if n==1:
                return x
            current=self.myPow(x,y)
        else:
            if n==-1:
                return 1/x
            current=self.myPow(x,y)
        if n%2==0:
            return current*current
        else:
            return current*current*x

sol = Solution()
print(sol.myPow(x = 2.00000, n = 10))
# x = 2.00000, n = 10
print(sol.myPow(x = 2.10000, n = 3))
# Output: 9.26100