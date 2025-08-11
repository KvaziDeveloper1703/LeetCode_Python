'''
Given an m x n matrix of integers called matrix and an integer target.

This matrix has the following properties:
    + Integers in each row are sorted in ascending order from left to right;
    + Integers in each column are sorted in ascending order from top to bottom.

Write an efficient algorithm that searches for target in matrix.

Return True if target is found, otherwise return False.

Examples:
Input: matrix = [   [ 1,  4,  7, 11, 15],
                    [ 2,  5,  8, 12, 19],
                    [ 3,  6,  9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30]
            ], target = 5
Output: True

Input: matrix = [   [ 1,  4,  7, 11, 15],
                    [ 2,  5,  8, 12, 19],
                    [ 3,  6,  9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30]
            ], target = 20
Output: False

Дан двумерный массив целых чисел matrix размером m x n и целое число target.

У этого массива есть следующие свойства:
    + Целые числа в каждой строке отсортированы по возрастанию слева направо;
    + Целые числа в каждом столбце отсортированы по возрастанию сверху вниз.

Нужно написать эффективный алгоритм, который проверит, содержится ли значение target в массиве matrix.

Если содержится — вернуть True, иначе — False.

Примеры:
Ввод: matrix = [[ 1,  4,  7, 11, 15],
                [ 2,  5,  8, 12, 19],
                [ 3,  6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
        ], target = 5
Вывод: True

Ввод: matrix = [[ 1,  4,  7, 11, 15],
                [ 2,  5,  8, 12, 19],
                [ 3,  6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
        ], target = 20
Вывод: False
'''

from typing import List

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows, columns = len(matrix), len(matrix[0])
    row, column = 0, columns - 1

    while row < rows and column >= 0:
        current = matrix[row][column]
        if current == target:
            return True
        elif current > target:
            column -= 1
        else:
            row += 1

    return False