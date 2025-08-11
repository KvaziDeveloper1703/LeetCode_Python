'''
You are given an m x n matrix M initialized with all 0s, and an array ops where each operation is represented as ops[i] = [a, b].
For each operation [a, b], you should increment by 1 every element M[x][y] such that 0 <= x < a and 0 <= y < b.

After performing all operations, return the count of the maximum integers in the matrix M.

Examples:
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4

Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],
                            [3,3],[3,3],[3,3],[2,2],[3,3],
                            [3,3],[3,3]]
Output: 4

Дан m x n матрица M, инициализированная нулями, а также массив операций ops, где каждая операция представлена в виде ops[i] = [a, b].
Для каждой операции [a, b] нужно увеличить на 1 все элементы матрицы M[x][y], для которых выполняется условие 0 <= x < a и 0 <= y < b.

После выполнения всех операций необходимо вернуть количество элементов матрицы, имеющих максимальное значение.

Примеры:
Ввод: m = 3, n = 3, ops = [[2,2],[3,3]]
Вывод: 4

Ввод:m = 3, n = 3, ops = [  [2,2],[3,3],[3,3],[3,3],[2,2],
                            [3,3],[3,3],[3,3],[2,2],[3,3],
                            [3,3],[3,3]]
Вывод: 4
'''

from typing import List

def max_count(m: int, n: int, ops: List[List[int]]) -> int:
    if not ops:
        return m * n

    min_a = m
    min_b = n

    for a, b in ops:
        min_a = min(min_a, a)
        min_b = min(min_b, b)

    return min_a * min_b