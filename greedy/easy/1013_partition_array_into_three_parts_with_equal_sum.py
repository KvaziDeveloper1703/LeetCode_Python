'''
Given an array of integers my_array.

Formally, you must find two indices i and j such that:
    + i + 1 < j,
    + The sum of the first part my_array[0] + ... + my_array[i] equals the sum of the second part my_array[i + 1] + ... + my_array[j - 1],
    + And this equals the sum of the third part my_array[j] + ... + my_array[my_array.length - 1].

Return True if such a partition exists, otherwise return False.

Examples:
Input: my_array = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
Output: True

Input: my_array = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
Output: False

Вам дан массив целых чисел my_array.

Нужно найти такие индексы i и j, что:
    + i + 1 < j,
    + Сумма первой части my_array[0] + ... + my_array[i] равна сумме второй части my_array[i + 1] + ... + my_array[j - 1],
    + И эта сумма равна сумме третьей части my_array[j] + ... + my_array[my_array.length - 1].

Верните True, если такое разбиение существует, иначе верните False.

Примеры:
Ввод: my_array = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
Вывод: True

Ввод: my_array = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
Вывод: False
'''

from typing import List

def can_three_parts_equal_sum(my_array: List[int]) -> bool:
    total = sum(my_array)

    if total % 3 != 0:
        return False

    target = total // 3
    current_sum = 0
    parts = 0

    for number in my_array:
        current_sum += number
        if current_sum == target:
            parts += 1
            current_sum = 0
        if parts == 3:
            return True

    return False