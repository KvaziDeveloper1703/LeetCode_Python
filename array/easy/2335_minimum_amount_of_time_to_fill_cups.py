'''
You have a water dispenser that can dispense cold, warm, and hot water.

Each second, you can perform one of the following actions:
    - Fill two cups with different types of water, or
    - Fill one cup with any type of water.

You are given a 0-indexed integer array amount of length 3, where:
    - amount[0] is the number of cold water cups to fill,
    - amount[1] is the number of warm water cups to fill,
    - amount[2] is the number of hot water cups to fill.

Return the minimum number of seconds required to fill all the cups.

Examples:
Input: amount = [1, 4, 2]
Output: 4

Input: amount = [5, 4, 4]
Output: 7

У вас есть кулер, который может наливать холодную, тёплую и горячую воду.

За одну секунду можно выполнить одно из следующих действий:
    - Наполнить две чашки разными видами воды, или
    - Наполнить одну чашку любой водой.

Дан 0-индексированный целочисленный массив amount длины 3, где:
    - amount[0] - количество чашек с холодной водой,
    - amount[1] - количество чашек с тёплой водой,
    - amount[2] - количество чашек с горячей водой.

Верните минимальное количество секунд, необходимое для заполнения всех чашек.

Примеры:
Ввод: amount = [1, 4, 2]
Вывод: 4

Ввод: amount = [5, 4, 4]
Вывод: 7
'''

from typing import List

def fill_cups(amount: List[int]) -> int:
    maximum_cups = max(amount)
    total_cups = sum(amount)
    return max(maximum_cups, (total_cups + 1) // 2)