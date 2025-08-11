'''
You are given a 2D integer matrix matrix. You need to handle multiple queries of the following type:
Calculate the sum of the elements in the submatrix defined by the top-left corner and the bottom-right corner.

Implement the class NumMatrix with the following methods:
    + NumMatrix(int[][] matrix): Initializes the object with the given 2D integer matrix.
    + int sumRegion(int row_1, int column_1, int row_2, int column_2): Returns the sum of the elements within the rectangle from (row_1, column_1) to (row_2, column_2), inclusive.

Requirement: The sumRegion method must run in O(1) time complexity.

Example:
Input: ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"], [[[[3, 0, 1, 4, 2], 
                                                                [5, 6, 3, 2, 1], 
                                                                [1, 2, 0, 1, 5], 
                                                                [4, 1, 0, 1, 7], 
                                                                [1, 0, 3, 0, 5]]], 
                                                                [2, 1, 4, 3], 
                                                                [1, 1, 2, 2], 
                                                                [1, 2, 2, 4]]
Output: [null, 8, 11, 12]

Дан двумерный массив matrix. Необходимо обрабатывать несколько запросов следующего типа:
Вычислить сумму элементов в подматрице, ограниченной прямоугольником с верхним левым углом в точке (row_1, column_1) и нижним правым углом в точке (row_2, column_2).

Реализуйте класс NumMatrix с двумя методами:
    + NumMatrix(int[][] matrix): конструктор, инициализирующий объект переданной матрицей.
    + int sumRegion(int row_1, int column_1, int row_2, int column_2): возвращает сумму всех элементов в прямоугольной области от (row_1, column_1) до (row_2, column_2) включительно.

Требование: метод sumRegion должен работать за O(1) времени — то есть, очень быстро, независимо от размера подматрицы.

Пример:
Ввод: ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"], [[[ [3, 0, 1, 4, 2], 
                                                                [5, 6, 3, 2, 1], 
                                                                [1, 2, 0, 1, 5], 
                                                                [4, 1, 0, 1, 7], 
                                                                [1, 0, 3, 0, 5]]], 
                                                                [2, 1, 4, 3], 
                                                                [1, 1, 2, 2], 
                                                                [1, 2, 2, 4]]
Вывод: [null, 8, 11, 12] 
'''

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = []
            return

        rows, columns = len(matrix), len(matrix[0])
        self.prefix = []

        for i in range(rows + 1):
            row = []
            for j in range(columns + 1):
                row.append(0)
            self.prefix.append(row)

        for i in range(rows):
            for j in range(columns):
                self.prefix[i+1][j+1] = (matrix[i][j]
                                         + self.prefix[i][j+1]
                                         + self.prefix[i+1][j]
                                         - self.prefix[i][j])

    def sumRegion(self, row_1: int, column_1: int, row_2: int, column_2: int) -> int:
        return (self.prefix[row_2+1][column_2+1] - self.prefix[row_1][column_2+1] - self.prefix[row_2+1][column_1] + self.prefix[row_1][column_1])