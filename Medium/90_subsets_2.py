'''
Given an integer array numbers that may contain duplicates, return all possible subsets.
    + The solution set must not contain duplicate subsets.
    + Return the solution in any order.

Examples:
Input: numbers = [1, 2, 2]
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

Input: numbers = [0]
Output: [[], [0]]

Дан массив целых чисел numbers, который может содержать дубликаты. Верните все возможные подмножества этого массива.
    + В результирующем наборе не должно быть одинаковых подмножеств.
    + Порядок вывода может быть любым.

Примеры:
Ввод: numbers = [1, 2, 2]
Вывод: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

Ввод: numbers = [0]
Вывод: [[], [0]]
'''

from typing import List

def subsetsWithDup(numbers: List[int]) -> List[List[int]]:
    result = []
    numbers.sort()

    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(numbers)):
            if i > start and numbers[i] == numbers[i - 1]:
                continue
            path.append(numbers[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result