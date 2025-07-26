'''
Given a string S of length n, representing a permutation pattern of n + 1 integers from the range [0, n].

The permutation perm must satisfy the following rules:
    + If S[i] == 'I', then perm[i] < perm[i + 1]
    + If S[i] == 'D', then perm[i] > perm[i + 1]

Return any valid permutation perm that satisfies the pattern S.

Examples:
Input: S = "IDID"
Output: [0, 4, 1, 3, 2]

Input: S = "III"
Output: [0, 1, 2, 3]

Дана строка S длины n, представляющая шаблон перестановки из n + 1 чисел в диапазоне [0, n].

Нужно восстановить перестановку perm такую, что:
    + Если s[i] == 'I', то perm[i] < perm[i + 1]
    + Если s[i] == 'D', то perm[i] > perm[i + 1]

Верните любую допустимую перестановку perm, которая соответствует шаблону s.

Примеры:
Ввод: S = "IDID"
Вывод: [0, 4, 1, 3, 2]

Ввод: S = "III"
Вывод: [0, 1, 2, 3]
'''

from typing import List

def di_string_match(S: str) -> List[int]:
    low, high = 0, len(S)
    result = []

    for character in S:
        if character == 'I':
            result.append(low)
            low += 1
        else:
            result.append(high)
            high -= 1

    result.append(low)
    return result