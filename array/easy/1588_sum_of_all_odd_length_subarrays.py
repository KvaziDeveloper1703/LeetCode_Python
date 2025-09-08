'''
Given an array of positive integers array.

Return the sum of all odd-length subarrays of array.

A subarray is a contiguous subsequence of the array.

Examples:
Input: array = [1,4,2,5,3]
Output: 58

Input: array = [1,2]
Output:3

Дан массив положительных целых чисел array.

Нужно вернуть сумму всех подмассивов нечётной длины.

Подмассив — это последовательность элементов массива, расположенных подряд.

Примеры:
Ввод: array = [1,4,2,5,3]
Вывод: 58

Ввод: array = [1,2]
Вывод: 3
'''

from typing import List

def sum_odd_length_subarrays(array: List[int]) -> int:
    n = len(array)
    total = 0
    for i in range(n):
        for j in range(i, n):
            length = j - i + 1
            if length % 2 == 1:
                total += sum(array[i:j+1])
    return total