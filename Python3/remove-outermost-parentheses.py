# https://leetcode.com/problems/remove-outermost-parentheses/
#
# Program removes outermost parentheses from input string.
#
# Runtime: 40 ms, faster than 96.44% of Python3 online submissions for Remove Outermost Parentheses.
# Memory Usage: 13.2 MB, less than 56.21% of Python3 online submissions for Remove Outermost Parentheses.
# (5/28/2019)

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        solution = ""
        balance = begin = 0
        for i, par in enumerate(S):
            balance += 1 if par == "(" else -1
            if balance == 0:
                solution += S[begin + 1 : i]
                begin = i + 1
                balance = 0
        
        return solution
