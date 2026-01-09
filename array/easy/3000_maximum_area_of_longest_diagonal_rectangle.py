'''
You are given a 2D 0-indexed integer array dimensions.

For each index i such that 0 ≤ i < dimensions.length:
    - dimensions[i][0] represents the length of the i-th rectangle,
    - dimensions[i][1] represents the width of the i-th rectangle.

The diagonal length of a rectangle depends on its length and width.
Your task is to determine which rectangle has the longest diagonal and return its area.
If there are multiple rectangles with the same longest diagonal, return the maximum area among them.

Examples:
Input: dimensions = [[9,3],[8,6]]
Output: 48

Input: dimensions = [[3,4],[4,3]]
Output: 12

Дан двумерный целочисленный массив dimensions с индексацией от 0.

Для каждого индекса i, где 0 ≤ i < dimensions.length:
    - dimensions[i][0] - длина прямоугольника,
    - dimensions[i][1] - ширина прямоугольника.

Длина диагонали прямоугольника определяется его длиной и шириной.
Необходимо определить, у какого прямоугольника диагональ самая длинная, и вернуть его площадь.
Если существует несколько прямоугольников с одинаковой максимальной длиной диагонали, нужно вернуть наибольшую площадь среди них.

Примеры:
Ввод: dimensions = [[9,3],[8,6]]
Вывод: 48

Ввод: dimensions = [[3,4],[4,3]]
Вывод: 12
'''

from typing import List

def area_of_max_diagonal(dimensions: List[List[int]]) -> int:
    max_diagonal_squared = 0
    max_area = 0

    for length, width in dimensions:
        diagonal_squared = length * length + width * width
        area = length * width

        if diagonal_squared > max_diagonal_squared:
            max_diagonal_squared = diagonal_squared
            max_area = area
        elif diagonal_squared == max_diagonal_squared:
            max_area = max(max_area, area)

    return max_area