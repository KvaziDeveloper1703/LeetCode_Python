'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Examples:
Input: n = 2
Output: [0,1,1]

Input: n = 5
Output: [0,1,1,2,1,2]

Дан целое число n. Необходимо вернуть массив ans длины n + 1, такой что для каждого i (0 <= i <= n), ans[i] — это количество единиц в двоичном представлении числа i.

Примеры:
Ввод: n = 2
Вывод: [0,1,1]

Ввод: n = 5
Вывод: [0,1,1,2,1,2]
'''

from typing import List

class Solution:
    def count_bits(self, n: int) -> List[int]:
        bit_counts = [0] * (n + 1)
        for i in range(1, n + 1):
            bit_counts[i] = bit_counts[i >> 1] + (i & 1)
        return bit_counts