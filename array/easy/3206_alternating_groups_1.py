'''
You are given a circular arrangement of red and blue tiles, represented by an integer array colors.

The color of tile i is defined as:
    - colors[i] = 0 means tile i is red;
    - colors[i] = 1 means tile i is blue.

An alternating group is any set of 3 contiguous tiles in the circle where the colors alternate in the following sense: the middle tile must have a different color than both its left and right neighbors.

In other words, for three consecutive tiles (a, b, c) to form an alternating group: b != a and b != c.

Return the number of alternating groups in the circle.

Examples:
Input: colors = [1, 1, 1]
Output: 0

Input: colors = [0, 1, 0, 0, 1]
Output: 3

Дана круговая последовательность красных и синих плиток, заданная массивом целых чисел colors.

Цвет плитки i определяется так:
    - colors[i] = 0 означает, что плитка красная;
    - colors[i] = 1 означает, что плитка синяя.

Чередующейся группой (alternating group) называется любая группа из 3 подряд идущих плиток по кругу, если: средняя плитка отличается по цвету от левой и правой плитки.

То есть для тройки (a, b, c) должно выполняться: b != a и b != c.

Нужно вернуть количество чередующихся групп.

Примеры:
Ввод: colors = [1, 1, 1]
Вывод: 0

Ввод: colors = [0, 1, 0, 0, 1]
Вывод: 3
'''

from typing import List

def number_of_alternating_groups(colors: List[int]) -> int:
    tilesCount = len(colors)
    alternatingGroupsCount = 0

    for index in range(tilesCount):
        leftIndex = (index - 1) % tilesCount
        rightIndex = (index + 1) % tilesCount

        if colors[leftIndex] == colors[rightIndex] and colors[index] != colors[leftIndex]:
            alternatingGroupsCount += 1

    return alternatingGroupsCount