'''
You are given an m × n integer matrix mat, where the rows are 0-indexed, and an integer k.

The following operation is performed k times:
    - Even-indexed rows (rows with indices 0, 2, 4, …) are cyclically shifted to the left by one position;
    - Odd-indexed rows (rows with indices 1, 3, 5, …) are cyclically shifted to the right by one position.

After performing the operation k times, determine whether the final matrix is identical to the original matrix.

Return true if the matrix remains unchanged after k steps, and false otherwise.

Examples:
Input: mat = [  [1,2,3],
                [4,5,6],
                [7,8,9]
            ], k = 4
Output: False

Input: mat = [  [1,2,1,2],
                [5,5,5,5],
                [6,3,6,3]
            ], k = 2
Output: True

Дана целочисленная матрица размером m × n mat, в которой строки пронумерованы с нуля, а также целое число k.

Следующая операция выполняется k раз:
    - Строки с чётными индексами (0, 2, 4, …) циклически сдвигаются влево на одну позицию;
    - Строки с нечётными индексами (1, 3, 5, …) циклически сдвигаются вправо на одну позицию.

После выполнения операции k раз необходимо определить, совпадает ли итоговая матрица с исходной.

Верните true, если матрица после всех сдвигов не изменилась, и false в противном случае.

Примеры:

Ввод: mat = [   [1,2,3],
                [4,5,6],
                [7,8,9]
        ], k = 4
Вывод: False

Ввод: mat = [   [1,2,1,2],
                [5,5,5,5],
                [6,3,6,3]
        ], k = 2
Вывод: True
'''

from typing import List

def are_similar(mat: List[List[int]], k: int) -> bool:
    number_of_columns = len(mat[0])
    effective_shifts = k % number_of_columns

    if effective_shifts == 0:
        return True

    for row_index in range(len(mat)):
        original_row = mat[row_index]

        if row_index % 2 == 0:
            shifted_row = original_row[effective_shifts:] + original_row[:effective_shifts]
        else:
            shifted_row = original_row[-effective_shifts:] + original_row[:-effective_shifts]

        if shifted_row != original_row:
            return False

    return True