'''
You are given a 0-indexed integer array numbers.
    - An index i is part of a hill if its closest non-equal neighbors on both sides are smaller than numbers[i];
    - An index i is part of a valley if its closest non-equal neighbors on both sides are larger than numbers[i].

Adjacent indices with equal values (numbers[i] == numbers[j]) belong to the same hill or valley.

Return the number of hills and valleys in numbers.

Examples:
Input: numbers = [2,4,1,1,6,5]
Output: 3

Input: numbers = [6,6,5,5,4,1]
Output: 0

Дан массив целых чисел numbers, индексируемый с нуля.
    - Индекс i является частью холма, если ближайшие неравные элементы слева и справа оба меньше, чем numbers[i];
    - Индекс i является частью долины, если ближайшие неравные соседи слева и справа оба больше, чем numbers[i].

Если соседние индексы имеют одинаковые значения (numbers[i] == numbers[j]), они относятся к одному и тому же холму или долине.

Верните количество холмов и долин в массиве numbers.

Примеры:
Ввод: numbers = [2,4,1,1,6,5]
Вывод: 3

Ввод: numbers = [6,6,5,5,4,1]
Вывод: 0
'''

from typing import List

def count_hill_valley(numbers: List[int]) -> int:
    compressed_numbers = []

    for number in numbers:
        if not compressed_numbers or compressed_numbers[-1] != number:
            compressed_numbers.append(number)

    hill_valley_count = 0

    for index in range(1, len(compressed_numbers) - 1):
        left_value = compressed_numbers[index - 1]
        current_value = compressed_numbers[index]
        right_value = compressed_numbers[index + 1]

        if current_value > left_value and current_value > right_value:
            hill_valley_count += 1
        elif current_value < left_value and current_value < right_value:
            hill_valley_count += 1

    return hill_valley_count