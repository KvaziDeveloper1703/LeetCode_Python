'''
Given a 2D integer array matrix, return the transpose of the matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, meaning the row and column indices of the matrix are switched.

Examples:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Дана двумерная целочисленная матрица matrix. Верните её транспонированную матрицу.
Транспонированная матрица — это матрица, полученная путем отражения по главной диагонали, то есть строки становятся столбцами, а столбцы — строками.

Примеры:
Ввод: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Вывод: [[1,4,7],[2,5,8],[3,6,9]]

Ввод: matrix = [[1,2,3],[4,5,6]]
Вывод: [[1,4],[2,5],[3,6]]
'''

from typing import List

def transpose(matrix: List[List[int]]) -> List[List[int]]:
    transposed = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transposed.append(new_row)
    return transposed