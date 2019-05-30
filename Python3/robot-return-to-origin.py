# https://leetcode.com/problems/robot-return-to-origin/
#
# Function returns true if input string of cartesian movements returns to origin.
#
# Runtime: 60 ms, faster than 65.70% of Python3 online submissions for Robot Return to Origin.
# Memory Usage: 13.2 MB, less than 65.79% of Python3 online submissions for Robot Return to Origin.
# (5/30/2019)

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vert = horz = 0
        for move in moves:
            if move == 'L':
                horz -= 1
            elif move == 'R':
                horz += 1
            elif move == 'U':
                vert += 1
            elif move == 'D':
                vert -= 1
                
        return vert == horz == 0
