'''
A subsequence of a string is a sequence that can be formed by deleting some (possibly none) of the characters from the original string, without changing the order of the remaining characters.
Given two strings s and t, return true if s is a subsequence of t, and false otherwise.

Examples:
Input: s = "abc", t = "ahbgdc" → Output: true
Input: s = "axc", t = "ahbgdc" → Output: false
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)