'''
You are given a 0-indexed one-dimensional integer array original, and two integers m and n.
Your task is to construct a two-dimensional array with m rows and n columns using all elements from original.

The elements from indices 0 to n − 1 of original should form the first row, the elements from indices n to 2n − 1 should form the second row, and so on, until all elements are placed.

Return the constructed m × n 2D array. If it is not possible to form such an array, return an empty 2D array.

Дан одномерный целочисленный массив original с индексацией от 0, а также два числа: m и n. Необходимо построить двумерный массив размером m строк и n столбцов, используя все элементы массива original.

Элементы с индексов от 0 до n - 1 должны составить первую строку, элементы с индексов от n до 2n - 1 - вторую строку, и так далее, пока все элементы не будут распределены.

Верните получившийся двумерный массив размером m × n. Если составить такую матрицу невозможно, верните пустой 2D-массив.
'''

from typing import List

def construct_2D_array(original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) != m * n:
        return []

    result = []
    for row_index in range(m):
        start = row_index * n
        end = start + n
        result.append(original[start:end])

    return result