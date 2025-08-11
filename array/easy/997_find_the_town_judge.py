'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of them is secretly the town judge.

If the town judge exists, they meet the following conditions:
    1) The town judge trusts nobody;
    2) Everybody else (except the judge) trusts the judge;
    3) Exactly one person satisfies both conditions above.

Given an array trust, where trust[i] = [a, b] means person a trusts person b.

Return the label of the town judge if they exist, or -1 if no such person can be identified.

Examples:
Input: n = 2, trust = [[1, 2]]
Output: 2

Input: n = 3, trust = [[1, 3], [2, 3]]
Output: 3

В городе живёт n человек с номерами от 1 до n. Ходит слух, что один из них — судья города.

Если городской судья действительно существует, то он удовлетворяет следующим условиям:
    1) Судья никому не доверяет;
    2) Все остальные (кроме судьи) доверяют судье;
    3) Только один человек удовлетворяет одновременно обоим условиям.

Дан массив trust, где trust[i] = [a, b] означает, что человек a доверяет человеку b.

Верните номер судьи, если он существует и может быть определён, или -1, если такого человека нет.

Примеры:
Ввод: n = 2, trust = [[1, 2]]
Вывод: 2

Ввод: n = 3, trust = [[1, 3], [2, 3]]
Вывод: 3
'''

from typing import List

def find_judge(n: int, trust: List[List[int]]) -> int:
    if n == 1 and not trust:
        return 1

    trust_count = [0] * (n + 1)

    for a, b in trust:
        trust_count[a] -= 1
        trust_count[b] += 1

    for i in range(1, n + 1):
        if trust_count[i] == n - 1:
            return i

    return -1