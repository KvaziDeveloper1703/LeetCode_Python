'''
A palindrome is a phrase that reads the same forward and backward after:
+ Converting all letters to lowercase
+ Removing all non-alphanumeric characters (only letters and numbers are kept)

Given a string s, return true if it is a palindrome, otherwise return false.

Examples:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Input: s = "race a car"
Output: false

Input: s = " "
Output: true
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]