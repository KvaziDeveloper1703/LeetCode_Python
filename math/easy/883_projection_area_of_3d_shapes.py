'''
Given an n x n grid where each grid[i][j] contains a number v, representing a tower of v cubes of size 1×1×1 placed on the cell.

All cubes are aligned with the x, y, and z axes.

We consider the projection of this 3D structure onto the XY, YZ, and ZX planes:
    + XY-plane: Count 1 for each cell that contains at least one cube;
    + YZ-plane: Take the maximum height in each row;
    + ZX-plane: Take the maximum height in each column.

Return the total area of all three projections.

Examples:
Input: grid = [[1,2],[3,4]]
Output: 17

Input: grid = [[2]]
Output: 5

Дан двумерный массив grid размера n x n, где каждая ячейка grid[i][j] содержит число v, обозначающее башню из v кубиков размером 1×1×1, размещённых в ячейке.

Все кубики ориентированы по осям x, y и z.

Требуется найти суммарную площадь трёх проекций фигуры на плоскости:
    + XY-плоскость — вид сверху: учитывается каждая ячейка, где есть хотя бы один кубик;
    + YZ-плоскость — вид спереди: максимальная высота в каждой строке;
    + ZX-плоскость — вид сбоку: максимальная высота в каждом столбце.

Верните общую площадь всех трёх проекций.

Примеры:
Ввод: grid = [[1,2],[3,4]]
Вывод: 17

Ввод: grid = [[2]]
Вывод: 5
'''

from typing import List

def projection_area(grid: List[List[int]]) -> int:
    n = len(grid)
    xy = 0
    yz = 0
    zx = 0

    for i in range(n):
        row_max = 0
        for j in range(n):
            if grid[i][j] > 0:
                xy += 1
            row_max = max(row_max, grid[i][j])
        zx += row_max

    for j in range(n):
        column_max = 0
        for i in range(n):
            column_max = max(column_max, grid[i][j])
        yz += column_max

    return xy + yz + zx