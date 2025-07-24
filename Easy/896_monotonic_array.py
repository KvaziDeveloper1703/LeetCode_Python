'''
An array is called monotonic if it is either monotone increasing or monotone decreasing:
    + An array numbers is monotone increasing if for every i <= j, numbers[i] <= numbers[j].
    + An array numbers is monotone decreasing if for every i <= j, numbers[i] >= numbers[j].

Given an array of integers numbers, return True if the array is monotonic, or False otherwise.

Examples:
Input: numbers = [1, 2, 2, 3]
Output: True

Input: numbers = [6, 5, 4, 4]
Output: True

Массив называется монотонным, если он либо монотонно возрастает, либо монотонно убывает:
    + Массив numbers монотонно возрастает, если для всех i <= j выполняется numbers[i] <= numbers[j].
    + Массив numbers монотонно убывает, если для всех i <= j выполняется numbers[i] >= numbers[j].

Дан массив целых чисел numbers. Верните True, если массив монотонен, и False в противном случае.

Примеры:
Ввод: numbers = [1, 2, 2, 3]
Вывод: True

Ввод: numbers = [6, 5, 4, 4]
Вывод: True
'''

from typing import List

def is_monotonic(numbers: List[int]) -> bool:
    increasing = decreasing = True

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            decreasing = False
        if numbers[i] < numbers[i - 1]:
            increasing = False

    return increasing or decreasing