'''
An axis-aligned rectangle is defined by a list [x1, y1, x2, y2], where:
    + (x1, y1) is the bottom-left corner,
    + (x2, y2) is the top-right corner.

The rectangle’s edges are parallel to the coordinate axes.

Two rectangles overlap if their intersection has a positive area. That means:
    + If they only touch at the edge or corner, they do not overlap.

Given two rectangles rectangle_1 and rectangle_2, return True if they overlap, and False otherwise.

Examples:
Input:  rectangle_1 = [0,0,2,2], rectangle_2 = [1,1,3,3]
Output: True

Input:  rectangle_1 = [0,0,1,1], rectangle_2 = [1,0,2,1]
Output: False

Прямоугольник, выровненный по осям координат, задаётся списком [x1, y1, x2, y2], где:
    + (x1, y1) — координаты нижнего левого угла,
    + (x2, y2) — координаты верхнего правого угла.

Грани прямоугольника параллельны осям координат.

Два прямоугольника считаются перекрывающимися, если площадь их пересечения положительная. Это означает:
    + Если они только касаются по краю или в углу, то они не перекрываются.

Дано два прямоугольника rectangle_1 и rectangle_2. Верните True, если они перекрываются, и False в противном случае.

Примеры:
Ввод: rectangle_1 = [0,0,2,2], rectangle_2 = [1,1,3,3]
Вывод: True

Ввод: rectangle_1 = [0,0,1,1], rectangle_2 = [1,0,2,1]
Вывод: False
'''

from typing import List

def is_rectangle_overlap(rectangle_1: List[int], rectangle_2: List[int]) -> bool:
    return not (
        rectangle_1[2] <= rectangle_2[0] or
        rectangle_1[0] >= rectangle_2[2] or
        rectangle_1[3] <= rectangle_2[1] or
        rectangle_1[1] >= rectangle_2[3]
    )