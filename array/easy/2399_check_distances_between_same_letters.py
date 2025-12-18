'''
You are given a 0-indexed string s consisting only of lowercase English letters, where each letter that appears in s appears exactly twice.

You are also given a 0-indexed integer array distance of length 26.

Each letter of the English alphabet is assigned an index from 0 to 25:
    - 'a' → 0
    - 'b' → 1
    - 'c' → 2
    - …
    - 'z' → 25

A string s is called well-spaced if, for every letter i that appears in s, the number of characters between the two occurrences of that letter is exactly distance[i].

If a letter does not appear in s, its corresponding value in distance can be ignored.

Return True if s is a well-spaced string. Otherwise, return False.

Вам дана строка s с нулевой индексацией, состоящая только из строчных английских букв, причём каждая буква, встречающаяся в s, появляется ровно два раза.

Также дан целочисленный массив distance с нулевой индексацией длины 26.

Каждой букве английского алфавита соответствует номер от 0 до 25:
    - 'a' → 0
    - 'b' → 1
    - 'c' → 2
    - …
    - 'z' → 25

Строка s называется правильно расставленной, если для каждой буквы i, присутствующей в строке, количество символов между двумя её вхождениями равно distance[i].

Если буква не встречается в строке s, соответствующее значение в массиве distance можно игнорировать.

Верните True, если строка s является well-spaced, иначе верните False.
'''

from typing import List

def check_distances(s: str, distance: List[int]) -> bool:
    first_position = {}

    for index, character in enumerate(s):
        if character in first_position:
            if index - first_position[character] - 1 != distance[ord(character) - ord('a')]:
                return False
        else:
            first_position[character] = index

    return True