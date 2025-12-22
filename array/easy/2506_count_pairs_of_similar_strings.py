'''
You are given a 0-indexed array of strings called words.

Two strings are considered similar if they consist of the same set of characters, regardless of their order or frequency.

For example:
    - "abca" and "cba" are similar because both contain the characters 'a', 'b', and 'c';
    - "abacba" and "bcfd" are not similar because they do not contain the same characters.

Your task is to return the number of pairs (i, j) such that:
    - 0 ≤ i < j < words.length;
    - words[i] and words[j] are similar strings.

Examples:
Input: words = ["aba", "aabb", "abcd", "bac", "aabc"]
Output: 2

Input: words = ["aabb", "ab", "ba"]
Output: 3

Дан массив строк words, индексированный с нуля.

Две строки считаются похожими, если они состоят из одинакового набора символов, независимо от порядка и количества повторений.

Например:
    - строки "abca" и "cba" похожи, так как обе содержат символы 'a', 'b' и 'c';
    - строки "abacba" и "bcfd" не похожи, так как их наборы символов различаются.

Необходимо найти количество пар (i, j), для которых выполняются условия:
    - 0 ≤ i < j < words.length;
    - строки words[i] и words[j] являются похожими.

Примеры:
Ввод:  words = ["aba", "aabb", "abcd", "bac", "aabc"]
Вывод: 2

Ввод:  words = ["aabb", "ab", "ba"]
Вывод: 3
'''

from collections import Counter
from typing import List

def similar_pairs(words: List[str]) -> int:
    character_sets_count = Counter()

    for word in words:
        character_set = frozenset(word)
        character_sets_count[character_set] += 1

    number_of_pairs = 0
    for count in character_sets_count.values():
        number_of_pairs += count * (count - 1) // 2

    return number_of_pairs