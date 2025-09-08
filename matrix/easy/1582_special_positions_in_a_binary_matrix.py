'''
Given an m x n binary matrix called matrix.

Return the number of special positions in the matrix.

A position (i, j) is called special if:
    + matrix[i][j] == 1, and
    + all other elements in row i and column j are 0.

Examples:
Input: matrix = [   [1,0,0],
                    [0,0,1],
                    [1,0,0]
            ]
Output: 1

Input: matrix = [   [1,0,0],
                    [0,1,0],
                    [0,0,1]
            ]
Output: 3

Дана бинарная матрица mat размера m x n.

Нужно вернуть количество особых позиций в матрице.

Позиция (i, j) называется особой, если:
    + matrix[i][j] == 1, и
    + все остальные элементы в строке i и в столбце j равны 0.

Примеры:
Ввод: matrix = [[1,0,0],
                [0,0,1],
                [1,0,0]
        ]
Вывод: 1

Ввод: matrix = [[1,0,0],
                [0,1,0],
                [0,0,1]
        ]
Вывод: 3
'''

from typing import List

def number_special(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    row_sum = [sum(row) for row in matrix]
    column_sum = [sum(matrix[i][j] for i in range(m)) for j in range(n)]
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and row_sum[i] == 1 and column_sum[j] == 1:
                count += 1
    return count