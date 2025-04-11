'''
You are given an m x n integer matrix.
If an element in the matrix is 0, set its entire row and column to 0.
You must perform this operation in place, meaning you cannot use additional space for another matrix.

Examples:
Input: matrix = [[1,1,1], 
                 [1,0,1],
                 [1,1,1]]
Output: [[1,0,1],
         [0,0,0],
         [1,0,1]]

Input: matrix = [[0,1,2,0], 
                 [3,4,5,2], 
                 [1,3,1,5]]
Output: [[0,0,0,0],
         [0,4,5,0],
         [0,3,1,0]]
'''

from typing import List

def set_zeroes(matrix: List[List[int]]) -> None:
    rows, columns = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(columns))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_has_zero:
        for j in range(columns):
            matrix[0][j] = 0

    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0