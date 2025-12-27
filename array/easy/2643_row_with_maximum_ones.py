'''
You are given an m × n binary matrix mat.

Find the 0-indexed row that contains the maximum number of 1s, and determine how many 1s are in that row.

If multiple rows contain the same maximum number of 1s`, choose the row with the smallest row index.

Return an array of two integers:
    - the index of the selected row,
    - the number of 1s in that row.

Examples:
Input: mat = [[0, 1], [1, 0]]
Output: [0, 1]

Input: mat = [[0, 0, 0], [0, 1, 1]]
Output: [1, 2]

Дана бинарная матрица mat размера m × n.

Найдите 0-индексированную строку, которая содержит наибольшее количество единиц (1), а также количество этих единиц.

Если несколько строк содержат одинаковое максимальное количество единиц, выберите строку с наименьшим индексом.

Верните массив из двух целых чисел:
    - индекс выбранной строки,
    - количество единиц в этой строке.

Примеры:
Ввод: mat = [[0, 1], [1, 0]]
Вывод: [0, 1]

Ввод: mat = [[0, 0, 0], [0, 1, 1]]
Вывод: [1, 2]
'''

from typing import List

def row_and_maximum_ones(mat: List[List[int]]) -> List[int]:
    max_number_of_ones = 0
    index_of_row_with_max_ones = 0

    for row_index in range(len(mat)):
        current_number_of_ones = sum(mat[row_index])

        if current_number_of_ones > max_number_of_ones:
            max_number_of_ones = current_number_of_ones
            index_of_row_with_max_ones = row_index

    return [index_of_row_with_max_ones, max_number_of_ones]