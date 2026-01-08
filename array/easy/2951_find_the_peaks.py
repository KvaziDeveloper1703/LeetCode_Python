'''
You are given a 0-indexed integer array mountain.

Your task is to find all peak elements in the array and return their indices in any order.

Definitions:
    - A peak is an element that is strictly greater than both of its neighboring elements;
    - The first and last elements of the array cannot be peaks.

Examples:
Input:  mountain = [2, 4, 4]
Output: []

Input:  mountain = [1, 4, 3, 8, 5]
Output: [1, 3]

Дан целочисленный массив mountain с нумерацией элементов с нуля.

Необходимо найти все пиковые элементы массива и вернуть массив их индексов в произвольном порядке.

Определения:
    - Пик - это элемент, который строго больше обоих своих соседей;
    - Первый и последний элементы массива не могут быть пиками.

Примеры:
Ввод:  mountain = [2, 4, 4]
Вывод: []

Ввод:  mountain = [1, 4, 3, 8, 5]
Вывод: [1, 3]
'''

from typing import List

def find_зeaks(mountain: List[int]) -> List[int]:
    peaks = []

    for i in range(1, len(mountain) - 1):
        if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
            peaks.append(i)

    return peaks