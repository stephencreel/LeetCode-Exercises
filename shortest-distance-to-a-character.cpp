/*/
https://leetcode.com/problems/shortest-distance-to-a-character/

Program finds the shortest distance to input character for every
character in an input string.
/*/

class Solution {
public:
    vector<int> shortestToChar(string S, char C) {
    
        vector<int> positions;
        vector<int> solution;
        
        for(int i = 0; i < S.size(); ++i) {
            if(S[i] == C) positions.push_back(i);
        }
        
        for(int i = 0; i < S.size(); ++i) {
            int minPos = INT_MAX;
            
            for(int pos : positions) {
                minPos = min(minPos, abs(pos - i));
            }
            
            solution.push_back(minPos);
        }    
        
        return solution;
    }
};
