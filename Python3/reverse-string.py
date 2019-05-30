# https://leetcode.com/problems/reverse-string/
#
# Program reverses input string in place.
#
# Runtime: 164 ms, faster than 93.60% of Python3 online submissions for Reverse String.
# Memory Usage: 17.4 MB, less than 61.63% of Python3 online submissions for Reverse String.
# (5/30/2019)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        length = (len(s))
        for i in range(length // 2):
            s[i], s[length - 1 - i] = s[length - 1 - i], s[i]
