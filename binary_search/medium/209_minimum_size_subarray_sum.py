'''
You are given an array of positive integers numbers and a positive integer target.

Find the minimal length of a contiguous subarray of which the sum is greater than or equal to target. If no such subarray exists, return 0.

Examples:
Input: target = 7, numbers = [2,3,1,2,4,3]
Output: 2

Input: target = 4, numbers = [1,4,4]
Output: 1

Дан массив положительных целых чисел numbers и положительное целое число target.

Найдите минимальную длину непрерывного подмассива, сумма элементов которого больше либо равна target. Если такого подмассива не существует, верните 0.

Примеры:
Ввод: target = 7, numbers = [2, 3, 1, 2, 4, 3]
Вывод: 2

Ввод: target = 4, numbers = [1, 4, 4]
Вывод: 1
'''

from typing import List

def minimum_sub_array_length(target: int, numbers: List[int]) -> int:
    left = 0
    total = 0
    min_length = float('inf')

    for right in range(len(numbers)):
        total += numbers[right]

        while total >= target:
            min_length = min(min_length, right - left + 1)
            total -= numbers[left]
            left += 1

    return 0 if min_length == float('inf') else min_length