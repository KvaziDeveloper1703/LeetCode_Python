'''
You are given an m x n grid obstacle_grid, where 0 represents an empty cell and 1 an obstacle. A robot starts at the top-left corner and wants to reach the bottom-right corner. It can only move right or down, and cannot pass through obstacles.
Return the number of unique paths the robot can take to reach the bottom-right corner avoiding obstacles.

Example:
Input: [[0,0,0],[0,1,0],[0,0,0]]
Output: 2

Дан m x n массив obstacle_grid, где 0 — свободная клетка, 1 — препятствие. Робот стартует в левом верхнем углу и должен попасть в правый нижний, двигаясь только вниз или вправо, избегая препятствий.
Вернуть количество уникальных путей от старта до финиша, не наступая на препятствия.

Пример:
Ввод: [[0,0,0],[0,1,0],[0,0,0]]
Вывод: 2
'''

from typing import List

def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    total_rows = len(obstacle_grid)
    total_columns = len(obstacle_grid[0])
    path_count_grid = []

    for row_index in range(total_rows):
        current_row = []
        for column_index in range(total_columns):
            current_row.append(0)
        path_count_grid.append(current_row)

    if obstacle_grid[0][0] == 1:
        return 0

    path_count_grid[0][0] = 1

    for row_index in range(total_rows):
        for column_index in range(total_columns):
            if obstacle_grid[row_index][column_index] == 1:
                path_count_grid[row_index][column_index] = 0
            else:
                if row_index > 0:
                    paths_from_top = path_count_grid[row_index - 1][column_index]
                    path_count_grid[row_index][column_index] += paths_from_top
                if column_index > 0:
                    paths_from_left = path_count_grid[row_index][column_index - 1]
                    path_count_grid[row_index][column_index] += paths_from_left

    return path_count_grid[total_rows - 1][total_columns - 1]