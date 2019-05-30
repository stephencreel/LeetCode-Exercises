# https://leetcode.com/problems/height-checker/
#
# Program returns number of elements in list out of sorted order.
#
# Runtime: 24 ms, faster than 99.82% of Python3 online submissions for Height Checker.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Height Checker.
# (5/30/2019)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        sortHeight = sorted(heights)
        return sum([h != s for h, s in zip(heights, sortHeight)])
