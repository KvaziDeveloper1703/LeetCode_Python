'''
Given a string s containing words and spaces, return the length of the last word in the string.
A word is defined as the longest sequence of non-space characters.

Examples:
Input: s = "Hello World"
Output: 5 (The last word is "World")

Input: s = " fly me to the moon "
Output: 4 (The last word is "moon")

Input: s = "luffy is still joyboy"
Output: 6 (The last word is "joyboy")
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])