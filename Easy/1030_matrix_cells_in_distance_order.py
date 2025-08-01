'''
Given four integers: rows, columns, rCenter, and cCenter.
    + There is a matrix with dimensions rows × columns.
    + You are located at the cell with coordinates (rCenter, cCenter).
    + Your task is to return the coordinates of all cells in the matrix, sorted by their Manhattan distance from (rCenter, cCenter).

The Manhattan distance between two cells is the number of steps needed to move from one cell to the other if you can only move up, down, left, or right.
The result can be returned in any order that respects the condition of being sorted from the smallest distance to the largest.

Examples:
Input: rows = 1, columns = 2, rCenter = 0, cCenter = 0
Output: [[0,0], [0,1]]

Input: rows = 2, columns = 2, rCenter = 0, cCenter = 1
Output: [[0,1], [0,0], [1,1], [1,0]]

Даны четыре целых числа: rows, columns, rCenter, cCenter.
    + Есть матрица размером rows × columns.
    + Вы находитесь в ячейке с координатами (rCenter, cCenter).
    + Нужно вернуть координаты всех ячеек матрицы, отсортированные по их манхэттенскому расстоянию до (rCenter, cCenter).

Манхэттенское расстояние между двумя ячейками — это количество шагов, которое нужно сделать, чтобы перейти из одной ячейки в другую, если можно двигаться только вверх, вниз, влево или вправо.
Результат можно вернуть в любом порядке, если расстояния расположены от меньшего к большему.

Примеры:
Ввод: rows = 1, columns = 2, rCenter = 0, cCenter = 0
Вывод: [[0,0], [0,1]]

Ввод: rows = 2, columns = 2, rCenter = 0, cCenter = 1
Вывод: [[0,1], [0,0], [1,1], [1,0]]
'''

from typing import List

def all_cells_distance_order(rows: int, columns: int, rCenter: int, cCenter: int) -> List[List[int]]:
    cells = []

    for r in range(rows):
        for c in range(columns):
            distance = abs(r - rCenter) + abs(c - cCenter)
            cells.append((distance, [r, c]))

    cells.sort(key=lambda x: x[0])

    return [coord for _, coord in cells]