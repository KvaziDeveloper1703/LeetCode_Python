'''
You are given two strings s and t. Determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t, with the following rules:
+ Every occurrence of a character in s must be replaced with the same character in t.
+ The character mapping must preserve the order of characters.
+ No two characters in s can map to the same character in t, but a character can map to itself.

Examples:
Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True