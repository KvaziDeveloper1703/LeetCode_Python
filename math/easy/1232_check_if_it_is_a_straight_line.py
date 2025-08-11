'''
Given an array coordinates, where coordinates[i] = [x, y] represents the coordinate of a point in the XY-plane.
Determine whether all the given points lie on a single straight line.

Examples:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: True

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: False

Вам дан массив coordinates, где coordinates[i] = [x, y] — это координата точки на плоскости XY.
Определите, лежат ли все заданные точки на одной прямой.

Примеры:
Ввод: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Вывод: True

Ввод: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Вывод: False
'''

from typing import List

def check_straight_line(coordinates: List[List[int]]) -> bool:
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]

    dx = x1 - x0
    dy = y1 - y0

    for x, y in coordinates[2:]:
        if (x - x0) * dy != (y - y0) * dx:
            return False
    return True