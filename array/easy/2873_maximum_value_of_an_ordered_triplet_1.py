'''
You are given a 0-indexed integer array numbers.

Return the maximum value among all triplets of indices (i, j, k) such that i < j < k.

If the value of every such triplet is negative, return 0.

The value of a triplet (i, j, k) is defined as: (numbers[i] - numbers[j]) * numbers[k].

Examples:
Input: numbers = [12,6,1,2,7]
Output: 77

Input: numbers = [1,10,3,4,19]
Output: 133

Вам дан 0-индексированный массив целых чисел numbers.

Найдите максимальное значение среди всех троек индексов (i, j, k), таких что i < j < k.

Если значение любой такой тройки отрицательное, верните 0.

Значение тройки индексов (i, j, k) определяется формулой: (numbers[i] - numbers[j]) * numbers[k].

Примеры:
Ввод: numbers = [12,6,1,2,7]
Вывод: 77

Ввод: numbers = [1,10,3,4,19]
Вывод: 133
'''

from typing import List

def maximum_triplet_value(numbers: List[int]) -> int:
    maximum_left_value = numbers[0]
    maximum_difference = 0
    maximum_triplet_value = 0

    for index in range(1, len(numbers)):
        current_value = numbers[index]
        maximum_triplet_value = max(maximum_triplet_value, maximum_difference * current_value)
        maximum_difference = max(maximum_difference, maximum_left_value - current_value)
        maximum_left_value = max(maximum_left_value, current_value)

    return maximum_triplet_value