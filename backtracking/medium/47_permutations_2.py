'''
Given a collection of numbers, that might contain duplicates, return all possible unique permutations in any order.

Example:
Input: numbers = [1, 1, 2]
Output: [   [1, 1, 2],
            [1, 2, 1],
            [2, 1, 1]
    ]

Дан массив numbers, который может содержать повторяющиеся числа. Необходимо вернуть все возможные уникальные перестановки элементов массива. Ответ можно вернуть в любом порядке.

Пример:
Ввод: numbers = [1, 1, 2]
Вывод: [[1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]
'''

from typing import List

def permute_unique(numbers: List[int]) -> List[List[int]]:
    result = []
    numbers.sort()

    used = [False] * len(numbers)

    def backtrack(path):
        if len(path) == len(numbers):
            result.append(path[:])
            return

        for i in range(len(numbers)):
            if used[i]:
                continue
            if i > 0 and numbers[i] == numbers[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(numbers[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result