'''
You are given two integers x and y, representing your current position on a Cartesian grid: (x, y).
You are also given an array points, where each element points[i] = [aᵢ, bᵢ] represents a point located at (aᵢ, bᵢ).

A point is considered valid if it shares either the same x-coordinate or the same y-coordinate as your current location.

Return the 0-indexed index of the valid point with the smallest Manhattan distance to your current location.
If multiple valid points have the same smallest distance, return the one with the smallest index.
If there are no valid points, return -1.

The Manhattan distance between points (x₁, y₁) and (x₂, y₂) is defined as: abs(x₁ − x₂) + abs(y₁ − y₂)

Examples:
Input: x = 3, y = 4, points = [[1,2], [3,1], [2,4], [2,3], [4,4]]
Output: 2

Input: x = 3, y = 4, points = [[3,4]]
Output: 0

Даны два целых числа x и y, которые обозначают вашу текущую позицию на декартовой плоскости: (x, y).
Также дан массив points, где каждый элемент points[i] = [aᵢ, bᵢ] - это координаты точки (aᵢ, bᵢ).

Точка считается подходящей (valid), если она имеет такую же координату x или такую же координату y, как и ваша текущая позиция.

Нужно вернуть индекс (0-based) подходящей точки с минимальным манхэттенским расстоянием до вашей позиции.
Если таких точек несколько, вернуть ту, у которой меньший индекс.
Если подходящих точек нет, вернуть -1.

Манхэттенское расстояние между точками (x₁, y₁) и (x₂, y₂) определяется формулой: abs(x₁ − x₂) + abs(y₁ − y₂)

Примеры:
Ввод: x = 3, y = 4, points = [[1,2], [3,1], [2,4], [2,3], [4,4]]
Вывод: 2

Ввод: x = 3, y = 4, points = [[3,4]]
Вывод: 0
'''

from typing import List

def nearest_valid_point(x: int, y: int, points: List[List[int]]) -> int:
    nearest_index = -1
    nearest_distance = float('inf')

    for index, (point_x, point_y) in enumerate(points):
        if point_x == x or point_y == y:
            distance = abs(x - point_x) + abs(y - point_y)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_index = index

    return nearest_index