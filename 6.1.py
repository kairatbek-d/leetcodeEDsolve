# task:
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# Runtime: 68 ms, faster than 48.79%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        leng = len(s)
        count = 0
        for x in range(numRows):
            if leng == 1 or numRows == 1:
                count += 1
                return s
            if x > 0 and x < numRows-1:
                for y in range(x, leng, numRows+numRows-2):
                    count += 1
                    res+=s[y]
                    res+= "" if numRows-x+y+numRows-2-x>=leng else s[numRows-x+y+numRows-2-x]
            else:
                for y in range(x, len(s), numRows+numRows-2):
                    count += 1
                    res+=s[y]
        return res


sol = Solution()
print(sol.convert("PAYPALISHIRING", 4))