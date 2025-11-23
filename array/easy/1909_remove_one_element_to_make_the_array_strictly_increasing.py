'''
Given a 0-indexed array of integers numbers, return True if it is possible to make the array strictly increasing by removing exactly one element. If the array is already strictly increasing, return True.

An array is strictly increasing if for every index i the condition numbers[i - 1] < numbers[i] holds.

Examples:
Input: numbers = [1, 2, 10, 5, 7]
Output: True

Input: numbers = [2, 3, 1, 2]
Output: False

Дан целочисленный массив numbers с индексами, начинающимися с 0. Верните True, если массив можно сделать строго возрастающим, удалив ровно один элемент. Если массив уже является строго возрастающим, также верните True.

Массив считается строго возрастающим, если для каждого индекса i (1 ≤ i < numbers.length) выполняется условие: numbers[i - 1] < numbers[i].

Примеры:
Ввод: numbers = [1, 2, 10, 5, 7]
Вывод: True

Ввод: numbers = [2, 3, 1, 2]
Вывод: False
'''

from typing import List

def can_be_increasing(numbers: List[int]) -> bool:
    n = len(numbers)
    removed = False

    for i in range(1, n):
        if numbers[i] <= numbers[i - 1]:
            if removed:
                return False
            removed = True

            if i == 1 or numbers[i] > numbers[i - 2]:
                continue

            numbers[i - 1] = numbers[i]
    return True