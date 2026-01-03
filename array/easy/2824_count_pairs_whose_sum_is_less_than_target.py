'''
You are given a 0-indexed integer array numbers of length n and an integer target.

Your task is to count the number of pairs of indices (i, j) such that:
    - 0 ≤ i < j < n;
    - numbers[i] + numbers[j] < target.

Return the total number of such pairs.

Examples:
Input: numbers = [-1, 1, 2, 3, 1], target = 2
Output: 3

Input: numbers = [-6, 2, 5, -2, -7, -1, 3], target = -2
Output: 10

Дан 0-индексированный массив целых чисел numbers длины n и целое число target.

Необходимо определить количество пар индексов (i, j), для которых выполняются условия:
    - 0 ≤ i < j < n;
    - numbers[i] + numbers[j] < target.

Верните количество таких пар.

Примеры:
Ввод: numbers = [-1, 1, 2, 3, 1], target = 2
Вывод: 3

Ввод: numbers = [-6, 2, 5, -2, -7, -1, 3], target = -2
Вывод: 10
'''

from typing import List

def count_pairs(numbers: List[int], target: int) -> int:
    numbers.sort()
    left = 0
    right = len(numbers) - 1
    count = 0

    while left < right:
        if numbers[left] + numbers[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1

    return count