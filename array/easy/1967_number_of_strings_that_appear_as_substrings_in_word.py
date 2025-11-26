'''
You are given an array of strings patterns and a string word.
Return the number of strings in patterns that appear as a substring in word.

A substring is a continuous sequence of characters within a string.

Examples:
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3

Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2

Дан массив строк patterns и строка word.
Нужно вернуть количество строк из patterns, которые встречаются как подстрока в word.

Подстрока - это непрерывная последовательность символов внутри строки.

Примеры:
Ввод: patterns = ["a","abc","bc","d"], word = "abc"
Вывод: 3

Ввод: patterns = ["a","b","c"], word = "aaaaabbbbb"
Вывод: 2
'''

from typing import List

def number_of_strings(patterns: List[str], word: str) -> int:
    number_of_patterns_in_word = 0
    for pattern in patterns:
        if pattern in word:
            number_of_patterns_in_word += 1
    return number_of_patterns_in_word