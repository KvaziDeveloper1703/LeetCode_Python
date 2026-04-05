'''
Given an integer array numbers, find a contiguous subarray which has the largest sum, and return that sum.

Example:
Input: numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6

Дан целочисленный массив numbers. Найдите непрерывный подмассив с наибольшей суммой, и верните эту сумму.

Пример:
Ввод: numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Вывод: 6
'''

from typing import List

def max_sub_array(numbers: List[int]) -> int:
    max_sum = current_sum = numbers[0]

    for number in numbers[1:]:
        current_sum = max(number, current_sum + number)
        max_sum = max(max_sum, current_sum)

    return max_sum