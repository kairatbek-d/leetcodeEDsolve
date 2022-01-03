# task:
# Given a string s, find the length of the longest substring without repeating characters.

# Для строки s найдите длину самой длинной подстроки без повторяющихся символов.


# Runtime: 77 ms, faster than 40.11%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=-1
        maxLen=0
        starting=0
        letterDict=dict()

        for item in s:
            count+=1
            print(letterDict)
            if letterDict.get(item)==None or letterDict[item]<starting:
                letterDict[item]=count
                maxLen=max(maxLen,count-starting+1)
            else:
                starting=letterDict[item]+1
                letterDict[item]=count
        return maxLen

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))