'''
Given an integer array numbers and an integer k.
You may perform at most one operation on each element in the array. In a single operation, you can add or subtract any integer x to/from numbers[i], where x is in the range [-k, k]. That is, you can change numbers[i] to any value in the range [numbers[i] - k, numbers[i] + k].
The score of the array is defined as the difference between the maximum and minimum values in the array.

Return the minimum possible score you can achieve after performing these operations.

Examples:
Input: numbers = [1], k = 0
Output: 0

Input: numbers = [0, 10], k = 2
Output: 6

Дан массив целых чисел numbers и число k.
Вы можете выполнить не более одной операции для каждого элемента массива. В одной операции разрешено прибавить или вычесть любое целое число x из диапазона [-k, k], то есть заменить numbers[i] на значение из диапазона [numbers[i] - k, numbers[i] + k].
Оценка массива — это разность между его максимальным и минимальным элементом.

Найдите минимально возможную оценку после применения описанных операций.

Примеры:
Ввод: numbers = [1], k = 0
Вывод: 0

Ввод: numbers = [0, 10], k = 2
Вывод: 6
'''

from typing import List

def smallest_range(numbers: List[int], value: int) -> int:
    max_value = max(numbers)
    min_value = min(numbers)
    reduced_range = (max_value - min_value) - 2 * value
    return max(0, reduced_range)