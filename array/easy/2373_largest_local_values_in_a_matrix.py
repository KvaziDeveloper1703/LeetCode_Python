'''
You are given an n × n integer matrix called grid.

Create a new integer matrix maxLocal of size (n − 2) × (n − 2) such that:
    - maxLocal[i][j] contains the maximum value from the 3 × 3 submatrix of grid;
    - This submatrix is centered at position (i + 1, j + 1) in grid.

In other words, for every possible contiguous 3 × 3 submatrix inside grid, determine its largest element and place it in the corresponding position in maxLocal.

Return the resulting matrix maxLocal.

Вам дана целочисленная матрица grid размера n × n.

Необходимо создать новую целочисленную матрицу maxLocal размера (n − 2) × (n − 2), где:
    - maxLocal[i][j] равен наибольшему элементу в подматрице 3 × 3 исходной матрицы grid;
    - Эта подматрица имеет центр в позиции (i + 1, j + 1) матрицы grid.

Иными словами, для каждой возможной непрерывной подматрицы 3 × 3 в grid нужно найти максимальный элемент и записать его в соответствующую ячейку матрицы maxLocal.

Верните полученную матрицу maxLocal.
'''

from typing import List

def largest_local(grid: List[List[int]]) -> List[List[int]]:
    grid_size = len(grid)
    result_matrix = []

    for row_index in range(grid_size - 2):
        result_row = []
        for column_index in range(grid_size - 2):
            maximum_value = 0
            for inner_row in range(row_index, row_index + 3):
                for inner_column in range(column_index, column_index + 3):
                    maximum_value = max(maximum_value, grid[inner_row][inner_column])
            result_row.append(maximum_value)
        result_matrix.append(result_row)

    return result_matrix