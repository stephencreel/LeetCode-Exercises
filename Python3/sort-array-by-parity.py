# https://leetcode.com/problems/sort-array-by-parity/
#
# Program returns input list sorted by parity (all even numbers followed by all odd numbers).
#
# Runtime: 60 ms, faster than 98.99% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 13.8 MB, less than 34.49% of Python3 online submissions for Sort Array By Parity.
# (5/29/2019)

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even, odd = [], []
        for num in A:
            if num & 1:
                odd.append(num)
            else:
                even.append(num)
        
        return even + odd
