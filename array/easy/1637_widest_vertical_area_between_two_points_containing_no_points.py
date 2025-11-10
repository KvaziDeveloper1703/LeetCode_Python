'''
You are given n points on a 2D plane, where points[i] = [x_i, y_i].

Your task is to find the widest vertical area between two points such that no points lie inside that area.

A vertical area is a region with a fixed width that extends infinitely along the y-axis.

The widest vertical area is the one with the maximum distance between two adjacent points along the x-axis — such that no points exist between them.

Examples:
Input: points = [   [8,7],
                    [9,9],
                    [7,4],
                    [9,7]
            ]
Output: 1

Input: points = [   [3,1],
                    [9,0],
                    [1,0],
                    [1,4],
                    [5,3],
                    [8,8]
            ]
Output: 3

Дано n точек на плоскости, где points[i] = [x_i, y_i].

Нужно найти наиболее широкую вертикальную область между двумя точками так, чтобы внутри этой области не было других точек.

Вертикальная область - это зона фиксированной ширины, которая простирается вверх и вниз бесконечно.

Нужно определить максимальную ширину такой области между соседними точками по оси x, где между ними нет других точек.

Примеры:

Ввод: points = [[8,7],
                [9,9],
                [7,4],
                [9,7]
            ]
Вывод: 1

Ввод: points = [[3,1],
                [9,0],
                [1,0],
                [1,4],
                [5,3],
                [8,8]
            ]
Вывод: 3
'''

from typing import List

class Solution:
    def max_width_of_vertical_area(self, points: List[List[int]]) -> int:
        x_coords = [x for x, y in points]
        x_coords.sort()
        max_width = 0

        for i in range(1, len(x_coords)):
            width = x_coords[i] - x_coords[i - 1]
            if width > max_width:
                max_width = width

        return max_width