'''
Given an array of integers numbers, where half of the integers are even and the other half are odd.

Rearrange the array so that:
    + Every number at an even index is even, and
    + Every number at an odd index is odd.

Return any array that satisfies this condition.

Examples:
Input: numbers = [4, 2, 5, 7]
Output: [4, 5, 2, 7]

Input: numbers = [2, 3]
Output: [2, 3]

Дан массив целых чисел numbers, в котором половина чисел — чётные, а другая половина — нечётные.

Необходимо переставить элементы так, чтобы:
    + На чётных индексах находились чётные числа,
    + На нечётных индексах находились нечётные числа.

Верните любой массив, удовлетворяющий этим условиям.

Примеры:
Ввод: numbers = [4, 2, 5, 7]
Вывод: [4, 5, 2, 7]

Ввод: numbers = [2, 3]
Вывод: [2, 3]
'''

from typing import List

def sort_array_by_parity(numbers: List[int]) -> List[int]:
    even_numbers = [number for number in numbers if number % 2 == 0]
    odd_numbers = [number for number in numbers if number % 2 != 0]

    result = [0] * len(numbers)
    even_index = 0
    odd_index = 1

    for number in even_numbers:
        result[even_index] = number
        even_index += 2

    for number in odd_numbers:
        result[odd_index] = number
        odd_index += 2

    return result