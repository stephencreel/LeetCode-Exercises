/*/
https://leetcode.com/problems/reverse-integer/

Program reverses an input integer and returns 0 if integer overflow occurs.

Runtime: 4 ms, faster than 100.00% of C++ online submissions for Reverse Integer.
Memory Usage: 8 MB, less than 100.00% of C++ online submissions for Reverse Integer.
(4/1/2019)
/*/

class Solution {
public:
    int reverse(int number) {
        
        int solution = 0;
        while (number != 0) {
            
            // Remove Least Significant Digit from Input and Store
            int digit = number % 10;
            number = number / 10;
            
            // Append Digit to Solution
            long long temp = solution;
            temp = (temp * 10) + digit;
            
            // Return 0 if Integer Overflow
            if(temp > INT_MAX || temp < INT_MIN) return 0;
            solution = temp;
        }
        return solution;
    }
};
