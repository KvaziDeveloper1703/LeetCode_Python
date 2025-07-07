'''
A web developer needs to determine the dimensions of a web page. Given a specific rectangular web page area, your task is to design a rectangle with dimensions length L and width W that satisfy the following requirements:
    1) The area of the rectangle must equal the given target area;
    2) The width W should not be larger than the length L;
    3) The difference between the length and the width should be as small as possible.

Return an array [L, W] where L is the length and W is the width.

Examples:
Input: area = 4
Output: [2, 2]

Input: area = 37
Output: [37,1]

Веб-разработчику нужно определить размеры веб-страницы. Дан прямоугольник с заданной площадью. Ваша задача — спроектировать прямоугольную веб-страницу с размерами длина L и ширина W, которые удовлетворяют следующим условиям:
    1) Площадь прямоугольника должна быть равна заданной целевой площади;
    2) Ширина W не должна быть больше длины L, то есть L >= W;
    3) Разность между длиной и шириной должна быть минимальной из всех возможных вариантов.

Верните массив [L, W], где L — длина, а W — ширина.

Примеры:
Ввод: area = 4
Вывод: [2, 2]

Ввод: area = 37
Вывод: [37,1]
'''

from typing import List

def construct_rectangle(self, area: int) -> List[int]:
    w = int(area ** 0.5)

    while area % w != 0:
        w -= 1
    l = area // w

    return [l, w]