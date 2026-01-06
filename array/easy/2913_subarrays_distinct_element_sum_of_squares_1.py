'''
You are given a 0-indexed integer array numbers.

The distinct count of a subarray numbers[i..j] is defined as follows: let numbers[i..j] be a subarray of numbers consisting of all elements with indices from i to j, where 0 ≤ i ≤ j < numbers.length. The number of distinct values in numbers[i..j] is called the distinct count of that subarray.

Your task is to return the sum of the squares of the distinct counts of all subarrays of numbers.

A subarray is a contiguous non-empty sequence of elements within an array.

Examples:
Input:numbers = [1, 2, 1]
Output: 15

Input: numbers = [1, 1]
Output: 3

Дан целочисленный массив numbers с индексацией с нуля.

Количество различных элементов подмассива numbers[i..j] определяется следующим образом: пусть numbers[i..j] — это подмассив массива numbers, включающий все элементы с индексами от i до j, где 0 ≤ i ≤ j < numbers.length. Тогда число различных значений в numbers[i..j] называется количеством различных элементов этого подмассива.

Требуется найти сумму квадратов количеств различных элементов для всех подмассивов массива numbers.

Подмассив - это непрерывная непустая последовательность элементов массива.

Примеры:
Ввод: numbers = [1, 2, 1]
Вывод: 15

Ввод: numbers = [1, 1]
Вывод: 3
'''

from typing import List

def sum_сounts(numbers: List[int]) -> int:
    array_length = len(numbers)
    total_sum = 0

    for start_index in range(array_length):
        distinct_values = set()

        for end_index in range(start_index, array_length):
            distinct_values.add(numbers[end_index])
            distinct_count = len(distinct_values)
            total_sum += distinct_count * distinct_count

    return total_sum