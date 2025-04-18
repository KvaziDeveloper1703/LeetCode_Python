'''
You are given an n x n 2D matrix representing an image. Rotate the image 90 degrees clockwise, in-place.
This means you must modify the original matrix directly, without using another 2D matrix for the rotation.

Examples:
Input: matrix = [[1,2,3], 
                 [4,5,6], 
                 [7,8,9]]
Output: [[7,4,1], 
         [8,5,2], 
         [9,6,3]]

Input: matrix = [[5,1,9,11], 
                 [2,4,8,10], 
                 [13,3,6,7], 
                 [15,14,12,16]]
Output: [[15,13,2,5], 
         [14,3,4,1], 
         [12,6,8,9], 
         [16,7,10,11]]

Дана квадратная матрица размером n x n, представляющая изображение.
Поверните изображение на 90 градусов по часовой стрелке, изменяя исходную матрицу на месте (то есть без использования дополнительной двумерной матрицы).

Примеры:
Ввод: matrix = [[1, 2, 3],  
                [4, 5, 6],  
                [7, 8, 9]]
Вывод: [[7, 4, 1],  
        [8, 5, 2],  
        [9, 6, 3]]

Ввод: matrix = [[5, 1, 9, 11],  
                [2, 4, 8, 10],  
                [13, 3, 6, 7],  
                [15, 14, 12, 16]]
Вывод: [[15, 13, 2, 5],  
        [14, 3, 4, 1],  
        [12, 6, 8, 9],  
        [16, 7, 10, 11]]
'''

from typing import List

def rotate(matrix: List[List[int]]) -> None:
    N = len(matrix)

    for i in range(N):
        for j in range(i + 1, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()