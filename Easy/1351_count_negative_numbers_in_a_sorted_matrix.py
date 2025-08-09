'''
Given an m×n matrix grid that is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.

Examples:
Input: grid = [ [4,3,2,-1],
                [3,2,1,-1],
                [1,1,-1,-2],
                [-1,-1,-2,-3]
        ]
Output: 8

Input: grid = [ [3,2],
                [1,0]
        ]
Output: 0

Дана матрица grid размером m×n, в которой элементы отсортированы в невозрастающем порядке как по строкам, так и по столбцам.

Нужно вернуть количество отрицательных чисел в grid.

Примеры:
Ввод: grid = [  [4,3,2,-1],
                [3,2,1,-1],
                [1,1,-1,-2],
                [-1,-1,-2,-3]
        ]
Вывод: 8

Ввод: grid = [  [3,2],
                [1,0]
        ]
Вывод: 0
'''

from typing import List

def count_negatives(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, columns = len(grid), len(grid[0])
    row_index, column_index = 0, columns - 1
    negative_count = 0

    while row_index < rows and column_index >= 0:
        if grid[row_index][column_index] < 0:
            negative_count += rows - row_index
            column_index -= 1
        else:
            row_index += 1

    return negative_count