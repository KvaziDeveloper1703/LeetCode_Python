'''
You are given an n × n 2D array grid containing distinct integers in the range [0, n² − 1].

Implement the class NeighborSum:
    - NeighborSum(int[][] grid) initializes the object with the given grid;
    - int adjacentSum(int value) returns the sum of all adjacent neighbors of value in the grid;
    - int diagonalSum(int value) returns the sum of all diagonal neighbors of value in the grid.

Examples:
Input: ["NeighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"], [[[[0,1,2],[3,4,5],[6,7,8]]],[1],[4],[4],[8]]
Output: [null, 6, 16, 16, 4]

Input: ["NeighborSum", "adjacentSum", "diagonalSum"], [[[[1,2,0,3],[4,7,15,6],[8,9,10,11],[12,13,14,5]]],[15],[9]]
Output: [null, 23, 45]

Дана квадратная матрица grid размера n × n, содержащая различные числа в диапазоне [0, n² - 1].

Нужно реализовать класс NeighborSum:
    - NeighborSum(int[][] grid) создаёт объект и сохраняет матрицу;
    - int adjacentSum(int value) возвращает сумму соседних по стороне элементов числа value;
    - int diagonalSum(int value) возвращает сумму диагональных соседей числа value.

Примеры:
Ввод: ["NeighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"], [[[[0,1,2],[3,4,5],[6,7,8]]],[1],[4],[4],[8]]
Вывод: [null, 6, 16, 16, 4]

Ввод: ["NeighborSum", "adjacentSum", "diagonalSum"], [[[[1,2,0,3],[4,7,15,6],[8,9,10,11],[12,13,14,5]]],[15],[9]]
Вывод: [null, 23, 45]
'''

from typing import List

class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.size = len(grid)
        self.position_by_value = {}

        for row in range(self.size):
            for column in range(self.size):
                self.position_by_value[grid[row][column]] = (row, column)

    def adjacentSum(self, value: int) -> int:
        row, column = self.position_by_value[value]
        total_sum = 0

        for row_shift, column_shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = row + row_shift
            new_column = column + column_shift
            if 0 <= new_row < self.size and 0 <= new_column < self.size:
                total_sum += self.grid[new_row][new_column]

        return total_sum

    def diagonalSum(self, value: int) -> int:
        row, column = self.position_by_value[value]
        total_sum = 0

        for row_shift, column_shift in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row = row + row_shift
            new_column = column + column_shift
            if 0 <= new_row < self.size and 0 <= new_column < self.size:
                total_sum += self.grid[new_row][new_column]

        return total_sum