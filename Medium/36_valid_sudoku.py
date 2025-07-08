'''
You are given a 9 x 9 Sudoku board as a 2D array of characters. 
Your task is to determine if the current board is valid according to the following rules:
    + Each row must contain the digits '1' to '9' without repetition;
    + Each column must contain the digits '1' to '9' without repetition;
    + Each of the nine 3 x 3 sub-boxes must contain the digits '1' to '9' without repetition.

A partially filled Sudoku board is valid if all the filled cells satisfy the above conditions.

Example:
Input: board = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ]
Output: True

Дано игровое поле Судоку размером 9 x 9 в виде двумерного массива символов. 
Ваша задача — определить, является ли текущее состояние поля валидным, исходя из следующих правил:
    + Каждая строка должна содержать цифры от '1' до '9' без повторений;
    + Каждый столбец должен содержать цифры от '1' до '9' без повторений;
    + Каждый из девяти подблоков 3 x 3 должен содержать цифры от '1' до '9' без повторений.

Частично заполненное поле Судоку считается валидным, если все уже заполненные ячейки соответствуют этим условиям.

Пример:
Ввод: board = [ ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ]  
Вывод: True
'''

from typing import List

def is_valid_sudoku(board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            number = board[i][j]
            if number == ".":
                continue

            box_index = (i // 3) * 3 + (j // 3)

            if number in rows[i] or number in columns[j] or number in boxes[box_index]:
                return False

            rows[i].add(number)
            columns[j].add(number)
            boxes[box_index].add(number)

    return True