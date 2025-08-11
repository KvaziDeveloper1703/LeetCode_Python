'''
You are given a row x column grid representing a map, where:
    + grid[i][j] = 1 represents land;
    + grid[i][j] = 0 represents water.

Cells are connected horizontally and vertically. The grid is completely surrounded by water, and it contains exactly one island — a group of one or more connected land cells.
The island has no lakes — meaning any water within the island is not connected to the surrounding water. Each cell is a square with side length 1. The grid is a rectangle and its width and height do not exceed 100.
Your task is to calculate the perimeter of the island.

Examples:
Input: grid = [ [0,1,0,0], 
                [1,1,1,0], 
                [0,1,0,0], 
                [1,1,0,0]]
Output: 16

Input: grid = [ [1]]
Output: 4

Дана карта в виде двумерного массива размером row x columns, где:
    + grid[i][j] = 1 означает землю;
    + grid[i][j] = 0 означает воду.

Ячейки соединены по горизонтали и вертикали. Сетка полностью окружена водой и содержит ровно один остров — группу связанных ячеек с землёй.
Озёр нет — т.е. внутренняя вода не соединена с внешней. Каждая ячейка — это квадрат со стороной 1. Размеры сетки не превышают 100 по ширине и высоте.
Ваша задача — найти периметр острова.

Примеры:
Ввод: [ [0,1,0,0], 
        [1,1,1,0], 
        [0,1,0,0], 
        [1,1,0,0]]
Вывод: 16

Ввод: [ [1]]
Вывод: 4
'''

def island_perimeter(grid: list[list[int]]) -> int:
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter