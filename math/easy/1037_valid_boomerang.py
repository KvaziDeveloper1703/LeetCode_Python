'''
Given an array points, where points[i] = [xi, yi] represents a point on the 2D X-Y plane.
Return True if these points form a boomerang.

A boomerang is a set of exactly three points that:
    1) Are all distinct.
    2) Do not lie on the same straight line.

Examples:
Input: points = [[1,1],[2,3],[3,2]]
Output: True

Input: points = [[1,1],[2,2],[3,3]]
Output: False

Дан массив points, где points[i] = [xi, yi] обозначает точку на двумерной декартовой плоскости.
Верните True, если эти точки образуют бумеранг.

Бумеранг — это набор ровно трёх точек, которые:
    1) Все разные.
    2) Не лежат на одной прямой.

Примеры:
Ввод: points = [[1,1],[2,3],[3,2]]
Вывод: True

Ввод: points = [[1,1],[2,2],[3,3]]
Вывод: False
'''

from typing import List

def is_boomerang(points: List[List[int]]) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = points

    if len({(x1, y1), (x2, y2), (x3, y3)}) < 3:
        return False

    return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)