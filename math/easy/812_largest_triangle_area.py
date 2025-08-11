'''
Given an array of 2D points on the XY-plane, where each point is represented as points[i] = [xi, yi]. 

Return the area of the largest triangle that can be formed by any three different points from the array.

Examples:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000

Дан массив точек на двумерной плоскости, где каждая точка представлена как points[i] = [xi, yi].

Необходимо вернуть площадь наибольшего треугольника, который можно построить, выбрав любые три различные точки из массива.

Примеры:
Ввод: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Вывод: 2.00000

Ввод: points = [[1,0],[0,0],[0,1]]
Вывод: 0.50000
'''

from typing import List
from itertools import combinations

def largest_triangle_area(points: List[List[int]]) -> float:
    def area(point_1, point_2, point_3):
        return abs(
            point_1[0] * (point_2[1] - point_3[1]) +
            point_2[0] * (point_3[1] - point_1[1]) +
            point_3[0] * (point_1[1] - point_2[1])
        ) / 2

    max_area = 0
    for point_1, point_2, point_3 in combinations(points, 3):
        max_area = max(max_area, area(point_1, point_2, point_3))
    return max_area