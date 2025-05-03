'''
The N-Queens problem is to place n queens on an n x n chessboard so that no two queens threaten each other. That is, no two queens share the same row, column, or diagonal.
Given an integer n, return all the distinct solutions to the n-queens puzzle. You can return the answers in any order.
Each solution should be represented as an array of strings, where:
+ 'Q' denotes a queen,
+ '.' denotes an empty space.

Each string represents a row of the chessboard.

Example:
Input: n = 4
Output: [  [".Q..",
            "...Q",
            "Q...",
            "..Q."],

           ["..Q.",
            "Q...",
            "...Q",
            ".Q.."]
    ]

Задача N ферзей заключается в размещении n ферзей на шахматной доске размером n x n так, чтобы ни один ферзь не угрожал другому. То есть, никакие два ферзя не должны находиться на одной строке, одном столбце или одной диагонали.
Дан целочисленный параметр n. Верните все различные решения задачи о n ферзях. Ответ может быть возвращён в любом порядке.
Каждое решение должно быть представлено в виде массива строк, где:
+ 'Q' обозначает ферзя,
+ '.' обозначает пустую клетку.

Каждая строка соответствует одному ряду шахматной доски.

Пример:
Ввод: n = 4
Вывод: [   [".Q..",
            "...Q",
            "Q...",
            "..Q."],

           ["..Q.",
            "Q...",
            "...Q",
            ".Q.."]
    ]
'''

from typing import List

def solve_n_queens(board_size: int) -> List[List[str]]:
    def place_queen_in_row(current_row: int):
        if current_row == board_size:
            formatted_board = ["".join(row) for row in chessboard]
            all_valid_solutions.append(formatted_board)
            return

        for current_col in range(board_size):
            if (current_col in occupied_columns or
                (current_row - current_col) in occupied_main_diagonals or
                (current_row + current_col) in occupied_anti_diagonals):
                continue

            chessboard[current_row][current_col] = 'Q'
            occupied_columns.add(current_col)
            occupied_main_diagonals.add(current_row - current_col)
            occupied_anti_diagonals.add(current_row + current_col)

            place_queen_in_row(current_row + 1)
            chessboard[current_row][current_col] = '.'
            occupied_columns.remove(current_col)
            occupied_main_diagonals.remove(current_row - current_col)
            occupied_anti_diagonals.remove(current_row + current_col)

    all_valid_solutions = []
    chessboard = [['.'] * board_size for _ in range(board_size)]
    occupied_columns = set()
    occupied_main_diagonals = set()
    occupied_anti_diagonals = set()

    place_queen_in_row(0)
    return all_valid_solutions