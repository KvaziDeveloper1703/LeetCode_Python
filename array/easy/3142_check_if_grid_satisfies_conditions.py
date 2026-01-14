'''
You are given a 2D matrix grid of size m × n. You need to check whether every cell grid[i][j] satisfies the following conditions:
    - It is equal to the cell directly below it, meaning grid[i][j] == grid[i + 1][j];
    - It is different from the cell directly to its right, meaning grid[i][j] != grid[i][j + 1].

Return True if all cells satisfy these conditions, otherwise return False.

Examples:
Input: grid = [[1,0,2],[1,0,2]]
Output: True

Input: grid = [[1,1,1],[0,0,0]]
Output: False

Дана двумерная матрица grid размера m × n. Нужно проверить, выполняются ли для каждой ячейки grid[i][j] следующие условия:
    - Она равна ячейке снизу, то есть grid[i][j] == grid[i + 1][j];
    - Она не равна ячейке справа, то есть grid[i][j] != grid[i][j + 1][j].

Верни True, если все ячейки удовлетворяют этим условиям, иначе верни False.

Примеры:
Ввод: grid = [[1,0,2],[1,0,2]]
Вывод: True

Ввод: grid = [[1,1,1],[0,0,0]]
Вывод: False
'''

from typing import List

def satisfies_conditions(grid: List[List[int]]) -> bool:
    row_count = len(grid)
    column_count = len(grid[0])

    for row_index in range(row_count):
        for column_index in range(column_count):
            if row_index + 1 < row_count:
                if grid[row_index][column_index] != grid[row_index + 1][column_index]:
                    return False

            if column_index + 1 < column_count:
                if grid[row_index][column_index] == grid[row_index][column_index + 1]:
                    return False

    return True