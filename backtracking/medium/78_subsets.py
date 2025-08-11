'''
Given an integer array numbers of unique elements, return all possible subsets.
The solution set must not contain duplicate subsets. You can return the subsets in any order.

Examples:
Input: numbers = [1,2,3]  
Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

Input: numbers = [0]  
Output: [[], [0]]

Дан целочисленный массив numbers, содержащий уникальные элементы. Необходимо вернуть все возможные подмножества этого массива.
Результат не должен содержать повторяющихся подмножеств. Порядок возвращаемых подмножеств может быть любым.

Примеры:
Ввод: numbers = [1,2,3]  
Вывод: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

Ввод: numbers = [0]  
Вывод: [[], [0]]
'''

from typing import List

def subsets(numbers: List[int]) -> List[List[int]]:
    result = []

    def backtrack(start: int, path: List[int]):
        result.append(path[:])

        for i in range(start, len(numbers)):
            path.append(numbers[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result