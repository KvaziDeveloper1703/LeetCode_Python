'''
You are given an array rectangles, where each element rectangles[i] = [li, wi] represents the length and width of the i-th rectangle.

From each rectangle, you can cut out the largest possible square.
The size of that square is equal to the smaller side of the rectangle.

Among all rectangles, find the largest square size that can be made.

Then return how many rectangles can produce a square of that largest size.

Дан массив rectangles, где каждый элемент [lᵢ, wᵢ] - это длина и ширина i-го прямоугольника.

Из каждого прямоугольника можно вырезать самый большой возможный квадрат.
Размер этого квадрата всегда равен меньшей стороне прямоугольника.

Сначала нужно определить максимальный размер квадрата, который вообще можно получить из всех прямоугольников.

Затем нужно вернуть количество прямоугольников, из которых можно вырезать квадрат именно этого максимального размера.
'''

from typing import List

def count_good_rectangles(rectangles: List[List[int]]) -> int:
    max_length = 0
    count = 0

    for l, w in rectangles:
        side = min(l, w)
        if side > max_length:
            max_length = side
            count = 1
        elif side == max_length:
            count += 1

    return count