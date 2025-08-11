'''
Given an integer array numbers representing side lengths.

Return the largest perimeter of a triangle with non-zero area that can be formed using any three lengths from numbers. If no such triangle can be formed, return 0.

Examples:
Input: numbers = [2, 1, 2]
Output: 5

Input: numbers = [1, 2, 1, 10]
Output: 0

Вам дан массив целых чисел numbers, представляющий длины сторон.

Ваша задача — вернуть наибольший возможный периметр треугольника с ненулевой площадью, который можно составить из любых трёх длин из массива numbers. Если нельзя составить ни одного треугольника, верните 0.

Примеры:
Ввод: numbers = [2, 1, 2]
Вывод: 5

Ввод: numbers = [1, 2, 1, 10]
Вывод: 0
'''

from typing import List

def largest_perimeter(numbers: List[int]) -> int:
    sorted_lengths = sorted(numbers, reverse=True)
    for i in range(len(sorted_lengths) - 2):
        side_1 = sorted_lengths[i]
        side_2 = sorted_lengths[i + 1]
        side_3 = sorted_lengths[i + 2]
        if side_2 + side_3 > side_1:
            return side_1 + side_2 + side_3
    return 0