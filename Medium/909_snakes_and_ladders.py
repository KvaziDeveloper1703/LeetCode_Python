'''
Given an n x n integer matrix board representing a Snakes and Ladders game, labeled in a Boustrophedon style (zigzag), starting from the bottom-left cell.
You start on square 1. On each turn:
    + Roll a 6-sided die and choose a square next in [current + 1, min(current + 6, n²)];
    + If next has a snake or ladder (board[r][c] != -1), move to that destination;
    + Only follow one snake or ladder per turn.

Return the minimum number of moves to reach square n². If it’s not possible, return -1.

Дан квадратный массив board размером n x n, представляющий игровое поле "Змеи и лестницы", заполненный по бустрофедонному (зигзагообразному) стилю — нумерация начинается снизу слева и чередуется по строкам: слева направо, затем справа налево и так далее.
Ты начинаешь на клетке 1, и в каждом ходе:
    + Бросаешь стандартный кубик (1–6), и выбираешь клетку next в диапазоне [current + 1, min(current + 6, n²)];
    + Если на next есть змея или лестница (board[r][c] != -1), то ты попадаешь на указанную клетку;
    + Если на новой клетке снова змея/лестница — игнорируешь.

Нужно добраться до клетки с номером n² за минимальное число бросков кубика. Если это невозможно — верни -1.
'''

from typing import List
from collections import deque

def snakes_and_ladders(board: List[List[int]]) -> int:
    board_size = len(board)

    def get_board_coordinates(square_number: int) -> (int, int):
        rows_count_from_bottom = (square_number - 1) // board_size
        column_position_in_row = (square_number - 1) % board_size
        actual_row_index = board_size - 1 - rows_count_from_bottom
        
        if rows_count_from_bottom % 2 == 1:
            actual_column_index = board_size - 1 - column_position_in_row
        else:
            actual_column_index = column_position_in_row
        
        return actual_row_index, actual_column_index

    visited_squares = set()
    bfs_queue = deque([(1, 0)])
    
    while bfs_queue:
        current_square_number, move_count = bfs_queue.popleft()
        
        if current_square_number == board_size * board_size:
            return move_count
        
        for next_square_candidate in range(
            current_square_number + 1, 
            min(current_square_number + 6, board_size * board_size) + 1
        ):
            row_index, column_index = get_board_coordinates(next_square_candidate)
            board_cell_value = board[row_index][column_index]
            final_destination_square = (
                board_cell_value if board_cell_value != -1 else next_square_candidate
            )
            if final_destination_square not in visited_squares:
                visited_squares.add(final_destination_square)
                bfs_queue.append((final_destination_square, move_count + 1))
    
    return -1