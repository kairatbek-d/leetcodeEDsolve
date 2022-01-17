# task:
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that
# 1 does not map to any letters.


# Runtime: 47 ms, faster than 21.62%
# Memory Usage: 14.4 MB, less than 33.39%

from functools import reduce
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])


sol = Solution()
print(sol.letterCombinations("23"))