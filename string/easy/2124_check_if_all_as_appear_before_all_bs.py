'''
You are given a string s that contains only the characters 'a' and 'b'.

Return True if all 'a' characters appear before any 'b' characters in the string. Otherwise, return False.

Examples:
Input: s = "aaabbb"
Output: True

Input: s = "abab"
Output: False

Дана строка s, состоящая только из символов 'a' и 'b'.

Верните True, если все символы 'a' стоят перед любыми символами 'b' в строке. Иначе верните False.

Примеры:
Ввод: s = "aaabbb"
Вывод: True

Ввод: s = "abab"
Вывод: False
'''

def check_string(s: str) -> bool:
    return "ba" not in s