'''
You are given an m x n matrix board consisting of the characters 'X' and 'O'.
Your task is to capture all regions that are completely surrounded by 'X'.

Definitions:
+ Connected: A cell is connected to its adjacent cells (up, down, left, right);
+ Region: A group of 'O' cells that are connected together;
+ Surrounded: A region is considered surrounded if none of its cells are on the edge of the board, and it is completely enclosed by 'X's.

To capture a surrounded region, you must replace all 'O's in it with 'X's directly in the original board.
You do not return anything — modify the board in-place.

Example:
Input: board = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]
            ]
Output: [   
["X","X","X","X"],
["X","X","X","X"],
["X","X","X","X"],
["X","O","X","X"]
]

Дана матрица m x n под названием board, состоящая из символов 'X' и 'O'.
Необходимо захватить все области, полностью окружённые символами 'X', изменив 'O' на 'X' на месте.

Определения:
+ Связь: Ячейки считаются связанными, если они соседствуют по вертикали или горизонтали;
+ Область: Группа связанных между собой ячеек 'O';
+ Окружение: Область считается окружённой, если ни одна её ячейка не находится на границе матрицы, и она со всех сторон окружена 'X'.

Чтобы захватить область, нужно заменить все 'O' в ней на 'X' в самой матрице.
Возвращать ничего не нужно — изменения происходят на месте.

Пример:
Ввод: board = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]
            ]

Вывод: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
'''

from typing import List

def solve(board: List[List[str]]) -> None:
    if not board or not board[0]:
        return
    total_rows = len(board)
    total_columns = len(board[0])
    def depth_first_search(row: int, column: int):
        if (row < 0 or row >= total_rows or
            column < 0 or column >= total_columns or
            board[row][column] != 'O'):
            return
        board[row][column] = 'S'  # Временная метка — safe
        depth_first_search(row + 1, column)
        depth_first_search(row - 1, column)
        depth_first_search(row, column + 1)
        depth_first_search(row, column - 1)
    for row in range(total_rows):
        if board[row][0] == 'O':
            depth_first_search(row, 0)
        if board[row][total_columns - 1] == 'O':
            depth_first_search(row, total_columns - 1)
    for column in range(total_columns):
        if board[0][column] == 'O':
            depth_first_search(0, column)
        if board[total_rows - 1][column] == 'O':
            depth_first_search(total_rows - 1, column)
    for row in range(total_rows):
        for column in range(total_columns):
            if board[row][column] == 'O':
                board[row][column] = 'X'
            elif board[row][column] == 'S':
                board[row][column] = 'O'