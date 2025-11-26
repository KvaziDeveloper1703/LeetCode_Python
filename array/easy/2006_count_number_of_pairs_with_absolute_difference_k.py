'''
You are given an integer array numbers and an integer k.

Return the number of pairs (i, j) such that:
    - i < j, and,
    - |numbers[i] - numbers[j]| == k.

The absolute value |x| is defined as:
    - x if x >= 0;
    - -x if x < 0.

Examples:
Input: numbers = [1,2,2,1], k = 1
Output: 4

Input: numbers = [1,3], k = 3
Output: 0

Дан массив целых чисел numbers и число k.

Нужно вернуть количество пар (i, j), для которых:
    - i < j, и,
    - |numbers[i] - numbers[j]| == k.

Абсолютное значение |x| определяется так:
    - x, если x >= 0;
    - -x, если x < 0.

Примеры:
Ввод: numbers = [1,2,2,1], k = 1
Вывод: 4

Ввод: numbers = [1,3], k = 3
Вывод: 0
'''

from typing import List

def count_k_difference(numbers: List[int], k: int) -> int:
    pair_count = 0
    numbers_length = len(numbers)

    for left_index in range(numbers_length):
        for right_index in range(left_index + 1, numbers_length):
            if abs(numbers[left_index] - numbers[right_index]) == k:
                pair_count += 1

    return pair_count