'''
Given a string s, find whether there exists any substring of length 2 that is also present in the reverse of s.
Return True if such a substring exists, otherwise return False.

Examples:
Input: s = "leetcode"
Output: True

Input: s = "abcba"
Output: True

Дана строка s. Необходимо определить, существует ли хотя бы одна подстрока длины 2, которая также встречается в перевёрнутой строке s.
Верните True, если такая подстрока существует, иначе верните False.

Примеры:
Ввод: s = "leetcode"
Вывод: True

Ввод: s = "abcba"
Вывод: True
'''

def is_substring_present(s: str) -> bool:
    reversed_string = s[::-1]

    for index in range(len(s) - 1):
        substring = s[index:index + 2]
        if substring in reversed_string:
            return True

    return False