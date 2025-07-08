'''
The set [1, 2, 3, ..., n] has exactly n! unique permutations.
By listing and ordering all of the permutations in lexicographical order, we can assign a number to each permutation from 1 to n!.

Given two integers n and k, return the k-th permutation sequence of the numbers 1 to n.

Examples:
Input: n = 3, k = 3
Output: "213"

Input: n = 4, k = 9
Output: "2314"

Множество [1, 2, 3, ..., n] содержит ровно n! уникальных перестановок.
Если перечислить все перестановки в лексикографическом порядке и пронумеровать их от 1 до n!, то каждая перестановка будет иметь уникальный номер.

По заданным числам n и k верните k-ю по счёту перестановку чисел от 1 до n.

Примеры:
Ввод: n = 3, k = 3
Вывод: "213"

Ввод: n = 4, k = 9
Вывод: "2314"
'''

from math import factorial

def get_permutation(n: int, k: int) -> str:
    digits = [str(i) for i in range(1, n + 1)]
    permutation_result = []
    remaining_k = k - 1

    for position in range(n):
        group_size = factorial(n - 1 - position)
        index = remaining_k // group_size
        remaining_k %= group_size
        permutation_result.append(digits.pop(index))

    return ''.join(permutation_result)