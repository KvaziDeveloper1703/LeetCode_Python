'''
You are given a 0-indexed integer matrix matrix of size m × n.
Create a new 0-indexed matrix called answer and initially copy all elements of matrix into it.
For every element in answer that is equal to -1, replace it with the maximum value in the same column.
Return the resulting matrix answer.

Examples:
Input: matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
Output: [[1,2,9],[4,8,6],[7,8,9]]

Input: matrix = [[3,-1],[5,2]]
Output: [[3,2],[5,2]]

Дана 0-индексированная целочисленная матрица matrix размера m × n.
Создайте новую 0-индексированную матрицу answer и сначала скопируйте в неё все элементы из matrix.
Затем каждый элемент answer, равный -1, замените на максимальное значение в том же столбце.
Верните итоговую матрицу answer.

Примеры:
Ввод: matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
Вывод: [[1,2,9],[4,8,6],[7,8,9]]

Ввод: matrix = [[3,-1],[5,2]]
Вывод: [[3,2],[5,2]]
'''

from typing import List

def modified_matrix(matrix: List[List[int]]) -> List[List[int]]:
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    column_maximums = []

    for column_index in range(number_of_columns):
        maximum_in_column = matrix[0][column_index]
        for row_index in range(1, number_of_rows):
            if matrix[row_index][column_index] > maximum_in_column:
                maximum_in_column = matrix[row_index][column_index]
        column_maximums.append(maximum_in_column)

    for row_index in range(number_of_rows):
        for column_index in range(number_of_columns):
            if matrix[row_index][column_index] == -1:
                matrix[row_index][column_index] = column_maximums[column_index]

    return matrix