# https://leetcode.com/problems/reverse-integer/
#
# Program returns reversed input 32-bit integer or 0 if overflow occurs.
#
# Runtime: 36 ms, faster than 94.82% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.3 MB, less than 44.18% of Python3 online submissions for Reverse Integer.
# (5/27/2019)

class Solution:
    def reverse(self, x: int) -> int:
        
        sign = -1 if x < 0 else 1
        
        reverse = int(str(x * sign)[::-1])
            
        return sign * reverse * (reverse < 2**31)
