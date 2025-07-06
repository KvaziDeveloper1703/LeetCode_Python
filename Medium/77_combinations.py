'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.
Note that the combinations are unordered, i.e., [1,2] and [2,1] are considered the same combination.

Example:
Input: n = 4, k = 2  
Output: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]

Даны два целых числа n и k. Необходимо вернуть все возможные комбинации из k чисел, выбранных из диапазона от 1 до n включительно.
Порядок элементов внутри комбинации не важен, то есть [1,2] и [2,1] считаются одной и той же комбинацией.
Ответ можно вернуть в любом порядке.

Пример:
Ввод: n = 4, k = 2  
Вывод: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
'''

from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    result = []

    def backtrack(start: int, combination: List[int]):

        if len(combination) == k:
            result.append(combination[:])
            return

        for i in range(start, n + 1):
            combination.append(i)
            backtrack(i + 1, combination)
            combination.pop()

    backtrack(1, [])
    return result