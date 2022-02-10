# task:
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
    # countAndSay(1) = "1"
    # countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then
    # converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of groups so that each group is
# a contiguous section all of the same character. Then for each group, say the number of characters, then say
# the character. To convert the saying into a digit string, replace the counts with a number and concatenate
# every saying.

# For example, the saying and conversion for digit string "3322251":
# two 3's, three 2's, one 5, and one 1
# 2 3 + 3 2 + 1 5 + 1 1
# 23321511

# Runtime: 74 ms, faster than 33.24%
# Memory Usage: 14.2 MB, less than 75.87%
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s

sol = Solution()
print(sol.countAndSay(n = 4)) # "1211"
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"