'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack.
If needle is not found, return -1.

Examples:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Input: haystack = "leetcode", needle = "leeto"
Output: -1
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        if m == 0:
            return 0

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1