'''
You are given a string allowed consisting of distinct characters, and an array of strings words.

A string is called consistent if every character in that string appears in the string allowed.

Return the number of consistent strings in the array words.

Examples:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7

Дана строка allowed, состоящая из уникальных символов, и массив строк words.

Строка называется допустимой, если все её символы содержатся в строке allowed.

Верни количество допустимых строк в массиве words.

Примеры:
Ввод: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Вывод: 2

Ввод: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Вывод: 7
'''

from typing import List

def count_consistent_strings(allowed: str, words: List[str]) -> int:
    allowed_characters = set(allowed)
    consistent_strings_count = 0

    for current_word in words:
        is_consistent_string = True
        for character in current_word:
            if character not in allowed_characters:
                is_consistent_string = False
                break
        if is_consistent_string:
            consistent_strings_count += 1

    return consistent_strings_count