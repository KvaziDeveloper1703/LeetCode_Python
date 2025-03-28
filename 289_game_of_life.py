'''
You are given a 2D grid board representing the current state of Conway's Game of Life, a cellular automaton. Each cell has two possible states:
+ 1 — live
+ 0 — dead

Each cell interacts with its eight neighbors (horizontal, vertical, and diagonal), and its next state is determined by the following rules:
+ Underpopulation: Any live cell with fewer than two live neighbors dies.
+ Survival: Any live cell with two or three live neighbors lives on to the next generation.
+ Overpopulation: Any live cell with more than three live neighbors dies.
+ Reproduction: Any dead cell with exactly three live neighbors becomes a live cell.

All cells are updated simultaneously, based on the current state of the grid.

Examples:
Input:
board = [[0,1,0], [0,0,1], [1,1,1], [0,0,0]]
Output:
[[0,0,0], [1,0,1], [0,1,1], [0,1,0]]

Input:
board = [[1,1], [1,0]]
Output:
[[1,1], [1,1]]
'''

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m, n = len(board), len(board[0])

        def count_live_neighbors(r, c):
            directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),  (1, 0), (1, 1)]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if abs(board[nr][nc]) == 1:
                        count += 1
            return count

        for r in range(m):
            for c in range(n):
                live_neighbors = count_live_neighbors(r, c)
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1
                else:
                    if live_neighbors == 3:
                        board[r][c] = 2

        for r in range(m):
            for c in range(n):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0