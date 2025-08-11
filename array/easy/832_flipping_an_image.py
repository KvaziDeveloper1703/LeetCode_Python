'''
Given an n x n binary matrix image, perform the following two operations and return the resulting matrix:
    1) Flip Horizontally: Reverse each row of the matrix;
    2) Invert: Replace every 0 with 1, and every 1 with 0.

Examples:
Input: image = [[1,1,0],
                [1,0,1],
                [0,0,0]
        ]
Output: [   [1,0,0], 
            [0,1,0], 
            [1,1,1]
    ]

Input: image = [[1,1,0,0],
                [1,0,0,1],
                [0,1,1,1],
                [1,0,1,0]
        ]
Output: [   [1,1,0,0],
            [0,1,1,0],
            [0,0,0,1],
            [1,0,1,0]
    ]

Дана бинарная матрица размера n x n под названием image. Выполните над ней два действия и верните полученную матрицу:
    1) Горизонтальное отражение: Разверните каждую строку матрицы в обратном порядке;
    2) Инвертирование: Замените все 0 на 1, а все 1 на 0.

Примеры:
Ввод: image = [ [1,1,0],
                [1,0,1],
                [0,0,0]
        ]
Вывод: [[1,0,0],
        [0,1,0],
        [1,1,1]
    ]

Ввод: image = [ [1,1,0,0],
                [1,0,0,1],
                [0,1,1,1],
                [1,0,1,0]
        ]
Вывод: [[1,1,0,0],
        [0,1,1,0],
        [0,0,0,1],
        [1,0,1,0]
    ]
'''

from typing import List

def flip_and_invert_image(image: List[List[int]]) -> List[List[int]]:
    result = []

    for row in image:
        flipped_row = row[::-1]

        inverted_row = []
        for pixel in flipped_row:
            inverted_pixel = 1 - pixel
            inverted_row.append(inverted_pixel)

        result.append(inverted_row)

    return result