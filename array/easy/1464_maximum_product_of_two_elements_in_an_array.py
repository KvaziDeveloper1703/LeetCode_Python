'''
You are given an array of integers nums. Choose two different indices i and j.
Return the maximum possible value of the expression: (nums[i] - 1) * (nums[j] - 1).

Examples:
Input: nums = [3, 4, 5, 2]
Output: 12

Input: nums = [1, 5, 4, 5]
Output: 16

Дан массив целых чисел nums. Необходимо выбрать два разных индекса i и j.
Нужно вернуть максимальное значение выражения: (nums[i] - 1) * (nums[j] - 1).

Примеры:
Ввод: nums = [3, 4, 5, 2]
Вывод: 12

Ввод: nums = [1, 5, 4, 5]
Вывод: 16
'''

from typing import List

def max_product(nums: List[int]) -> int:
    first_max = 0
    second_max = 0

    for number in nums:
        if number > first_max:
            second_max = first_max
            first_max = number
        elif number > second_max:
            second_max = number

    return (first_max - 1) * (second_max - 1)