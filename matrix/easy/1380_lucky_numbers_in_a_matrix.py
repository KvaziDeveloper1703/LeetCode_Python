'''
Given an m x n matrix of distinct numbers.

Return all lucky numbers in the matrix in any order.

A lucky number is an element that is:
    + the smallest in its row, and
    + the largest in its column.

Examples:
Input:  matrix = [  [3,7,8],
                    [9,11,13],
                    [15,16,17]
            ]
Output: [15]

Input:  matrix = [  [1,10,4,2],
                    [9,3,8,7],
                    [15,16,17,12]
            ]
Output: [12]

Вам дана матрица размером m x n, содержащая различные числа.

Необходимо вернуть все счастливые числа в матрице в любом порядке.

Счастливое число — это элемент, который одновременно:
    + является наименьшим в своей строке, и
    + является наибольшим в своём столбце.

Примеры:
Ввод:  matrix = [   [3,7,8],
                    [9,11,13],
                    [15,16,17]
            ]
Вывод: [15]

Ввод:  matrix = [   [1,10,4,2],
                    [9,3,8,7],
                    [15,16,17,12]
            ]
Вывод: [12]
'''

from typing import List

def lucky_numbers(matrix: List[List[int]]) -> List[int]:
    min_values_in_rows = {min(row) for row in matrix}
    max_values_in_columns = {
        max(matrix[row_index][column_index] for row_index in range(len(matrix)))
        for column_index in range(len(matrix[0]))
    }
    return list(min_values_in_rows & max_values_in_columns)