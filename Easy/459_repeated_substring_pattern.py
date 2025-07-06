"""
Given a string S, determine whether it can be constructed by taking a non-empty substring of S and appending one or more copies of that substring together to form the original string.

Examples:
Input: "abab"
Output: true

Input: "aba"
Output: false

Дана строка S. Необходимо определить, можно ли составить эту строку путём многократного повторения её подстроки.

Примеры:
Ввод: "abab"
Вывод: true

Ввод: "aba"
Вывод: false
"""

def repeatedSubstringPattern(S: str) -> bool:
    doubled = (S + S)[1:-1]
    return S in doubled