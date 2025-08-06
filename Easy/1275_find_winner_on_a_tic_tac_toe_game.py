'''
Tic-tac-toe is played by two players, A and B, on a 3 x 3 grid.

The rules are:
    1) Players take turns placing marks in empty squares;
    2) Player A always places 'X', and Player B always places 'O';
    3) Marks are only placed in empty squares — never in filled ones;
    4) The game ends when any row, column, or diagonal contains three identical marks;
    5) The game also ends when all squares are filled;
    6) No moves can be made after the game ends.

Given a 2D integer array moves, where moves[i] = [rowi, coli] represents the position of the i‑th move on the grid.

Return:
    + "A" if player A wins;
    + "B" if player B wins;
    + "Draw" if the game ends with no winner and all squares are filled;
    + "Pending" if the game has not ended and there are still moves left to play.

Examples:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"

Крестики-нолики играют два игрока — A и B — на поле 3 x 3.

Правила:
    1) Игроки ходят по очереди, ставя символы в пустые клетки;
    2) Игрок A всегда ставит 'X', игрок B всегда ставит 'O';
    3) Символы ставятся только в пустые клетки — никогда на занятые;
    4) Игра заканчивается, когда в каком-либо ряду, столбце или диагонали окажутся три одинаковых символа;
    5) Игра также заканчивается, если все клетки заполнены;
    6) После окончания игры ходы больше не делаются.

Дан двумерный массив moves, где moves[i] = [rowi, coli] обозначает позицию i‑го хода на поле.

Верните:
    + "A", если победил игрок A;
    + "B", если победил игрок B;
    + "Draw", если игра закончилась без победителя и поле заполнено;
    + "Pending", если игра ещё не закончилась и остались ходы.

Примеры:
Ввод: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Вывод: "A"

Ввод: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Вывод: "B"
'''

from typing import List

def tictactoe(moves: List[List[int]]) -> str:
    board = [[""] * 3 for _ in range(3)]

    for i, (r, c) in enumerate(moves):
        if i % 2 == 0:
            board[r][c] = "X"
        else:
            board[r][c] = "O"

    def check_winner(player: str) -> bool:
        for row in board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    if check_winner("X"):
        return "A"
    if check_winner("O"):
        return "B"

    return "Draw" if len(moves) == 9 else "Pending"