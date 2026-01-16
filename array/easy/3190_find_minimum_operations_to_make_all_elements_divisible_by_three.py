'''
You are given an integer array numbers.
In one operation, you can add 1 or subtract 1 from any element of the array.
Return the minimum number of operations needed to make every element of numbers divisible by 3.

Examples:
Input: numbers = [1, 2, 3, 4]
Output: 3

Input: numbers = [3, 6, 9]
Output: 0

Дан целочисленный массив numbers.
За одну операцию можно увеличить или уменьшить на 1 любой элемент массива.
Нужно вернуть минимальное количество операций, чтобы все элементы массива numbers стали делиться на 3 без остатка.

Примеры:
Ввод: numbers = [1, 2, 3, 4]
Вывод: 3

Ввод: numbers = [3, 6, 9]
Вывод: 0
'''

from typing import List

def minimum_operations(numbers: List[int]) -> int:
    operations_count = 0

    for value in numbers:
        if value % 3 != 0:
            operations_count += 1

    return operations_count