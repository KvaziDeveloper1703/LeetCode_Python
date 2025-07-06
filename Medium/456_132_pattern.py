'''
Given an array of n integers numbers, a 132 pattern is a subsequence of three elements numbers[i], numbers[j], and numbers[k] such that:
    + i < j < k, and
    + numbers[i] < numbers[k] < numbers[j]

Return true if there is at least one such 132 pattern in the array. Otherwise, return false.

Examples:
Input: numbers = [1, 2, 3, 4]
Output: false

Input: numbers = [3, 1, 4, 2]
Output: true

Дан массив из n целых чисел numbers.
Шаблон 132 — это подпоследовательность из трёх элементов numbers[i], numbers[j] и numbers[k], такая что:
    + i < j < k, и
    + numbers[i] < numbers[k] < numbers[j]

Верните true, если в массиве существует хотя бы один шаблон 132. В противном случае верните false.

Примеры:
Ввод: numbers = [1, 2, 3, 4]
Вывод: false

Ввод: numbers = [3, 1, 4, 2]
Вывод: true
'''

from typing import List

def find_132_pattern(numbers: List[int]) -> bool:
    if len(numbers) < 3:
        return False

    stack = []
    third = float('-inf')

    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] < third:
            return True

        while stack and numbers[i] > stack[-1]:
            third = stack.pop()
        stack.append(numbers[i])

    return False