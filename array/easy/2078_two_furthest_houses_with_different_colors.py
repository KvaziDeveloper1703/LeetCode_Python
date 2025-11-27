'''
There are n houses arranged in a straight line, each painted with a certain color.
You are given a 0-indexed integer array colors of length n, where colors[i] is the color of the i-th house.

Return the maximum distance between any two houses that have different colors.

The distance between house i and house j is defined as: abs(i−j), where abs(x) is the absolute value of x.

Examples:
Input: colors = [1,1,1,6,1,1,1]
Output: 3

Input: colors = [1,8,3,8,3]
Output: 4

На улице расположены n домов в ряд, и каждый дом окрашен в определённый цвет.
Дан 0-индексированный массив colors длины n, где colors[i] - это цвет i-го дома.

Нужно вернуть максимальное расстояние между двумя домами, окрашенными в разные цвета.

Расстояние между домом i и домом j определяется так: abs(i−j), где abs(x) - абсолютное значение числа.

Примеры:
Ввод: colors = [1,1,1,6,1,1,1]
Вывод: 3

Ввод: colors = [1,8,3,8,3]
Вывод: 4
'''

from typing import List

def max_distance(colors: List[int]) -> int:
    number_of_houses = len(colors)
    maximum_distance = 0

    for right_index in range(number_of_houses):
        if colors[right_index] != colors[0]:
            maximum_distance = max(maximum_distance, right_index)

    for left_index in range(number_of_houses - 1, -1, -1):
        if colors[left_index] != colors[number_of_houses - 1]:
            maximum_distance = max(maximum_distance, number_of_houses - 1 - left_index)
            break

    return maximum_distance