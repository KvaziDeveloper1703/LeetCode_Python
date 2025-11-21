'''
You are given a 0-indexed integer array numbers and two integers target and start.

Your task is to find an index i such that:
    - numbers[i] == target, and
    - the value abs(i - start) is minimized.

Here, abs(x) denotes the absolute value of x. Return the value abs(i - start).

Examples:
Input: numbers = [1,2,3,4,5], target = 5, start = 3
Output: 1

Input: numbers = [1], target = 1, start = 0
Output: 0

Дан целочисленный массив numbers с индексацией с 0 и два числа - target и start.

Нужно найти такой индекс i, что:
    - numbers[i] == target,
    - величина abs(i - start) минимальна.

Здесь abs(x) - это абсолютное значение числа x. Верните abs(i - start).

Примеры:
Ввод: numbers = [1,2,3,4,5], target = 5, start = 3
Вывод: 1

Ввод: numbers = [1], target = 1, start = 0
Вывод: 0
'''

from typing import List

def get_min_distance(numbers: List[int], target: int, start: int) -> int:
    minimum_distance = float('inf')

    for index in range(len(numbers)):
        if numbers[index] == target:
            distance = abs(index - start)
            if distance < minimum_distance:
                minimum_distance = distance

    return minimum_distance