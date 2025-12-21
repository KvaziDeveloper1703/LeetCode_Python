'''
A valid cut in a circle can be one of the following:
    - A straight line that touches two points on the boundary of the circle and passes through the center, or
    - A straight line that touches one point on the boundary of the circle and passes through the center.

Some examples of valid and invalid cuts are shown in the figures.

You are given an integer n.

Return the minimum number of cuts required to divide the circle into n equal slices.

Examples:
Input: n = 4
Output: 2

Input: n = 3
Output: 3

Допустимый разрез круга может быть одним из следующих:
    - Прямая линия, которая касается двух точек на границе круга и проходит через его центр, или
    - Прямая линия, которая касается одной точки на границе круга и проходит через его центр.

На рисунках показаны примеры допустимых и недопустимых разрезов.

Дано целое число n.

Необходимо вернуть минимальное количество разрезов, необходимых для деления круга на n равных секторов.

Примеры:
Ввод: n = 4
Вывод: 2

Ввод: n = 3
Вывод: 3
'''

def number_of_cuts(n: int) -> int:
    if n == 1:
        return 0
    if n % 2 == 0:
        return n // 2
    return n