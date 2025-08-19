'''
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of integers my_array, return True if the array can be rearranged to form an arithmetic progression. Otherwise, return False.

Examples:
Input: my_array = [3, 5, 1]
Output: True

Input: my_array = [1, 2, 4]
Output: False

Последовательность чисел называется арифметической прогрессией, если разность между любыми двумя соседними элементами одинакова.

Дан массив целых чисел my_array. Верните True, если элементы массива можно переставить так, чтобы получилась арифметическая прогрессия. В противном случае верните False.

Примеры:
Ввод: my_array = [3, 5, 1]
Вывод: True

Ввод: my_array = [1, 2, 4]
Вывод: False
'''

from typing import List

def can_make_arithmetic_progression(my_array: List[int]) -> bool:
    n = len(my_array)
    if n <= 2:
        return True

    my_array.sort()
    d = my_array[1] - my_array[0]

    for i in range(2, n):
        if my_array[i] - my_array[i - 1] != d:
            return False
    return True