'''
Given an integer n, return any array of n unique integers such that their sum is 0. There can be multiple valid answers.

Examples:
Input: n = 5
Output: [-7, -1, 1, 3, 4]

Input: n = 3
Output: [-1, 0, 1]

Дано целое число n. Необходимо вернуть любой массив из n уникальных целых чисел, сумма которых равна 0. Допускается несколько корректных решений.

Примеры:
Ввод: n = 5
Вывод: [-7, -1, 1, 3, 4]

Ввод: n = 3
Вывод: [-1, 0, 1]
'''

from typing import List

def sum_zero(n: int) -> List[int]:
    result = []
    for i in range(1, n // 2 + 1):
        result.extend([-i, i])
    if n % 2 != 0:
        result.append(0)
    return result