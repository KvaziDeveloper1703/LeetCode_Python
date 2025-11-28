'''
You are given a 0-indexed integer array numbers and an integer target.

A target index is an index i such that numbers[i] == target.

Your task is to return a list of all target indices after sorting numbers in non-decreasing order.
If the target does not appear in the array, return an empty list.
The returned list must be sorted in increasing order.

Examples:
Input: numbers = [1,2,5,2,3], target = 2
Output: [1,2]

Input: numbers = [1,2,5,2,3], target = 3
Output: [3]

Вам дан целочисленный массив numbers с индексами, начинающимися с 0, и число target.

Целевой индекс - это индекс i, для которого выполняется условие numbers[i] == target.

Нужно вернуть список всех целевых индексов после сортировки массива numbers по неубыванию.
Если целевое значение не встречается в массиве, верните пустой список.
Возвращаемый список должен быть отсортирован по возрастанию.

Примеры:
Ввод: numbers = [1,2,5,2,3], target = 2
Вывод: [1,2]

Ввод: numbers = [1,2,5,2,3], target = 3
Вывод: [3]
'''

from typing import List

def target_indices(numbers: List[int], target: int) -> List[int]:
    numbers.sort()
    target_indices = []
    for index, value in enumerate(numbers):
        if value == target:
            target_indices.append(index)
    return target_indices