'''
In MATLAB, there’s a convenient function called reshape that can transform an m x n matrix into a new matrix of size r x c, while keeping all its elements in their original row-wise order.

Your task is to implement a similar function:
    + You’re given:
        + an m x n matrix mat,
        + two integers r and c representing the desired number of rows and columns for the new matrix.

    + The function should:
        + Reshape mat into a r x c matrix that contains all the elements of mat in the same row-wise order (left to right, top to bottom).
        + If the reshape operation is possible (i.e., if m * n == r * c), return the new reshaped matrix.
        + Otherwise, return the original matrix unchanged.

Examples:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

В MATLAB есть удобная функция reshape, которая позволяет преобразовать матрицу размером m x n в новую матрицу размером r x c, сохранив все элементы в исходном порядке обхода по строкам.

Ваша задача — реализовать аналогичную функцию:
    + Вам даны:
        + матрица mat размером m x n,
        + два целых числа r и c, обозначающих желаемое количество строк и столбцов в новой матрице.

    + Функция должна:
        + Преобразовать mat в матрицу размером r x c, содержащую все элементы исходной матрицы в том же порядке обхода по строкам (слева направо, сверху вниз).
        + Если операция изменения формы возможна (то есть если m * n == r * c), вернуть новую преобразованную матрицу.
        + В противном случае вернуть исходную матрицу без изменений.

Примеры:
Ввод: mat = [[1,2],[3,4]], r = 1, c = 4
Вывод: [[1,2,3,4]]

Ввод: mat = [[1,2],[3,4]], r = 2, c = 4
Вывод: [[1,2],[3,4]]
'''

from typing import List

def matrix_reshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])

    if m * n != r * c:
        return mat

    flat = [num for row in mat for num in row]

    reshaped = []
    for i in range(0, len(flat), c):
        reshaped.append(flat[i:i + c])

    return reshaped