'''
Given an m x n matrix, return True if the matrix is Toeplitz, otherwise return False.

A matrix is called Toeplitz if every diagonal from top-left to bottom-right contains the same elements.

Examples:
Input: matrix = [   [1,2,3,4],
                    [5,1,2,3],
                    [9,5,1,2]
            ]
Output: True

Input: matrix = [   [1,2],
                    [2,2]
            ]
Output: False

Дана матрица размера m x n. Верните True, если она является тёплицевой матрицей, и False — в противном случае.

Матрица называется тёплицевой, если все диагонали, идущие от левого верхнего угла к правому нижнему, содержат одинаковые элементы.

Примеры:
Ввод: matrix = [[1,2,3,4],
                [5,1,2,3],
                [9,5,1,2]
        ]
Вывод: True

Ввод: matrix = [[1,2],
                [2,2]
        ]
Вывод: False
'''

from typing import List

def is_toeplitz_matrix(matrix: List[List[int]]) -> bool:
    rows, columns = len(matrix), len(matrix[0])
    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True