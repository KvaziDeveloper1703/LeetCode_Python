'''
You are given a 2D grid board representing the current state of Conway's Game of Life, a cellular automaton. Each cell has two possible states:
    + 1 — live;
    + 0 — dead.

Each cell interacts with its eight neighbors (horizontal, vertical, and diagonal), and its next state is determined by the following rules:
    + Underpopulation: Any live cell with fewer than two live neighbors dies;
    + Survival: Any live cell with two or three live neighbors lives on to the next generation;
    + Overpopulation: Any live cell with more than three live neighbors dies;
    + Reproduction: Any dead cell with exactly three live neighbors becomes a live cell.

All cells are updated simultaneously, based on the current state of the grid.

Example:
Input: board = [[0,1,0], 
                [0,0,1], 
                [1,1,1], 
                [0,0,0]
        ]
Output: [   [0,0,0], 
            [1,0,1], 
            [0,1,1], 
            [0,1,0]
    ]

Дана двумерная сетка board, представляющая текущее состояние Игры «Жизнь» Конвея — клеточного автомата. Каждая ячейка может находиться в одном из двух состояний:
    1 — живая клетка;
    0 — мёртвая клетка.

Каждая клетка взаимодействует с восемью соседями (по горизонтали, вертикали и диагонали). Состояние клетки в следующем поколении определяется по следующим правилам:
    + Недостаточная популяция: Любая живая клетка с менее чем двумя живыми соседями умирает;
    + Выживание: Любая живая клетка с двумя или тремя живыми соседями продолжает жить;
    + Перенаселение: Любая живая клетка с более чем тремя живыми соседями умирает;
    + Воспроизводство: Любая мёртвая клетка с ровно тремя живыми соседями становится живой.

Все клетки обновляются одновременно, основываясь на текущем состоянии сетки.

Пример:
Ввод: board = [ [0, 1, 0],  
                [0, 0, 1],  
                [1, 1, 1],  
                [0, 0, 0]
        ]
Вывод: [[0, 0, 0],  
        [1, 0, 1],  
        [0, 1, 1],  
        [0, 1, 0]
    ]
'''

from typing import List

def game_of_life(board: List[List[int]]) -> None:
    number_of_rows = len(board)
    number_of_columns = len(board[0])

    def count_live_neighbors(cell_row: int, cell_column: int) -> int:
        neighbor_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        live_neighbor_count = 0

        for row_offset, column_offset in neighbor_directions:
            neighbor_row = cell_row + row_offset
            neighbor_column = cell_column + column_offset

            if 0 <= neighbor_row < number_of_rows and 0 <= neighbor_column < number_of_columns:
                if abs(board[neighbor_row][neighbor_column]) == 1:
                    live_neighbor_count += 1

        return live_neighbor_count

    for row_index in range(number_of_rows):
        for column_index in range(number_of_columns):
            live_neighbors = count_live_neighbors(row_index, column_index)

            if board[row_index][column_index] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    board[row_index][column_index] = -1
            else:
                if live_neighbors == 3:
                    board[row_index][column_index] = 2

    for row_index in range(number_of_rows):
        for column_index in range(number_of_columns):
            if board[row_index][column_index] > 0:
                board[row_index][column_index] = 1
            else:
                board[row_index][column_index] = 0