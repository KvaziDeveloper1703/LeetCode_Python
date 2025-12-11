'''
You are given an array of strings words and a string s.
Both words[i] and s consist only of lowercase English letters.

Your task is to return the number of strings in words that are prefixes of s.

A prefix is a substring that appears at the beginning of a string, and a substring is a continuous sequence of characters.

Вам дан массив строк words и строка s.
Все строки words[i] и строка s состоят только из строчных английских букв.

Нужно вернуть количество строк из words, которые являются префиксами строки s.

Префикс - это подстрока, расположенная в начале строки; подстрока - это непрерывная последовательность символов.
'''

from typing import List

def count_prefixes(words_list: List[str], target_string: str) -> int:
    number_of_prefixes = 0

    for current_word in words_list:
        if target_string.startswith(current_word):
            number_of_prefixes += 1

    return number_of_prefixes