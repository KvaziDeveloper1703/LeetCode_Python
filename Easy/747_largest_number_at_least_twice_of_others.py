'''
Given an integer array numbers, in which the largest integer is unique.

Determine whether the largest element in the array is at least twice as large as every other number in the array.
    + If it is, return the index of the largest element;
    + If it is not, return -1.

Examples:
Input: numbers = [3, 6, 1, 0]
Output: 1

Input: numbers = [1, 2, 3, 4]
Output: -1

Дан массив целых чисел numbers, в котором наибольший элемент уникален.

Ваша задача — определить, является ли наибольший элемент массива как минимум в два раза больше каждого из остальных чисел.
    + Если это так, верните индекс наибольшего элемента;
    + Если не так — верните -1.

Примеры:
Ввод: numbers = [3, 6, 1, 0]
Вывод: 1

Ввод: numbers = [1, 2, 3, 4]
Вывод: -1
'''

from typing import List

def dominant_index(numbers: List[int]) -> int:
    max_value = max(numbers)
    max_index = numbers.index(max_value)

    for i, number in enumerate(numbers):
        if i != max_index and max_value < 2 * number:
            return -1

        return max_index