'''
Given an array array of positive integers, sorted in strictly increasing order, and an integer k.

Return the k-th missing positive integer that does not appear in the array.

Examples:
Input: array = [2,3,4,7,11], k = 5
Output: 9

Input: array = [1,2,3,4], k = 2
Output: 6

Вам дан массив array, состоящий из положительных целых чисел, отсортированных в строго возрастающем порядке, и число k.

Нужно вернуть k-й отсутствующий положительный элемент, которого нет в массиве.

Примеры:
Ввод: array = [2,3,4,7,11], k = 5
Вывод: 9

Ввод: array = [1,2,3,4], k = 2
Вывод: 6
'''

from typing import List

def find_kth_positive(array: List[int], k: int) -> int:
    missing_count = 0
    current_number = 1

    array_index = 0
    array_length = len(array)
    while True:
        if array_index < array_length and array[array_index] == current_number:
            array_index += 1
        else:
            missing_count += 1
            if missing_count == k:
                return current_number
        current_number += 1