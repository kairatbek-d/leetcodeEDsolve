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

# Runtime: 49 ms, faster than 68.11%
# Memory Usage: 13.8 MB, less than 97.71%
import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            # original
            # s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
            
            # decomposed
            v = '' # accumulator string
            # iterate the characters (digits) grouped by digit
            for digit, group in itertools.groupby(result):
                count = len(list(group)) # eg. the 2 in two 1s 
                v += "%i%s" % (count, digit) # create the 21 string and accumulate it
            result = v # save to result for the next for loop pass

        # return the accumulated string
        return result

sol = Solution()
print(sol.countAndSay(n = 4)) # "1211"