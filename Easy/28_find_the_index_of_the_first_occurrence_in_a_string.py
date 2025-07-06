'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack.
If needle is not found, return -1.

Examples:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Input: haystack = "leetcode", needle = "leeto"
Output: -1

Даны две строки — needle и haystack. Верните индекс первого вхождения подстроки needle в строку haystack.
Если needle не найден в haystack, верните -1.

Примеры:
Ввод: haystack = "sadbutsad", needle = "sad"
Вывод: 0

Ввод: haystack = "leetcode", needle = "leeto"
Вывод: -1
'''

def index_of_substring(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1