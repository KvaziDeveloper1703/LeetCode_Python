'''
You are given an array of positive integers numbers.
Your task is to return the maximum possible sum of a strictly increasing subarray in numbers.

A subarray is a contiguous sequence of elements within an array.

Examples:
Input: numbers = [10, 20, 30, 5, 10, 50]
Output: 65

Input: numbers = [10, 20, 30, 40, 50]
Output: 150

Дан массив положительных целых чисел numbers.
Нужно вернуть максимально возможную сумму строго возрастающего подмассива в numbers.

Подмассив - это непрерывная последовательность элементов массива.

Примеры:
Ввод: numbers = [10, 20, 30, 5, 10, 50]
Вывод: 65

Ввод: numbers = [10, 20, 30, 40, 50]
Вывод: 150
'''

from typing import List

def max_ascending_sum(numbers: List[int]) -> int:
    current_subarray_sum = numbers[0]
    maximum_subarray_sum = numbers[0]

    for index in range(1, len(numbers)):
        if numbers[index] > numbers[index - 1]:
            current_subarray_sum += numbers[index]
        else:
            current_subarray_sum = numbers[index]

        if current_subarray_sum > maximum_subarray_sum:
            maximum_subarray_sum = current_subarray_sum

    return maximum_subarray_sum