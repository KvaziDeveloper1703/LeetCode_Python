'''
An integer array is called arithmetic if it has at least three elements and the difference between any two consecutive elements is the same.

Examples of arithmetic sequences:
    + [1, 3, 5, 7, 9]
    + [7, 7, 7, 7]
    + [3, -1, -5, -9]

Given an integer array numbers, return the number of all subarrays of nums that are arithmetic sequences.
A subarray is a contiguous portion of the array.

Examples:
Input: numbers = [1, 2, 3, 4]
Output: 3

Input: numbers = [1]
Output: 0

Массив целых чисел называется арифметическим, если он содержит как минимум три элемента и разность между любыми двумя последовательными элементами одинаковая.

Примеры арифметических последовательностей:
    + [1, 3, 5, 7, 9]
    + [7, 7, 7, 7]
    + [3, -1, -5, -9]

Дан массив целых чисел numbers. Нужно вернуть количество всех подмассивов, которые являются арифметическими последовательностями.
Подмассив — это непрерывная часть массива.

Примеры:
Вход: numbers = [1, 2, 3, 4]
Выход: 3

Вход: numbers = [1]
Выход: 0
'''

from typing import List

def number_of_arithmetic_slices(numbers: List[int]) -> int:
    if len(numbers) < 3:
        return 0

    total = 0
    count = 0
    
    for i in range(2, len(numbers)):
        if numbers[i] - numbers[i-1] == numbers[i-1] - numbers[i-2]:
            count += 1
            total += count
        else:
            count = 0

    return total