/*/
https://leetcode.com/problems/hamming-distance/

Program calculates the Hamming Distance between two input integers.

Runtime: 0 ms, faster than 100.00% of C++ online submissions for
Hamming Distance. (1/25/2019)
/*/

class Solution {
public:
    int hammingDistance(int x, int y) {
        
        vector<int> xBin = convertToBinary(x);
        vector<int> yBin = convertToBinary(y);
        
        while(xBin.size() != yBin.size()) {
            if(xBin.size() > yBin.size()) yBin.insert(yBin.begin(), 0);
            else xBin.insert(xBin.begin(), 0);
        }
        
        int solution = 0;
        for(int i = 0; i < xBin.size(); ++i) 
            if(xBin[i] != yBin[i]) ++solution;
        
        return solution;
    }
    
    vector<int> convertToBinary(int n) {
        
        vector<int> binary;
        while(n != 0) {
            binary.insert(binary.begin(), n % 2);
            n /= 2;
        }
        return binary;
    }
};
