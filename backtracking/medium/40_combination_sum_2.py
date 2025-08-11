'''
Given a list of integers candidates and a target integer target, find all unique combinations in candidates where the numbers sum to target.
Each number in candidates may only be used once in each combination. The solution set must not contain duplicate combinations.

Example:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],
         [1,2,5],
         [1,7],
         [2,6]
    ]

Дан список чисел candidates и целевое число target. Найдите все уникальные комбинации чисел из candidates, сумма которых равна target.
Каждое число из candidates можно использовать только один раз в каждой комбинации. Множество решений не должно содержать повторяющихся комбинаций.

Пример:
Ввод: candidates = [10,1,2,7,6,1,5], target = 8
Вывод: [[1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
    ]
'''

from typing import List

def combination_sum_2(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    candidates.sort()

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result