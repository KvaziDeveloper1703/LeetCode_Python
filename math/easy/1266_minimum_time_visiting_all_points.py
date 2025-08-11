'''
Given n points on a 2D plane, with integer coordinates points[i] = [xi, yi].

Return the minimum time in seconds required to visit all the points in the order they are given.

You can move according to these rules:
    1) In 1 second, you can move vertically by 1 unit;
    2) In 1 second, you can move horizontally by 1 unit;
    3) In 1 second, you can move diagonally.

You must visit the points in the same order they appear in the array. You may pass through points that appear later in the order, but this does not count as visiting them.

Examples:
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7

Input: points = [[3,2],[-2,2]]
Output: 5

Даны n точек на плоскости с целыми координатами points[i] = [xi, yi].

Найдите минимальное время в секундах, необходимое, чтобы посетить все точки в указанном порядке.

Правила перемещения:
    1) За 1 секунду можно сдвинуться вверх/вниз на 1 единицу;
    2) За 1 секунду можно сдвинуться влево/вправо на 1 единицу;
    3) За 1 секунду можно сдвинуться по диагонали.

Точки нужно посещать в том же порядке, в котором они даны. Можно проходить через точки, которые встречаются позже в порядке, но это не считается их посещением.

Примеры:
Ввод: points = [[1,1],[3,4],[-1,0]]
Вывод: 7

Ввод: points = [[3,2],[-2,2]]
Вывод: 5
'''

from typing import List

def minimum_time_to_visit_all_points(points: List[List[int]]) -> int:
    total_time = 0

    for i in range(1, len(points)):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        total_time += max(dx, dy)

    return total_time