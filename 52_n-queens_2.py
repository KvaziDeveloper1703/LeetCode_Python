'''
The N-Queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens can attack each other. This means that no two queens share the same row, column, or diagonal.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
Input: n = 4
Output: 2

Задача о N ферзях заключается в размещении n ферзей на шахматной доске размером n x n так, чтобы ни один ферзь не угрожал другому. Это означает, что никакие два ферзя не должны находиться в одной строке, одном столбце или на одной диагонали.
По заданному целому числу n верните количество различных решений задачи о n ферзях.

Пример:
Ввод: n = 4
Вывод: 2
'''

def total_n_queens(board_size: int) -> int:
    def place_queen_in_row(current_row: int):
        nonlocal solution_count
        if current_row == board_size:
            solution_count += 1
            return

        for current_col in range(board_size):
            if (current_col in occupied_columns or
                (current_row - current_col) in occupied_main_diagonals or
                (current_row + current_col) in occupied_anti_diagonals):
                continue

            occupied_columns.add(current_col)
            occupied_main_diagonals.add(current_row - current_col)
            occupied_anti_diagonals.add(current_row + current_col)

            place_queen_in_row(current_row + 1)

            occupied_columns.remove(current_col)
            occupied_main_diagonals.remove(current_row - current_col)
            occupied_anti_diagonals.remove(current_row + current_col)

    solution_count = 0
    occupied_columns = set()
    occupied_main_diagonals = set()
    occupied_anti_diagonals = set()

    place_queen_in_row(0)
    return solution_count