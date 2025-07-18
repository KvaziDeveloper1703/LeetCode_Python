'''
Given a string S that consists of lowercase and/or uppercase English letters, return the length of the longest palindrome that can be built using the letters from S.
    + Letters are case-sensitive — for example, "Aa" is not a palindrome;
    + You may rearrange the letters in any way to build the palindrome.

Examples:
Input: S = "abccccdd"
Output: 7

Input: S = "a"
Output: 1

Дана строка S, состоящая из строчных и/или прописных английских букв. Необходимо вернуть длину самого длинного палиндрома, который можно составить из этих букв.
    + Буквы различаются по регистру — например, "Aa" не считается палиндромом;
    + Буквы в строке можно переставлять в любом порядке, чтобы получить палиндром.

Примеры:
Ввод: S = "abccccdd"
Вывод: 7

Ввод: S = "a"
Вывод: 1
'''

from collections import Counter

def longest_palindrome(S: str) -> int:
    character_counts = Counter(S)
    palindrome_length = 0

    for count in character_counts.values():
        pairs = (count // 2) * 2
        palindrome_length += pairs

    if palindrome_length < len(letters):
        palindrome_length += 1

    return palindrome_length