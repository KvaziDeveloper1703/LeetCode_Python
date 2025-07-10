'''
Given an integer array numbers, return a new array answer such that answer[i] is equal to the product of all elements in numbers except numbers[i].
    + The result for each position must be calculated without using the division operation;
    + The algorithm must run in O(n) time complexity;
    + It is guaranteed that the product of all prefix or suffix elements will fit within a 32-bit integer.

Examples:
Input: numbers = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Input: numbers = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]

Дан массив целых чисел numbers. Необходимо вернуть новый массив answer, такой что answer[i] равен произведению всех элементов массива numbers, кроме numbers[i].
    + Нельзя использовать операцию деления при вычислениях;
    + Алгоритм должен работать за O(n) по времени;
    + Гарантируется, что произведения всех префиксов и суффиксов поместятся в 32-битное целое число.

Примеры:
Ввод: numbers = [1, 2, 3, 4]
Вывод: [24, 12, 8, 6]

Ввод: numbers = [-1, 1, 0, -3, 3]
Вывод: [0, 0, 9, 0, 0]
'''

from typing import List

def product_except_self(numbers: List[int]) -> List[int]:
    length = len(numbers)
    result = [1] * length

    left_product = 1
    for i in range(length):
        result[i] = left_product
        left_product *= numbers[i]

    right_product = 1
    for i in range(length - 1, -1, -1):
        result[i] *= right_product
        right_product *= numbers[i]

    return result