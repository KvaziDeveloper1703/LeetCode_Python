'''
You are given an array of integers numbers.
Return the length of the longest subarray of numbers that is either strictly increasing or strictly decreasing.

A subarray must consist of consecutive elements from the array.

Examples:
Input: numbers = [1,4,3,3,2]
Output: 2

Input: numbers = [3,3,3,3]
Output: 1

Дан массив целых чисел numbers.
Нужно вернуть длину самого длинного подмассива, который является либо строго возрастающим, либо строго убывающим.

Подмассив должен состоять из соседних элементов массива.

Примеры:
Ввод: numbers = [1,4,3,3,2]
Вывод: 2

Ввод: numbers = [3,3,3,3]
Вывод: 1
'''

from typing import List

def longest_monotonic_subarray(numbers: List[int]) -> int:
    array_length = len(numbers)

    longest_length = 1
    current_increasing_length = 1
    current_decreasing_length = 1

    for index in range(1, array_length):
        if numbers[index] > numbers[index - 1]:
            current_increasing_length += 1
            current_decreasing_length = 1
        elif numbers[index] < numbers[index - 1]:
            current_decreasing_length += 1
            current_increasing_length = 1
        else:
            current_increasing_length = 1
            current_decreasing_length = 1

        longest_length = max(longest_length, current_increasing_length, current_decreasing_length)

    return longest_length