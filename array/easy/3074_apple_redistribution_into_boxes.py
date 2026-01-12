'''
You are given an array apple of size n and an array capacity of size m.

There are n packs of apples, where the i-th pack contains apple[i] apples.
There are also m boxes, where the i-th box can hold up to capacity[i] apples.

You need to choose some of the boxes and redistribute all the apples from the n packs into these boxes.

Return the minimum number of boxes required to store all the apples.

Examples:
Input: apple = [1, 3, 2], capacity = [4, 3, 1, 5, 2]
Output: 2

Input: apple = [5, 5, 5], capacity = [2, 4, 2, 7]
Output: 4

Вам дан массив apple длины n и массив capacity длины m.

Существует n упаковок с яблоками, где в i-й упаковке содержится apple[i] яблок.
Также есть m коробок, где i-я коробка может вместить не более capacity[i] яблок.

Необходимо выбрать некоторое количество коробок и распределить в них все яблоки из n упаковок.

Верните минимальное количество коробок, необходимое для размещения всех яблок.

Примеры:
Ввод: apple = [1, 3, 2], capacity = [4, 3, 1, 5, 2]
Вывод: 2

Ввод: apple = [5, 5, 5], capacity = [2, 4, 2, 7]
Вывод: 4
'''

from typing import List

def minimum_boxes(apple: List[int], capacity: List[int]) -> int:
    total_apples = sum(apple)
    sorted_capacities = sorted(capacity, reverse=True)

    used_boxes = 0
    accumulated_capacity = 0

    for current_capacity in sorted_capacities:
        accumulated_capacity += current_capacity
        used_boxes += 1
        if accumulated_capacity >= total_apples:
            return used_boxes

    return used_boxes