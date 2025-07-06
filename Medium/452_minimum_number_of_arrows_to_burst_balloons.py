'''
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points, where points[i] = [x_start, x_end] denotes a balloon whose horizontal diameter stretches between x_start and x_end. You do not know the exact y-coordinates of the balloons.
Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with x_start and x_end is burst by an arrow shot at x if x_start <= x <= x_end. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Examples:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4

На плоской стене, представляющей собой координатную плоскость XY, прикреплены сферические воздушные шары. Каждый шар задан в виде двумерного массива points, где points[i] = [x_start, x_end] — это горизонтальный диаметр шара, простирающийся от x_start до x_end. Точные координаты по y неизвестны.
Вы можете стрелять стрелами вверх (по положительному направлению оси Y) из любых точек на оси X. Одна стрела, пущенная из точки x, пробивает все шары, у которых x_start <= x <= x_end. Стрел можно выпустить сколько угодно, и они летят вверх бесконечно, пробивая все шары на своём пути.
По заданному массиву points необходимо вернуть минимальное количество стрел, необходимых для того, чтобы пробить все шары.

Примеры:
Ввод: points = [[10,16],[2,8],[1,6],[7,12]]
Вывод: 2

Ввод: points = [[1,2],[3,4],[5,6],[7,8]]
Вывод: 4
'''

from typing import List

def find_min_arrow_shots(balloon_intervals: List[List[int]]) -> int:
    if not balloon_intervals:
        return 0

    balloon_intervals.sort(key=lambda interval: interval[1])

    minimum_arrows_required = 1
    current_arrow_position = balloon_intervals[0][1]

    for balloon_start, balloon_end in balloon_intervals[1:]:
        if balloon_start > current_arrow_position:
            minimum_arrows_required += 1
            current_arrow_position = balloon_end

    return minimum_arrows_required