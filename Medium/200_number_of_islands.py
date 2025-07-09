'''
You are given an m x n 2D binary grid representing a map, where:
    + '1' represents land;
    + '0' represents water.

Your task is to return the number of islands in the grid. An island is a group of '1's connected horizontally or vertically. All the edges of the grid are surrounded by water.

Examples:
Input: grid = [ ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
        ]
Output: 1

Input: grid = [ ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
        ]
Output: 3

Дан двумерный бинарный массив размера m x n, представляющий карту, где:
    + '1' — это земля;
    + '0' — это вода.

Необходимо вернуть количество островов на карте. Остров — это группа ячеек '1', связанных по горизонтали или вертикали. Все края сетки окружены водой.

Примеры:
Ввод: grid = [  ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ]
Вывод: 1

Ввод: grid = [  ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
Вывод: 3
'''

from typing import List

def number_of_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    total_rows = len(grid)
    total_columns = len(grid[0])
    visited_cells = [[False for _ in range(total_columns)] for _ in range(total_rows)]

    def depth_first_search(row: int, column: int):
        if (row < 0 or row >= total_rows or
            column < 0 or column >= total_columns or
            grid[row][column] == '0' or
            visited_cells[row][column]):
            return

        visited_cells[row][column] = True
        depth_first_search(row + 1, column)
        depth_first_search(row - 1, column)
        depth_first_search(row, column + 1)
        depth_first_search(row, column - 1)

    number_of_islands = 0

    for current_row in range(total_rows):
        for current_column in range(total_columns):
            if grid[current_row][current_column] == '1' and not visited_cells[current_row][current_column]:
                depth_first_search(current_row, current_column)
                number_of_islands += 1

    return number_of_islands