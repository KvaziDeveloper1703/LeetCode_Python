'''
You are given a 9x9 Sudoku board represented as a 2D array board.
Your task is to fill in the empty cells to solve the puzzle.

A valid Sudoku solution must satisfy all of the following rules:
    + Each row must contain the digits 1-9 with no repetition;
    + Each column must contain the digits 1-9 with no repetition;
    + Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 with no repetition.

You must solve the puzzle using backtracking or another valid approach that explores possible solutions, and you must modify the board in-place.

Вам дана доска Судоку размером 9x9, представленная в виде двумерного массива board.
Ваша задача — заполнить пустые ячейки так, чтобы получилось корректное решение.

Правильное решение Судоку должно соответствовать следующим правилам:
    + В каждой строке должны быть цифры от 1 до 9 без повторений;
    + В каждом столбце должны быть цифры от 1 до 9 без повторений;
    + В каждом из девяти квадратов 3x3 должны быть цифры от 1 до 9 без повторений.

Вы должны решить задачу, используя метод перебора (backtracking) или другой подход, проверяющий возможные решения. Решение должно модифицировать доску на месте.
'''

from typing import List

def solve_sudoku(board: List[List[str]]) -> None:

    def is_valid(row: int, column: int, digit: str) -> bool:
        for i in range(9):
            if board[row][i] == digit:
                return False
            if board[i][column] == digit:
                return False
            start_row = 3 * (row // 3)
            start_column = 3 * (column // 3)
            if board[start_row + i // 3][start_column + i % 3] == digit:
                return False
        return True
    
    def solve_cell() -> bool:
        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    for digit in map(str, range(1, 10)):
                        if is_valid(row, column, digit):
                            board[row][column] = digit
                            if solve_cell():
                                return True
                            board[row][column] = '.'
                    return False
        return True
    
    solve_cell()