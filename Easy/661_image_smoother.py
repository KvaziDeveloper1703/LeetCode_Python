'''
Given an m x n integer matrix img representing the grayscale values of an image. You need to apply an image smoother to this image.
An image smoother is a 3 x 3 filter that processes each cell in the matrix by replacing its value with the floor of the average of its value and the values of its up to eight surrounding cells.
If one or more surrounding cells do not exist, they are simply ignored in the average calculation.

Return the resulting image as a new matrix after applying this smoother on every cell.

Examples:
Input: img = [  [1,1,1],
                [1,0,1],
                [1,1,1]
        ]
Output: [   [0,0,0],
            [0,0,0],
            [0,0,0]
    ]

Input: img = [  [100,200,100],
                [200,50,200],
                [100,200,100]
        ]
Output: [   [137,141,137],
            [141,138,141],
            [137,141,137]
    ]

Дан целочисленный матрицa img размером m x n, которая представляет уровни серого изображения. Необходимо применить к этой матрице сглаживающий фильтр.
Сглаживающий фильтр — это маска размером 3 x 3, которая обрабатывает каждую ячейку матрицы, заменяя её значение на округлённое вниз среднее между самой этой ячейкой и всеми её существующими соседями.
Если какие-то соседние ячейки отсутствуют, они просто не учитываются при вычислении среднего.

Верните новую матрицу, которая получится после применения этого фильтра ко всем ячейкам исходного изображения.

Примеры:
Ввод: img = [   [1,1,1],
                [1,0,1],
                [1,1,1]
        ]
Вывод: [[0,0,0],
        [0,0,0],
        [0,0,0]
    ]

Ввод: img = [   [100,200,100],
                [200,50,200],
                [100,200,100]
        ]
Вывод: [[137,141,137],
        [141,138,141],
        [137,141,137]
    ]
'''

from typing import List

def image_smoother(img: List[List[int]]) -> List[List[int]]:
    m, n = len(img), len(img[0])
    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            total = 0
            count = 0

            for ni in range(i - 1, i + 2):
                for nj in range(j - 1, j + 2):
                    if 0 <= ni < m and 0 <= nj < n:
                        total += img[ni][nj]
                        count += 1

            result[i][j] = total // count

    return result