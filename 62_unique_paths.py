'''
There is a robot on an m x n grid. The robot starts at the top-left corner of the grid (grid[0][0]) and wants to reach the bottom-right corner (grid[m - 1][n - 1]).
At any point in time, the robot can only move right or down.

Given two integers m and n, return the number of unique paths the robot can take to reach the bottom-right corner.
It is guaranteed that the answer will not exceed 2 * 10⁹.

Example:
Input: m = 3, n = 7
Output: 28

На сетке размером m x n находится робот. Изначально он стоит в левом верхнем углу (grid[0][0]) и хочет попасть в правый нижний угол (grid[m - 1][n - 1]).
Робот может двигаться только вниз или вправо в любой момент времени.

По заданным значениям m и n, верните количество уникальных путей, по которым робот может дойти до правого нижнего угла.
Гарантируется, что ответ не превышает 2 * 10⁹.

Пример:
Ввод: m = 3, n = 7
Вывод: 28
'''

def unique_paths(total_rows: int, total_columns: int) -> int:
    path_count_grid = []

    for row_index in range(total_rows):
        current_row = []
        for column_index in range(total_columns):
            current_row.append(1)
        path_count_grid.append(current_row)
    
    for current_row in range(1, total_rows):
        for current_column in range(1, total_columns):
            number_of_paths_from_top = path_count_grid[current_row - 1][current_column]
            number_of_paths_from_left = path_count_grid[current_row][current_column - 1]
            total_paths_to_current_cell = number_of_paths_from_top + number_of_paths_from_left
            path_count_grid[current_row][current_column] = total_paths_to_current_cell
    
    return path_count_grid[total_rows - 1][total_columns - 1]