'''
You are given an m x n grid filled with non-negative numbers. A robot starts at the top-left corner and wants to reach the bottom-right corner, moving only right or down.
Find a path that minimizes the sum of all numbers along the way and return that minimum sum.

Example:
Input: [[1,3,1],
        [1,5,1],
        [4,2,1]
    ]
Output: 7

Дана матрица m x n, заполненная неотрицательными числами. Робот стартует из левого верхнего угла и должен дойти до правого нижнего, двигаясь только вниз или вправо.
Найдите путь с минимальной суммой чисел и верните эту сумму.

Пример:
Ввод: [ [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
Вывод: 7
'''

from typing import List

def minimum_path_sum(cost_grid: List[List[int]]) -> int:
    total_rows = len(cost_grid)
    total_columns = len(cost_grid[0])

    min_sum_grid = []

    for row_index in range(total_rows):
        current_row = []
        for column_index in range(total_columns):
            current_row.append(0)
        min_sum_grid.append(current_row)

    for row_index in range(total_rows):
        for column_index in range(total_columns):
            current_cell_cost = cost_grid[row_index][column_index]

            if row_index == 0 and column_index == 0:
                min_sum_grid[row_index][column_index] = current_cell_cost
            elif row_index == 0:
                min_sum_grid[row_index][column_index] = min_sum_grid[row_index][column_index - 1] + current_cell_cost
            elif column_index == 0:
                min_sum_grid[row_index][column_index] = min_sum_grid[row_index - 1][column_index] + current_cell_cost
            else:
                cost_from_top = min_sum_grid[row_index - 1][column_index]
                cost_from_left = min_sum_grid[row_index][column_index - 1]
                min_sum_grid[row_index][column_index] = min(cost_from_top, cost_from_left) + current_cell_cost

    return min_sum_grid[total_rows - 1][total_columns - 1]