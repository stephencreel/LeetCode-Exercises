/*/
https://leetcode.com/problems/reverse-integer/

Program reverses an input integer and returns 0 if integer overflow occurs.

Runtime: 4 ms, faster than 100.00% of C++ online submissions for Reverse Integer.
Memory Usage: 8.2 MB, less than 99.80% of C++ online submissions for Reverse Integer.
(4/1/2019)
/*/

class Solution {
public:
    int reverse(int number) {
        
        // Store as long long to Avoid Integer Overflow Error
        long long solution = 0;
        
        while (number != 0) {

            // Append Least Significant Digit from Input to Solution
            solution = (solution * 10) + number % 10;
            
            // Remove Digit from Input
            number = number / 10;
        }
        
        // Return Reversed Integer or 0 if Integer Overflow
        if(solution > INT_MAX || solution < INT_MIN) return 0;
        return solution;
    }
};
