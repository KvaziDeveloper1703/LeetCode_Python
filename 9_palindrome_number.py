'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Examples:
Input:
x = 121
Output:
true

Input:
x = -121
Output:
false
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x != 0 and x % 10 == 0:
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10