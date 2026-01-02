'''
You are given an integer array numbers.

We call an array good if it is a permutation of the array base[n].

The array base[n] is defined as: base[n] = [1, 2, ..., n − 1, n, n].

In other words, base[n] is an array of length n + 1 that:
    - contains each integer from 1 to n - 1 exactly once, and
    - contains the integer n exactly twice.

Return True if the given array numbers is a permutation of base[n] for some integer n. Otherwise, return False.

Examples:
Input: numbers = [2, 1, 3]
Output: False

Input: numbers = [1, 3, 3, 2]
Output: True

Вам дан массив целых чисел numbers.

Массив называется хорошим, если он является перестановкой массива base[n].

Массив base[n] определяется следующим образом: base[n] = [1, 2, ..., n − 1, n, n].

Иными словами, base[n] - это массив длины n + 1, который:
    - содержит все числа от 1 до n − 1 ровно по одному разу, и
    - содержит число n ровно два раза.

Необходимо вернуть True, если массив numbers является перестановкой base[n] для некоторого n. В противном случае вернуть False.

Примеры:
Ввод: numbers = [2, 1, 3]
Вывод: False

Ввод: numbers = [1, 3, 3, 2]
Вывод: True
'''

from typing import List
from collections import Counter

def is_good(numbers: List[int]) -> bool:
    n = max(numbers)

    if len(numbers) != n + 1:
        return False

    count = Counter(numbers)

    for i in range(1, n):
        if count[i] != 1:
            return False

    return count[n] == 2