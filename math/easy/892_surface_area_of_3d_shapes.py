'''
Given an n x n 2D grid, where each value grid[i][j] represents the number of 1x1x1 cubes stacked vertically at position.
After placing the cubes, all directly adjacent cubes are glued together, forming one or more irregular 3D shapes.

Calculate the total surface area of the resulting glued shapes.

Note:
    + The bottom face of each shape counts toward the surface area;
    + Adjacent cubes glued together do not contribute shared faces to the surface area.

Examples:
Input: grid = [ [1,2],
                [3,4]
        ]
Output: 34

Input: grid = [ [1,1,1],
                [1,0,1],
                [1,1,1]
        ]
Output: 32

Вам дан двумерный массив размера n x n, где каждое значение grid[i][j] обозначает количество кубиков размером 1x1x1, поставленных друг на друга в ячейке.
После размещения кубиков, все смежные кубики склеиваются, образуя одну или несколько неправильных 3D фигур.

Ваша задача — вычислить полную площадь поверхности всех получившихся фигур.

Примечание:
    + Нижняя грань каждой фигуры засчитывается в площадь;
    + Общие грани между склеенными кубиками не учитываются в общей площади — считаются только открытые (внешние) грани.

Примеры:
Ввод: grid = [  [1,2],
                [3,4]
        ]
Вывод: 34

Ввод: grid = [  [1,1,1],
                [1,0,1],
                [1,1,1]
        ]
Вывод: 32
'''

from typing import List

def surface_area(grid: List[List[int]]) -> int:
    n = len(grid)
    surface_area = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                surface_area += grid[i][j] * 6 - (grid[i][j] - 1) * 2

                if i > 0:
                    surface_area -= min(grid[i][j], grid[i-1][j]) * 2
                if j > 0:
                    surface_area -= min(grid[i][j], grid[i][j-1]) * 2

    return surface_area