'''
Given a list of dominoes, where dominoes[i] = [a, b].

Two dominoes are equivalent if:
    + (a == c and b == d) — they match exactly, or
    + (a == d and b == c) — one domino is the rotated version of the other.

Return the number of pairs (i, j) such that 0 <= i < j < dominoes.length and dominoes[i] is equivalent to dominoes[j].

Examples:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3

Дан список доминошек, где dominoes[i] = [a, b].

Две доминошки считаются эквивалентными, если:
    + (a == c и b == d) — то есть полностью совпадают, или
    + (a == d и b == c) — то есть одна доминошка является повёрнутой версией другой.

Нужно вернуть количество пар (i, j) таких, что 0 <= i < j < dominoes.length, и доминошка dominoes[i] эквивалентна доминошке dominoes[j].

Примеры:
Ввод: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Вывод: 1

Ввод: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Вывод: 3
'''

from typing import List

def number_of_equivalent_domino_pairs(dominoes: List[List[int]]) -> int:
    count_map = {}
    pairs_count = 0

    for a, b in dominoes:
        key = tuple(sorted((a, b)))
        if key in count_map:
            pairs_count += count_map[key]
            count_map[key] += 1
        else:
            count_map[key] = 1

    return pairs_count