'''
You have an array of floating point numbers averages, which is initially empty.
You are given an integer array numbers of length n, where n is even.

Repeat the following process n / 2 times:
    - Remove the smallest element minElement and the largest element maxElement from numbers;
    - Compute (minElement + maxElement) / 2 and add the result to the array averages.

After all operations, return the minimum value in the array averages.

Examples:
Input: numbers = [7, 8, 3, 4, 15, 13, 4, 1]
Output: 5.5

Input: numbers = [1, 9, 8, 3, 10, 5]
Output: 5.5

Есть массив вещественных чисел averages, который изначально пуст.
Дан целочисленный массив numbers длины n, причём n чётное.

Повторите следующий процесс n / 2 раз:
    - Удалите из массива numbers минимальный элемент minElement и максимальный элемент maxElement;
    - Вычислите (minElement + maxElement) / 2 и добавьте результат в массив averages.

После выполнения всех шагов верните минимальный элемент массива averages.

Примеры:
Ввод: numbers = [7, 8, 3, 4, 15, 13, 4, 1]
Вывод: 5.5

Ввод: numbers = [1, 9, 8, 3, 10, 5]
Вывод: 5.5
'''

from typing import List

def minimum_average(numbers: List[int]) -> float:
    numbers.sort()

    left_index = 0
    right_index = len(numbers) - 1
    minimum_average = float("inf")

    while left_index < right_index:
        current_average = (numbers[left_index] + numbers[right_index]) / 2
        minimum_average = min(minimum_average, current_average)
        left_index += 1
        right_index -= 1

    return minimum_average