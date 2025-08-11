'''
Given an array of strings words and a string chars.
A string is considered good if it can be formed using the characters from chars.

Return the total sum of the lengths of all good strings from words.

Examples:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10

Дан массив строк words и строка chars.
Строка считается хорошей, если её можно составить из букв строки chars.

Верните сумму длин всех хороших строк из массива words.

Примеры:
Ввод: words = ["cat","bt","hat","tree"], chars = "atach"
Вывод: 6

Ввод: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Вывод: 10
'''

from typing import List
from collections import Counter

def count_characters(words: List[str], chars: str) -> int:
    chars_counter = Counter(chars)
    total = 0

    for w in words:
        w_counter = Counter(w)
        if all(w_counter[c] <= chars_counter.get(c, 0) for c in w_counter):
            total += len(w)
    return total