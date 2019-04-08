/*/
https://leetcode.com/problems/palindrome-number/

Program returns bool indicating if input number is palindromic.

Runtime: 32 ms, faster than 99.62% of C++ online submissions for Palindrome Number.
Memory Usage: 8 MB, less than 100.00% of C++ online submissions for Palindrome Number.
(4/8/2019)
/*/

class Solution {
public:
    bool isPalindrome(int x) {
        
        // If Input Single Digit Return True
        if(x >= 0 && x < 9) return true;
        
        // If Input Negative Number or Divisible by 10 Return False
        if(x < 0 || x % 10 == 0) return false;
        
        // Reverse Least Significant Half of Input
        int reverse = 0;
        while (reverse < x) {
            reverse = reverse * 10 + (x % 10);
            x /= 10;
        }
        
        // If Odd Input Remove Center Digit
        if(reverse > x) reverse /= 10;
        
        // Return True if Input Equals Reversed Section
        return x == reverse;

    }
};
