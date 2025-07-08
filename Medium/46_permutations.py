'''
Given an array numbers of distinct integers.

Return all possible permutations of the array. You can return the answer in any order.

Example:
Input: numbers = [1, 2, 3]
Output: [   [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
    ]

Дан массив numbers, содержащий уникальные целые числа.

Необходимо вернуть все возможные перестановки этих чисел. Ответ можно вернуть в любом порядке.

Пример:
Ввод: numbers = [1, 2, 3]
Вывод: [[1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
'''

from typing import List

def permute(numbers: List[int]) -> List[List[int]]:
    result = []

    def backtrack(start=0):
        if start == len(numbers):
            result.append(numbers[:])
            return

        for i in range(start, len(numbers)):
            numbers[start], numbers[i] = numbers[i], numbers[start]
            backtrack(start + 1)
            numbers[start], numbers[i] = numbers[i], numbers[start]

    backtrack()
    return result