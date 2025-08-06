'''
Given a 2D grid of size m x n and an integer k. Your task is to shift the elements of the grid k times.

In one shift operation:
    1) The element at grid[i][j] moves to grid[i][j + 1];
    2) The element at grid[i][n - 1] moves to grid[i + 1][0];
    3) The element at grid[m - 1][n - 1] moves to grid[0][0].

Return the 2D grid after performing the shift operation k times.

Example:
Input: grid = [ [1,2,3],
                [4,5,6],
                [7,8,9]
        ], k = 1
Output: [   [9,1,2],
            [3,4,5],
            [6,7,8]
    ]

Вам дана двумерная таблица размером m x n и целое число k. Необходимо сдвинуть элементы таблицы k раз.

В одной операции сдвига:
    1) Элемент grid[i][j] перемещается в grid[i][j + 1];
    2) Элемент grid[i][n - 1] перемещается в grid[i + 1][0];
    3) Элемент grid[m - 1][n - 1] перемещается в grid[0][0].

Верните таблицу после выполнения операции сдвига k раз.

Пример:
Ввод: grid = [  [1,2,3],
                [4,5,6],
                [7,8,9]
        ], k = 1
Вывод: [[9,1,2],
        [3,4,5],
        [6,7,8]
    ]
'''

from typing import List

def shift_grid(grid: List[List[int]], k: int) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0])
    total_elements = m * n

    flat_list = []
    for row in range(m):
        for column in range(n):
            flat_list.append(grid[row][column])
    
    k = k % total_elements
    shifted_list = flat_list[-k:] + flat_list[:-k]
    
    new_grid = []
    for row_index in range(m):
        start = row_index * n
        end = start + n
        new_grid.append(shifted_list[start:end])
    
    return new_grid