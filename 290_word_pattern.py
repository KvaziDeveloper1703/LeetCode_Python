'''
You are given a pattern (a string of lowercase letters) and a string s consisting of words separated by spaces.
Determine if s follows the same pattern.
For s to follow the pattern, there must be a bijection between:
+ Each character in pattern, and
+ Each non-empty word in s.

This means:
+ Each letter in pattern maps to exactly one unique word in s.
+ Each word in s maps to exactly one unique letter in pattern.
+ No two letters can map to the same word, and no two words can map to the same letter.

Examples:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for p, w in zip(pattern, words):
            if p in char_to_word:
                if char_to_word[p] != w:
                    return False
            else:
                char_to_word[p] = w

            if w in word_to_char:
                if word_to_char[w] != p:
                    return False
            else:
                word_to_char[w] = p

        return True