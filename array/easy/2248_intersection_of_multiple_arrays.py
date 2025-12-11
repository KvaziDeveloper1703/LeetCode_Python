'''
You are given a 2D array numbers, where each numbers[i] is a non-empty list of distinct positive integers.

Your task is to return a list of all integers that appear in every array within numbers.
The result must be sorted in ascending order.

Вам дан двумерный массив numbers, где каждый numbers[i] - это непустой массив различных положительных целых чисел.

Нужно вернуть список всех чисел, которые встречаются во всех массивах из numbers.
Ответ должен быть отсортирован по возрастанию.
'''

from typing import List

def intersection(numbers: List[List[int]]) -> List[int]:
    common_elements = set(numbers[0])

    for current_list in numbers[1:]:
        common_elements = common_elements.intersection(current_list)

    return sorted(list(common_elements))