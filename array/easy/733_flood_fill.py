'''
Given a 2D grid image of size m x n, where each image[i][j] represents a pixel color. You are also given:
    + sr – the starting pixel row index,
    + sc – the starting pixel column index,
    + color – the new color to apply.

Your task is to implement a flood fill algorithm starting at pixel (sr, sc). The flood fill algorithm works as follows:
    1) Change the color of the starting pixel to the new color;
    2) Then, recursively or iteratively change the color of all 4-directionally adjacent pixels (up, down, left, right) that have the same original color as the starting pixell;
    3) Repeat this process until no adjacent pixels of the original color remain.

Return the updated image after flood fill.

Example:
Input: image = [[1,1,1],
                [1,1,0],
                [1,0,1]
        ], sr = 1, sc = 1, color = 2
Output: [   [2,2,2],
            [2,2,0],
            [2,0,1]
    ]

Вам дано изображение в виде двумерного массива image размером m x n, где image[i][j] обозначает цвет пикселя. Также даны:
    + sr — индекс строки начального пикселя,
    + sc — индекс столбца начального пикселя,
    + color — новый цвет.

Ваша задача — реализовать алгоритм заливки, начиная с пикселя (sr, sc). Алгоритм работает так:
    1) Замените цвет начального пикселя на новый;
    2) Затем рекурсивно или итеративно замените цвет всех соседних по стороне (вверх, вниз, влево, вправо) пикселей, у которых такой же цвет, как у начального;
    3) Повторяйте, пока не останется подходящих соседних пикселей.

Верните изменённое изображение после заливки.

Пример:
Ввод: image = [ [1,1,1],
                [1,1,0],
                [1,0,1]
        ], sr = 1, sc = 1, color = 2
Вывод: [[2,2,2],
        [2,2,0],
        [2,0,1]
    ]
'''

from typing import List

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    start_color = image[sr][sc]
    if start_color == color:
        return image

    def dfs(r, c):
        if (0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == start_color):
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

    dfs(sr, sc)
    return image