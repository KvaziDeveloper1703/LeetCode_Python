'''
You are given a string s. Your task is to find the length of the longest substring that contains no duplicate characters.
A substring is a contiguous sequence of characters within the string.

Examples:
Input: s = "abcabcbb"
Output: 3

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length