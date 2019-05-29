# https://leetcode.com/problems/unique-morse-code-words/
#
# Program returns number of unique strings of words converted into morse code.
#
# Runtime: 32 ms, faster than 98.71% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 12.8 MB, less than 90.63% of Python3 online submissions for Unique Morse Code Words.
# (5/28/2019)

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                 ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        unique = {"".join(morse[ord(char) - 97] for char in word) for word in words}
            
        return len(unique)
