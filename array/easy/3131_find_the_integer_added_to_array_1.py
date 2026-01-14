'''
You are given two arrays of the same length: numbers_1 and numbers_2.
Each element of numbers_1 was changed by adding the same integer x.
After applying this change to every element, numbers_1 becomes equal to numbers_2.
Two arrays are considered equal if they contain the same integers with the same frequencies.
Return the integer x.

Examples:
Input: numbers_1 = [2,6,4], numbers_2 = [9,7,5]
Output: 3

Input: numbers_1 = [10], numbers_2 = [5]
Output: -5

Даны два массива одинаковой длины: numbers_1 и numbers_2.
Каждый элемент массива numbers_1 был изменён путём прибавления одного и того же целого числа x.
После изменения каждого элемента numbers_1, массив numbers_1 становится равен numbers_2.
Два массива считаются равными, если они содержат одинаковые числа с одинаковыми количествами повторений.
Верни целое число x.

Примеры:
Ввод: numbers_1 = [2,6,4], numbers_2 = [9,7,5]
Вывод: 3

Ввод: numbers1 = [10], numbers2 = [5]
Вывод: -5
'''

from typing import List

def added_integer(numbers_1: List[int], numbers_2: List[int]) -> int:
    numbers_1.sort()
    numbers_2.sort()

    return numbers_2[0] - numbers_1[0]