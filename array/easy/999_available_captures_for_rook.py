'''
Given an 8 × 8 matrix representing a chessboard.

The board contains:
    + Exactly one white rook represented by 'R'
    + Some number of white bishops represented by 'B'
    + Some number of black pawns represented by 'p'
    + Empty squares represented by '.'

The rook can move any number of squares horizontally or vertically (left, right, up, down) until it hits another piece or the edge of the board.

The rook can attack a pawn if it can move to the pawn's square in one straight move without jumping over any piece.

Return the number of pawns the rook is attacking.

Examples:
Input:
board = [[".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".","R",".",".",".","p"],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."]]
Output: 3

Input:
board = [[".",".",".",".",".",".",".","."],
         [".","p","p","p","p","p",".","."],
         [".","p","p","B","p","p",".","."],
         [".","p","B","R","B","p",".","."],
         [".","p","p","B","p","p",".","."],
         [".","p","p","p","p","p",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."]]
Output: 0

Дана шахматная доска размером 8 × 8, представленная в виде матрицы.

На доске:
    + Ровно одна белая ладья, обозначенная символом 'R'
    + Несколько белых слонов ('B')
    + Несколько чёрных пешек ('p')
    + Пустые клетки обозначены точками '.'

Ладья может двигаться на любое количество клеток по вертикали или горизонтали (вверх, вниз, влево, вправо), пока не встретит другую фигуру или край доски.

Ладья может атаковать пешку, если она может добраться до неё одним ходом без прыжков через другие фигуры.

Верните количество пешек, которые может атаковать ладья.

Примеры:
Ввод:
board = [[".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".","R",".",".",".","p"],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."]]
Вывод: 3

Ввод:
board = [[".",".",".",".",".",".",".","."],
         [".","p","p","p","p","p",".","."],
         [".","p","p","B","p","p",".","."],
         [".","p","B","R","B","p",".","."],
         [".","p","p","B","p","p",".","."],
         [".","p","p","p","p","p",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."]]
Вывод: 0
'''

from typing import List

def number_of_rook_captures(board: List[List[str]]) -> int:
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                rook_x, rook_y = i, j
                break

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    captures = 0

    for dx, dy in directions:
        x, y = rook_x, rook_y
        while 0 <= x + dx < 8 and 0 <= y + dy < 8:
            x += dx
            y += dy
            if board[x][y] == 'B':
                break
            if board[x][y] == 'p':
                captures += 1
                break

    return captures