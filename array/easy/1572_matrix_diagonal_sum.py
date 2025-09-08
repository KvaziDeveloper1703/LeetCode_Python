'''
Given a square matrix called matrix. 

Return the sum of the elements on the primary diagonal and the secondary diagonal.

If an element is part of both diagonals, it should only be counted once.

Examples:
Input: matrix = [   [1,2,3],
                    [4,5,6],
                    [7,8,9]
            ]

Output: 25

Input: matrix = [   [1,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1]
            ]

Output: 8

Дана квадратная матрица matrix.

Нужно вернуть сумму элементов, находящихся на главной диагонали и на побочной диагонали.

Если элемент находится одновременно на обеих диагоналях, то он должен учитываться только один раз.

Примеры:
Ввод: matrix = [[1,2,3],
                [4,5,6],
                [7,8,9]
        ]

Вывод: 25

Ввод: matrix = [[1,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1]
        ]

Вывод: 8
'''

from typing import List

def diagonal_sum(matrix: List[List[int]]) -> int:
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]
        total += matrix[i][n - 1 - i]
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]
    return total