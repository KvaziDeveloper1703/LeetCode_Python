'''
Given a string s, reverse the order of the words.
+ A word is a sequence of non-space characters.
+ Words are separated by at least one space.
+ The output should contain the words in reverse order, joined by a single space.
+ Remove any extra spaces — no leading, trailing, or multiple spaces between words.

Examples:
Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = " hello world "
Output: "world hello"

Input: s = "a good example"
Output: "example good a"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])