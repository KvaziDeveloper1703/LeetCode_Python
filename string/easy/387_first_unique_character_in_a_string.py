'''
Given a string S, find the first non-repeating character in it and return its index. If there is no such character, return -1.

Examples:
Input: S = "leetcode"
Output: 0

Input: S = "loveleetcode"
Output: 2

Дана строка S. Найдите первый неповторяющийся символ в строке и верните его индекс. Если такого символа не существует, верните -1.

Примеры:
Ввод: S = "leetcode"
Вывод: 0

Ввод: S = "loveleetcode"
Вывод: 2
'''

from collections import Counter

def first_unique_char(S: str) -> int:
    character_counts = Counter(S)

    for index, character in enumerate(S):
        if character_counts[character] == 1:
            return index

    return -1