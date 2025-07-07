'''
Given an array numbers containing n distinct numbers in the range [0, n].
Return the only number in the range that is missing from the array.

Examples:
Input: numbers = [3, 0, 1]
Output: 2

Input: numbers = [0, 1]
Output: 2

Дан массив numbers, содержащий n уникальных чисел в диапазоне от 0 до n включительно. 
Верните единственное число, которое отсутствует в этом диапазоне, но должно быть в массиве.

Примеры:
Ввод: numbers = [3, 0, 1]
Вывод: 2

Ввод: numbers = [0, 1]
Вывод: 2
'''

from typing import List

def missing_number(numbers: List[int]) -> int:
    n = len(numbers)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum