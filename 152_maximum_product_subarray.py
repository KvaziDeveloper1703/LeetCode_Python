'''
Given an array of integers numbers, find the contiguous subarray that has the largest product, and return that product.
It is guaranteed that the result will fit within a 32-bit signed integer.

Example:
Input: numbers = [2, 3, -2, 4]
Output: 6

Дан массив целых чисел numbers. Найдите подмассив с непрерывными элементами, у которого максимальное произведение, и верните это произведение.
Гарантируется, что результат поместится в 32-битное целое число со знаком.

Пример:
Ввод: numbers = [2, 3, -2, 4]
Вывод: 6
'''

from typing import List

def max_product(numbers: List[int]) -> int:
    if not numbers:
        return 0

    max_product = min_product = result = numbers[0]
    for number in numbers[1:]:
        if number < 0:
            max_product, min_product = min_product, max_product

        max_product = max(number, max_product * number)
        min_product = min(number, min_product * number)
        result = max(result, max_product)

    return result