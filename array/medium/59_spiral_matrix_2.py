'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n² in spiral order, starting from the top-left corner and moving clockwise.

Example:
Input: n = 3
Output: [   [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
    ]

Дано положительное целое число n. Сгенерируйте квадратную матрицу размером n x n, заполненную числами от 1 до n² в спиральном порядке, начиная с левого верхнего угла и двигаясь по часовой стрелке.

Пример:
Ввод: n = 3
Вывод: [[1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ]
'''

from typing import List

def generate_matrix(matrix_size: int) -> List[List[int]]:
    spiral_matrix = [[0] * matrix_size for _ in range(matrix_size)]
    current_value = 1
    left_boundary = 0
    right_boundary = matrix_size - 1
    top_boundary = 0
    bottom_boundary = matrix_size - 1

    while left_boundary <= right_boundary and top_boundary <= bottom_boundary:
        for column in range(left_boundary, right_boundary + 1):
            spiral_matrix[top_boundary][column] = current_value
            current_value += 1
        top_boundary += 1

        for row in range(top_boundary, bottom_boundary + 1):
            spiral_matrix[row][right_boundary] = current_value
            current_value += 1
        right_boundary -= 1

        if top_boundary <= bottom_boundary:
            for column in range(right_boundary, left_boundary - 1, -1):
                spiral_matrix[bottom_boundary][column] = current_value
                current_value += 1
            bottom_boundary -= 1

        if left_boundary <= right_boundary:
            for row in range(bottom_boundary, top_boundary - 1, -1):
                spiral_matrix[row][left_boundary] = current_value
                current_value += 1
            left_boundary += 1

    return spiral_matrix