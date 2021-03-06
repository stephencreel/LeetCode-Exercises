// https://leetcode.com/problems/unique-email-addresses/
//
// Program returns number of unique e-mail addresses in input vector.

class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {

        unordered_set<string> solution;
        
        for(string email : emails) {
            int at = email.find('@');
            string name = email.substr(0, at);
            string host = (email.substr(at, email.size()));
            if(name.find('+') != string::npos) name = name.substr(0, name.find('+'));
            name.erase(remove(name.begin(), name.end(), '.'), name.end());
            solution.insert(name + host);
        }
        return solution.size();
    }
};
