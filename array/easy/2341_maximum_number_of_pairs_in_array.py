'''
You are given a 0-indexed integer array numbers.

In one operation, you may perform the following:
    - Choose two equal integers from numbers;
    - Remove both integers from the array, forming one pair.

You can repeat this operation as many times as possible.

Return a 0-indexed integer array answer of size 2, where:
    - answer[0] is the number of pairs formed,
    - answer[1] is the number of remaining integers in numbers after all possible operations.

Examples:
Input: numbers = [1, 3, 2, 1, 3, 2, 2]
Output: [3, 1]

Input: numbers = [1, 1]
Output: [1, 0]

Дан 0-индексированный целочисленный массив numbers.

За одну операцию можно:
    - выбрать два одинаковых числа из массива numbers,
    - удалить их из массива, образовав одну пару.

Эту операцию можно выполнять максимально возможное число раз.

Верните 0-индексированный массив answer длины 2, где:
    - answer[0] - количество образованных пар,
    - answer[1] - количество оставшихся чисел в массиве numbers после выполнения всех возможных операций.

Примеры:
Ввод: numbers = [1, 3, 2, 1, 3, 2, 2]
Вывод: [3, 1]

Ввод: numbers = [1, 1]
Вывод: [1, 0]
'''

from typing import List
from collections import Counter

def number_of_pairs(numbers: List[int]) -> List[int]:
    frequency_counter = Counter(numbers)

    pair_count = 0
    leftover_count = 0

    for occurrences in frequency_counter.values():
        pair_count += occurrences // 2
        leftover_count += occurrences % 2

    return [pair_count, leftover_count]