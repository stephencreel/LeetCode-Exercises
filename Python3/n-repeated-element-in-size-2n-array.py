# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
#
# Given an input list of size 2N with N unique elements and one additional element repeated N times,
# the program returns the repeated element.
#
# Runtime: 36 ms, faster than 99.81% of Python3 online submissions for N-Repeated Element in Size 2N Array.
# Memory Usage: 14.3 MB, less than 25.58% of Python3 online submissions for N-Repeated Element in Size 2N Array.
# (5/28/2019)

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        unique = {}
        
        for num in A:
            if num in unique.keys():
                return num
            else:
                unique[num] = 1
