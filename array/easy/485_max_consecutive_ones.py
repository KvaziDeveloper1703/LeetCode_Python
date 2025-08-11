'''
Given a binary array numbers, return the maximum number of consecutive 1s in the array.

Examples:
Input: numbers = [1,1,0,1,1,1]
Output: 3

Input: numbers = [1,0,1,1,0,1]
Output: 2

Дан бинарный массив numbers, содержащий только 0 и 1. Верните максимальное количество подряд идущих 1 в массиве.

Примеры:
Ввод: numbers = [1,1,0,1,1,1]
Вывод: 3

Ввод: numbers = [1,0,1,1,0,1]
Вывод: 2
'''

from typing import List

def find_max_consecutive_ones(numbers: List[int]) -> int:
    max_count = 0
    count = 0

    for number in numbers:
        if number == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    return max_count