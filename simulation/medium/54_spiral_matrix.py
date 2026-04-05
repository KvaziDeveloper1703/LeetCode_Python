'''
You are given an m x n 2D array matrix. Your task is to return all elements of the matrix in spiral order, starting from the top-left corner and moving clockwise.

Examples:
Input: matrix = [   [1,2,3],
                    [4,5,6],
                    [7,8,9]
            ]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [   [1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12]
            ]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Дана двумерная матрица размером m x n. Ваша задача — вернуть все элементы этой матрицы в спиральном порядке, начиная с верхнего левого угла и двигаясь по часовой стрелке.

Примеры:
Ввод: matrix = [[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ]
Вывод: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Ввод: matrix = [[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 10, 11, 12]
            ]
Вывод: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
'''

from typing import List

def spiral_order(matrix: List[List[int]]) -> List[int]:
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result