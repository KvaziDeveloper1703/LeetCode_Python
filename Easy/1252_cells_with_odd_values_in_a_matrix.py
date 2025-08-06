'''
Given an m x n matrix initially filled with 0s. Also given a 2D array indices, where each element indices[i] = [ri, ci] represents a 0-indexed location in the matrix.

For each indices[i], do the following two operations:
    1) Increment every cell in row ri;
    2) Increment every cell in column ci.

After performing all operations, return the number of cells in the matrix that contain odd values.

Examples:
Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6

Input: m = 2, n = 2, indices = [[1,1],[0,0]]
Output: 0

Дана матрица размером m x n, изначально заполненная нулями. Также дан двумерный массив indices, где каждый элемент indices[i] = [ri, ci] — это индекс строки и столбца.

Для каждого элемента indices[i] нужно выполнить два действия:
    1) Увеличить на 1 все элементы в строке ri.
    2) Увеличить на 1 все элементы в столбце ci.

После выполнения всех операций верните количество ячеек в матрице, содержащих нечётные значения.

Примеры:
Ввод: m = 2, n = 3, indices = [[0,1],[1,1]]
Вывод: 6

Ввод: m = 2, n = 2, indices = [[1,1],[0,0]]
Вывод: 0
'''

from typing import List

def odd_cells(m: int, n: int, indices: List[List[int]]) -> int:
    rows = [0] * m
    columns = [0] * n

    for r, c in indices:
        rows[r] += 1
        columns[c] += 1

    odd_count = 0
    for i in range(m):
        for j in range(n):
            if (rows[i] + columns[j]) % 2 == 1:
                odd_count += 1

    return odd_count