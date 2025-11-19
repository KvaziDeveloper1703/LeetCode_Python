'''
Implement a function signFunc(x) that returns:
    - 1 if x is positive;
    - -1 if x is negative;
    - 0 if x equals 0.

You are given an integer array numbers. Let product be the product of all elements in numbers.

Return signFunc(product).

Examples:
Input: numbers = [-1, -2, -3, -4, 3, 2, 1]
Output: 1

Input: numbers = [1, 5, 0, 2, -3]
Output: 0

Реализуйте функцию signFunc(x), которая возвращает:
    - 1, если x - положительное число;
    - -1, если x - отрицательное число;
    - 0, если x равно нулю.

Вам дан массив целых чисел numbers. Пусть product - произведение всех элементов массива.

Верните signFunc(product).

Примеры:
Ввод: numbers = [-1, -2, -3, -4, 3, 2, 1]
Вывод: 1

Ввод: numbers = [1, 5, 0, 2, -3]
Вывод: 0
'''

from typing import List

def array_sign(numbers: List[int]) -> int:
    product_sign = 1
    for number in numbers:
        if number == 0:
            return 0
        if number < 0:
            product_sign = -product_sign
    return product_sign