'''
You are given a 0-indexed array of strings words.
Define a boolean function isPrefixAndSuffix(str1, str2) as follows:
    - The function returns true if str1 is both a prefix and a suffix of str2;
    - Otherwise, it returns false.

Return the number of index pairs (i, j) such that:
    - i < j;
    - isPrefixAndSuffix(words[i], words[j]) is true.

Examples:
Input: words = ["a","aba","ababa","aa"]
Output: 4

Input: words = ["pa","papa","ma","mama"]
Output: 2

Дан 0-индексированный массив строк words.
Определим булеву функцию isPrefixAndSuffix(str1, str2):
    - Функция возвращает true, если строка str1 является одновременно префиксом и суффиксом строки str2.
    - В противном случае функция возвращает false.

Найдите количество пар индексов (i, j), таких что:
    - i < j;
    - isPrefixAndSuffix(words[i], words[j]) возвращает true.

Примеры:
Ввод: words = ["a","aba","ababa","aa"]
Вывод: 4

Ввод: words = ["pa","papa","ma","mama"]
Вывод: 2
'''

from typing import List

def count_prefix_suffix_pairs(words: List[str]) -> int:
    pairs_count = 0
    number_of_words = len(words)

    for first_index in range(number_of_words):
        for second_index in range(first_index + 1, number_of_words):
            if (words[second_index].startswith(words[first_index]) and words[second_index].endswith(words[first_index])):
                pairs_count += 1

    return pairs_count