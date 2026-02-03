'''
You are given an m × n matrix grid containing non-negative integers.

In one operation, you may increase any element grid[i][j] by 1.

Your goal is to make each column strictly increasing from top to bottom.
This means every element must be strictly greater than the element above it in the same column.

Return the minimum number of operations required to achieve this.

Examples:
Input: grid = [ [3,2],
                [1,3],
                [3,4],
                [0,1]
            ]
Output: 15

Input: grid = [ [3,2,1],
                [2,1,0],
                [1,2,3]
            ]
Output: 12

You are given an m × n matrix grid containing non-negative integers.

In one operation, you may increase any element grid[i][j] by 1.

Your goal is to make each column strictly increasing from top to bottom.
This means every element must be strictly greater than the element above it in the same column.

Return the minimum number of operations required to achieve this.

Examples:
Input: grid = [ [3,2],
                [1,3],
                [3,4],
                [0,1]
            ]
Output: 15

Input: grid = [ [3,2,1],
                [2,1,0],
                [1,2,3]
            ]
Output: 12

Дана матрица размера m × n под названием grid, состоящая из неотрицательных целых чисел.

За одну операцию можно увеличить любое значение grid[i][j] на 1.

Нужно сделать так, чтобы каждый столбец был строго возрастающим сверху вниз.
То есть каждый элемент должен быть строго больше элемента над ним.

Верните минимальное количество операций, необходимое для этого.

Примеры:
Ввод: grid = [  [3,2],
                [1,3],
                [3,4],
                [0,1]
            ]
Вывод: 15

Ввод: grid = [  [3,2,1],
                [2,1,0],
                [1,2,3]
            ]
Вывод: 12
'''

from typing import List

def minimum_operations(grid: List[List[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])

    total_operations = 0

    for column in range(columns):
        previous_value = grid[0][column]

        for row in range(1, rows):
            current_value = grid[row][column]

            if current_value <= previous_value:
                needed_value = previous_value + 1
                total_operations += needed_value - current_value
                previous_value = needed_value
            else:
                previous_value = current_value

    return total_operations