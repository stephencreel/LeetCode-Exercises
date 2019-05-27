# https://leetcode.com/problems/two-sum/
#
# Program returns indices of numbers in list that add to input target number.
#
# Runtime: 32 ms, faster than 99.21% of Python3 online submissions for Two Sum.
# Memory Usage: 14.5 MB, less than 23.17% of Python3 online submissions for Two Sum.
# (5/26/2019)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        dictNums = {}
        for index, value in enumerate(nums):
            if value in dictNums:
                return [dictNums[value], index]
            dictNums[target - value] = index
