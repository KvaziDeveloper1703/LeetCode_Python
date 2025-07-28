'''
Given an integer array numbers with the following properties:
    + numbers.length == 2 * n;
    + numbers contains exactly n + 1 unique elements;
    + Exactly one element in numbers is repeated n times.

Return the element that is repeated n times.

Examples:
Input: numbers = [1, 2, 3, 3]
Output: 3

Input: numbers = [2, 1, 2, 5, 3, 2]
Output: 2

Вам дан массив целых чисел numbers, обладающий следующими свойствами:
    + numbers.length == 2 * n;
    + В массиве содержится ровно n + 1 уникальных элементов;
    + Только один элемент повторяется ровно n раз.

Ваша задача — вернуть элемент, который повторяется n раз.

Примеры:
Ввод: numbers = [1, 2, 3, 3]
Вывод: 3

Ввод: numbers = [2, 1, 2, 5, 3, 2]
Вывод: 2
'''

from typing import List

def repeated_n_times(numbers: List[int]) -> int:
    seen_elements = set()
    for number in numbers:
        if number in seen_elements:
            return number
        seen_elements.add(number)