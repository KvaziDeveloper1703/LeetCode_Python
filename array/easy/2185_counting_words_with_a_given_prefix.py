'''
You are given an array of strings words and a string pref.

Return the number of strings in words that have pref as their prefix.

A prefix of a string s is any contiguous substring that starts at the beginning of s.

Examples:
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0

Дан массив строк words и строка pref.

Нужно вернуть количество строк из words, которые имеют pref в качестве префикса.

Префикс строки s - это любой непрерывный подстрочный фрагмент, начинающийся с первого символа строки.

Примеры:
Ввод: words = ["pay","attention","practice","attend"], pref = "at"
Вывод: 2

Ввод: words = ["leetcode","win","loops","success"], pref = "code"
Вывод: 0
'''

from typing import List

def prefix_count(words: List[str], pref: str) -> int:
    count = 0
    for word in words:
        if word.startswith(pref):
            count += 1
    return count