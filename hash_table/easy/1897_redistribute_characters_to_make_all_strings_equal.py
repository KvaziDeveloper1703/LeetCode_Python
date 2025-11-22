'''
You are given an array of strings words.

In one operation, you may choose two different indices i and j, where words[i] is non-empty, and move any one character from words[i] to any position in words[j].

Return True if it is possible to make all strings in words identical by performing any number of such operations. Otherwise, return False.

Examples:
Input: words = ["abc", "aabc", "bc"]
Output: True

Input: words = ["ab", "a"]
Output: False

Дан массив строк words.

За одну операцию можно выбрать два разных индекса i и j, где words[i] - непустая строка, и переместить один любой символ из words[i] в любое место строки words[j].

Верните True, если можно сделать все строки массива одинаковыми, выполнив любое количество таких операций. Иначе верните False.

Примеры:
Ввод: words = ["abc", "aabc", "bc"]
Вывод: True

Ввод: words = ["ab", "a"]
Вывод: False
'''

from typing import List
from collections import Counter

def make_equal(words: List[str]) -> bool:
    total_counts = Counter()

    for current_word in words:
        total_counts.update(current_word)

    number_of_words = len(words)

    for character, count in total_counts.items():
        if count % number_of_words != 0:
            return False

    return True