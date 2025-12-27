'''
You are given a 0-indexed integer matrix grid of size m × n.

The width of a column is defined as the maximum length of the integers contained in that column.
    - The length of a non-negative integer with len digits is len;
    - The length of a negative integer with len digits is len + 1.

Return an integer array ans of size n, where ans[i] represents the width of the i-th column.

Examples:
Input: grid = [[1], [22], [333]]
Output: [3]

Input: grid = [[-15, 1, 3], [15, 7, 12], [5, 6, -2]]
Output: [3, 1, 2]

Дана 0-индексированная целочисленная матрица grid размера m × n.

Ширина столбца определяется как максимальная длина числа среди всех элементов этого столбца.
    - Длина неотрицательного числа с len цифрами равна len;
    - Длина отрицательного числа с len цифрами равна len + 1.

Верните целочисленный массив ans длины n, где ans[i] - это ширина i-го столбца.

Примеры:
Ввод: grid = [[1], [22], [333]]
Вывод: [3]

Ввод: grid = [[-15, 1, 3], [15, 7, 12], [5, 6, -2]]
Вывод: [3, 1, 2]
'''

from typing import List

def find_column_width(grid: List[List[int]]) -> List[int]:
    number_of_rows = len(grid)
    number_of_columns = len(grid[0])

    column_widths = [0] * number_of_columns

    for column_index in range(number_of_columns):
        for row_index in range(number_of_rows):
            current_number_length = len(str(grid[row_index][column_index]))
            column_widths[column_index] = max(column_widths[column_index], current_number_length)

    return column_widths