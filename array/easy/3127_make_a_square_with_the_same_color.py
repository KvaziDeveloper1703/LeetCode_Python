'''
You are given a 3 × 3 matrix grid containing only the characters 'B' and 'W'. 'W' represents white, and 'B' represents black.

You are allowed to change the color of at most one cell in the grid so that there exists at least one 2 × 2 square in which all 4 cells have the same color.

Return True if it is possible to create such a 2 × 2 square, otherwise return False.

Examples:
Input: grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
Output: True

Input: grid = [["B","W","B"],["W","B","W"],["B","W","B"]]
Output: False

Дана матрица grid размера 3 × 3, содержащая только символы 'B' и 'W'. 'W' означает белый цвет, а 'B' - чёрный цвет.

Разрешается изменить цвет максимум одной клетки, чтобы в матрице появилась хотя бы одна область 2 × 2, в которой все 4 клетки одного и того же цвета.

Верни True, если это возможно, иначе верни False.

Примеры:
Ввод: grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
Вывод: True

Ввод: grid = [["B","W","B"],["W","B","W"],["B","W","B"]]
Вывод: False
'''

from typing import List

def can_make_square(grid: List[List[str]]) -> bool:
    for row in range(2):
        for column in range(2):
            square_cells = [
                grid[row][column],
                grid[row][column + 1],
                grid[row + 1][column],
                grid[row + 1][column + 1]
            ]

            black_count = square_cells.count("B")
            white_count = square_cells.count("W")

            if black_count >= 3 or white_count >= 3:
                return True

    return False