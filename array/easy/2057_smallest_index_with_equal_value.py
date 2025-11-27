'''
You are given a 0-indexed integer array numbers.

Return the smallest index i such that: i mod 10 = numbers[i]

If no such index exists, return -1.

Here, x mod y means the remainder when x is divided by y.

Examples:
Input: numbers = [0,1,2]
Output: 0

Input: numbers = [4,3,2,1]
Output: 2

Дан целочисленный массив numbers с индексами, начинающимися с 0.

Нужно вернуть наименьший индекс i, для которого выполняется: i mod 10 = numbers[i]

Если такого индекса нет, вернуть -1.

Здесь x mod y - это остаток от деления x на y.

Примеры:
Ввод: numbers = [0,1,2]
Вывод: 0

Ввод: numbers = [4,3,2,1]
Вывод: 2
'''

from typing import List

def smallest_equal(numbers: List[int]) -> int:
    for index in range(len(numbers)):
        if index % 10 == numbers[index]:
            return index
    return -1