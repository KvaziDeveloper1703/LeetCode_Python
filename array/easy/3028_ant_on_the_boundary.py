'''
An ant starts at a boundary point on an infinite line. During its movement, it may go left or right.

You are given an array of non-zero integers numbers. The ant processes the array from the first element to the last, and at each step moves according to the current value:
    - If numbers[i] < 0, the ant moves left by |numbers[i]| units;
    - If numbers[i] > 0, the ant moves right by numbers[i] units.

Return the number of times the ant ends up exactly on the boundary after completing a move.

Examples:
Input: numbers = [2, 3, -5]
Output: 1

Input: numbers = [3, 2, -3, -4]
Output: 0

Муравей находится в точке границы на бесконечной прямой. В процессе движения он может идти влево или вправо.

Вам дан массив ненулевых целых чисел numbers. Муравей последовательно обрабатывает элементы массива с первого до последнего, и на каждом шаге перемещается в соответствии со значением текущего элемента:
    - Если numbers[i] < 0, муравей движется влево на |numbers[i]| единиц;
    - Если numbers[i] > 0, муравей движется вправо на numbers[i] единиц.

Необходимо определить, сколько раз муравей оказывается ровно на границе после завершения очередного перемещения.

Примеры:
Ввод: numbers = [2, 3, -5]
Вывод: 1

Ввод: numbers = [3, 2, -3, -4]
Вывод: 0
'''

from typing import List

def return_to_boundary_count(numbers: List[int]) -> int:
    current_position = 0
    return_count = 0

    for movement in numbers:
        current_position += movement
        if current_position == 0:
            return_count += 1

    return return_count