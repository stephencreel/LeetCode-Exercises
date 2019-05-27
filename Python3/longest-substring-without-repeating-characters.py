
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Program returns the size of longest unique substring within input string.
#
# Runtime: 52 ms, faster than 99.50% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13 MB, less than 89.12% of Python3 online submissions for Longest Substring Without Repeating Characters.
# (5/26/2019)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sDict = {}
        length = start = 0
        
        for i, char in enumerate(s):
            
            if char in sDict and start <= sDict[char]:
                start = sDict[char] + 1
            else:
                length = max(length, i - start + 1)
                
            sDict[char] = i
            
        return length
