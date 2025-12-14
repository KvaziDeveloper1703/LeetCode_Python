'''
A square matrix is called an X-Matrix if it satisfies both of the following conditions:
    - All elements on the main diagonal and the secondary diagonal are non-zero;
    - All elements not on these diagonals are equal to 0.

You are given a 2D integer array grid of size n × n representing a square matrix.
Return True if grid is an X-Matrix. Otherwise, return False.

Examples:
Input: grid = [ [2, 0, 0, 1],
                [0, 3, 1, 0],
                [0, 5, 2, 0],
                [4, 0, 0, 2]
            ]
Output: True

Input: grid = [ [5, 7, 0],
                [0, 3, 1],
                [0, 5, 0]
            ]
Output: False
 
Квадратная матрица называется X-матрицей, если выполняются оба следующих условия:
    - Все элементы на главной диагонали и побочной диагонали являются ненулевыми;
    - Все элементы, не лежащие на диагоналях, равны 0.

Дан двумерный целочисленный массив grid размером n × n, представляющий квадратную матрицу.
Верните True, если grid является X-матрицей, иначе верните False.

Примеры:
Ввод: grid = [  [2, 0, 0, 1],
                [0, 3, 1, 0],
                [0, 5, 2, 0],
                [4, 0, 0, 2]
            ]
Вывод: True

Ввод: grid = [  [5, 7, 0],
                [0, 3, 1],
                [0, 5, 0]
            ]
Вывод: False
'''

from typing import List

def check_x_matrix(grid: List[List[int]]) -> bool:
    n = len(grid)

    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                if grid[i][j] == 0:
                    return False
            else:
                if grid[i][j] != 0:
                    return False
    return True