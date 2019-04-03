
/*/
https://leetcode.com/problems/goat-latin/

Program changes input string into 'goat latin'.

Runtime: 4 ms, faster than 100.00% of C++ online submissions for Goat Latin.
Memory Usage: 9.1 MB, less than 100.00% of C++ online submissions for Goat Latin.
(4/3/2019)
/*/

class Solution {
public:
    string toGoatLatin(string S) {
        
        string solution;
        istringstream iss(S);
        
        vector<string> subStrings = {istream_iterator<string>{iss},
                                     istream_iterator<string>{}};
        
        for(int i = 0; i < subStrings.size(); ++i) {
            
            if(!isVowel(subStrings[i][0])) {
                subStrings[i] += subStrings[i][0];
                subStrings[i].erase(0, 1);
            }
            subStrings[i] += "ma";
            
            for(int j = 0; j <= i; ++j) 
                subStrings[i] += "a";
            
            solution += subStrings[i];
            
            if(i < subStrings.size() - 1) 
                solution += " ";
        }
        
        return solution;
        
    }
        
    bool isVowel (char c) {
    char vowels[] = {'a', 'e', 'i', 'o', 'u', 
                     'A', 'E', 'I', 'O', 'U'};

    return (find(begin(vowels), end(vowels), c) != end(vowels));
    }
};
