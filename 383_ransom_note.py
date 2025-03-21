"""
You are given two strings: ransomNote and magazine. Return true if the ransomNote can be constructed using the letters from magazine, and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Examples:

Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for character, count in ransom_count.items():
            if magazine_count[character] < count:
                return False
        return True