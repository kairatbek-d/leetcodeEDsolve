# task:
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# Runtime: 75 ms, faster than 37.35%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # when no conversion is required
        if len(s) < numRows or numRows == 1: return s
        
        # store each row of the result in a list
        rows, rev, count = [''] * numRows, False, 0
        
        for i in s:
            rows[count] += i
            if rev:
                count -= 1
            else:
                count += 1
            # change direction when count hits N or 0
            if count == numRows - 1 or count == 0:
                rev = not rev
        # join rows together
        return ''.join(rows)

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3)) # PAHNAPLSIIGYIR