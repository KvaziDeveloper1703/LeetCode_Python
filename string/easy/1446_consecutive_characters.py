'''
The power of a string is defined as the maximum length of a non-empty substring that contains only one unique character.

Given a string S, return the power of S.

Examples:
Input: S = "leetcode"
Output: 2

Input: S = "abbcccddddeeeeedcba"
Output: 5

Сила строки определяется как максимальная длина непустой подстроки, которая состоит только из одного уникального символа.

Дана строка S. Нужно вернуть её силу.

Примеры:
Ввод: S = "leetcode"
Вывод: 2

Ввод: S = "abbcccddddeeeeedcba"
Вывод: 5
'''

from typing import List

def max_power(S: str) -> int:
    if not S:
        return 0

    max_power = 1
    current_run = 1

    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            current_run += 1
        else:
            current_run = 1
        if current_run > max_power:
            max_power = current_run

    return max_power