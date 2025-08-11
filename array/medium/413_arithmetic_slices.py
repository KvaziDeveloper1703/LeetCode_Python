'''
An integer array is called arithmetic if it has at least three elements and the difference between any two consecutive elements is the same.

Given an integer array numbers.

Return the number of all subarrays of nums that are arithmetic sequences.

Examples:
Input: numbers = [1, 2, 3, 4]
Output: 3

Input: numbers = [1]
Output: 0

Массив целых чисел называется арифметическим, если он содержит как минимум три элемента и разность между любыми двумя последовательными элементами одинаковая.

Дан массив целых чисел numbers. 

Нужно вернуть количество всех подмассивов, которые являются арифметическими последовательностями.

Примеры:
Ввод: numbers = [1, 2, 3, 4]
Вывод: 3

Ввод: numbers = [1]
Вывод: 0
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