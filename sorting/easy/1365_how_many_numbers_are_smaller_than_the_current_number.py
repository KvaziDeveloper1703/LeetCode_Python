'''
Given an array numbers. For each element numbers[i], determine how many numbers in the array are smaller than it.
Formally, for each numbers[i], count the number of indices j such that:
    + j!=i;
    + numbers[j]<numbers[i].

Return the result as an array.

Examples:
Input: numbers = [8,1,2,2,3]
Output: [4,0,1,1,3]

Input: numbers = [6,5,4,8]
Output: [2,1,0,3]

Дан массив numbers. Для каждого элемента numbers[i] определите, сколько чисел в массиве меньше его.
Формально, для каждого numbers[i] нужно посчитать количество индексов j, таких что:
    + j!=i;
    + numbers[j]<numbers[i].

Верните результат в виде массива.

Примеры:
Ввод: numbers = [8,1,2,2,3]
Вывод: [4,0,1,1,3]

Ввод: numbers = [6,5,4,8]
Вывод: [2,1,0,3]
'''

from typing import List

def smaller_numbers_than_current(numbers: List[int]) -> List[int]:
    sorted_numbers = sorted(numbers)
    first_index = {}
    for i, value in enumerate(sorted_numbers):
        if value not in first_index:
            first_index[value] = i
    return [first_index[x] for x in numbers]