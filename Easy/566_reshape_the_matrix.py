'''
In MATLAB, there is a handy function called reshape that can reshape an m x n matrix into a new one with a different size r x c while keeping its original data in row-traversing order.

Given:
    + an m x n matrix mat,
    + two integers r and c representing the desired number of rows and columns of the new matrix,

write a function to reshape the matrix.

    + The reshaped matrix should contain all the elements of the original matrix in the same row-traversing order (left to right, top to bottom).
    + If the reshape operation is possible (i.e., m * n == r * c), return the new reshaped matrix.
    + Otherwise, return the original matrix.

Examples:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

В MATLAB есть удобная функция reshape, которая может преобразовать матрицу размера m x n в новую матрицу размера r x c, сохраняя исходные данные в порядке обхода по строкам.

Вам дано:
    + матрица mat размером m x n,
    + два целых числа r и c, обозначающих желаемое количество строк и столбцов новой матрицы.

Необходимо написать функцию для преобразования матрицы.

    + Новая матрица должна содержать все элементы исходной матрицы в том же порядке обхода по строкам (слева направо, сверху вниз).
    + Если операция изменения формы возможна (т.е. если m * n == r * c), вернуть новую матрицу.
    + В противном случае вернуть исходную матрицу.

Примеры:
Ввод: mat = [[1,2],[3,4]], r = 1, c = 4
Вывод: [[1,2,3,4]]

Ввод: mat = [[1,2],[3,4]], r = 2, c = 4
Вывод: [[1,2],[3,4]]
'''

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        flat = [num for row in mat for num in row]

        reshaped = []
        for i in range(0, len(flat), c):
            reshaped.append(flat[i:i + c])

        return reshaped