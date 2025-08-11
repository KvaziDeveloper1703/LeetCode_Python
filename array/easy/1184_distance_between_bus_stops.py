'''
A bus has n stops numbered from 0 to n - 1 arranged in a circle. The bus can travel in both directions: clockwise and counterclockwise.
You have an array distance where distance[i] represents the distance between stop i and stop (i + 1) % n.

Given two stops, start and destination, return the shortest distance between them.

Examples:
Input: distance = [1, 2, 3, 4], start = 0, destination = 1
Output: 1

Input: distance = [1, 2, 3, 4], start = 0, destination = 2
Output: 3

У автобуса есть n остановок, пронумерованных от 0 до n - 1, которые образуют круг. Автобус может двигаться в обоих направлениях: по часовой стрелке и против часовой стрелки.
Дан массив distance, где distance[i] — это расстояние между остановкой i и остановкой (i + 1) % n.

По заданным остановкам start и destination верните минимальное расстояние между ними.

Примеры:
Ввод: distance = [1, 2, 3, 4], start = 0, destination = 1
Вывод: 1

Ввод: distance = [1, 2, 3, 4], start = 0, destination = 2
Вывод: 3
'''

from typing import List

def distance_between_bus_stops(distance: List[int], start: int, destination: int) -> int:
    if start > destination:
        start, destination = destination, start

    total = sum(distance)
    clockwise = sum(distance[start:destination])
    counterclockwise = total - clockwise
    return min(clockwise, counterclockwise)