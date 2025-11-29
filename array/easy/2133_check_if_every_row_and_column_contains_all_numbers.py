'''
An n × n matrix is considered valid if every row and every column contains all the integers from 1 to n, each appearing exactly once.

Given an n × n integer matrix matrix, return True if it is valid. Otherwise, return False.

Examples:
Input: matrix = [[1,2,3],
                 [3,1,2],
                 [2,3,1]
            ]
Output: True

Input: matrix = [[1,1,1],
                 [1,2,3],
                 [1,2,3]
            ]
Output: False

Матрица размера n × n считается валидной, если каждая строка и каждый столбец содержат все числа от 1 до n, и каждое из них встречается ровно один раз.

Дана целочисленная матрица matrix размером n × n. Верните True, если матрица валидна. Иначе верните False.

Примеры:
Ввод: matrix = [[1,2,3],
                [3,1,2],
                [2,3,1]
            ]
Вывод: True

Ввод: matrix = [[1,1,1],
                [1,2,3],
                [1,2,3]
            ]
Вывод: False
'''

from typing import List

def check_valid(matrix: List[List[int]]) -> bool:
    matrix_size = len(matrix)
    required_values = set(range(1, matrix_size + 1))

    for row_values in matrix:
        if set(row_values) != required_values:
            return False

    for column_index in range(matrix_size):
        column_values_set = {matrix[row_index][column_index] for row_index in range(matrix_size)}
        if column_values_set != required_values:
            return False

    return True