'''
You are given a 0-indexed integer array numbers. Rearrange its elements according to the following rules:
    - Sort the values at odd indices of numbers in non-increasing order;
    - Sort the values at even indices of numbers in non-decreasing order.

Return the array after applying both rearrangements.

Examples:
Input: numbers = [4, 1, 2, 3]
Output: [2, 3, 4, 1]

Input: numbers = [2, 1]
Output: [2, 1]

Дан целочисленный массив numbers с индексами от 0. Необходимо переставить его элементы по следующим правилам:
    - Отсортировать элементы на нечётных индексах в невозрастающем порядке;
    - Отсортировать элементы на чётных индексах в неубывающем порядке.

Верните массив после выполнения обеих сортировок.

Примеры:
Ввод: numbers = [4, 1, 2, 3]
Вывод: [2, 3, 4, 1]

Ввод: numbers = [2, 1]
Вывод: [2, 1]
'''

from typing import List

def sort_even_odd(numbers: List[int]) -> List[int]:
    even_values = sorted(numbers[::2])
    odd_values = sorted(numbers[1::2], reverse=True)

    result = []
    even_index_pointer = 0
    odd_index_pointer = 0

    for index in range(len(numbers)):
        if index % 2 == 0:
            result.append(even_values[even_index_pointer])
            even_index_pointer += 1
        else:
            result.append(odd_values[odd_index_pointer])
            odd_index_pointer += 1

    return result