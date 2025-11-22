'''
You are given two n × n binary matrices: mat and target.

Return True if you can make mat equal to target by rotating mat by 90 degrees any number of times (0°, 90°, 180°, or 270°). Otherwise, return False.

Examples:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: True

Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: False

Даны две бинарные матрицы размера n × n: mat и target.

Верните True, если можно сделать mat равной target, поворачивая матрицу mat на 90 градусов любое количество раз (0°, 90°, 180°, 270°). В противном случае верните False.

Примеры:
Ввод: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Вывод: True

Ввод: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Вывод: False
'''

from typing import List

def find_rotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    def rotate_90(matrix):
        n = len(matrix)
        rotated_matrix = [[0] * n for _ in range(n)]
        for row in range(n):
            for column in range(n):
                rotated_matrix[column][n - row - 1] = matrix[row][column]
        return rotated_matrix

    current_matrix = mat
    for _ in range(4):
        if current_matrix == target:
            return True
        current_matrix = rotate_90(current_matrix)

    return False