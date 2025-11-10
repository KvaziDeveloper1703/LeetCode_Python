'''
You are given two string arrays, word_1 and word_2.

Return True if the two arrays represent the same string, and False otherwise.

A string is represented by an array if the concatenation of all its elements forms that string.

Examples:
Input: word_1 = ["ab", "c"], word_2 = ["a", "bc"]
Output: True

Input: word_1 = ["a", "cb"], word_2 = ["ab", "c"]
Output: False

Даны два массива строк: word_1 и word_2.

Нужно вернуть True, если оба массива представляют одну и ту же строку, и False - в противном случае.

Строка представляется массивом, если конкатенация всех его элементов по порядку образует эту строку.

Примеры:
Ввод: word_1 = ["ab", "c"], word_2 = ["a", "bc"]
Вывод: True

Ввод: word_1 = ["a", "cb"], word_2 = ["ab", "c"]
Вывод: False
'''

from typing import List

def array_strings_are_equal(word_1: List[str], word_2: List[str]) -> bool:
    return "".join(word_1) == "".join(word_2)