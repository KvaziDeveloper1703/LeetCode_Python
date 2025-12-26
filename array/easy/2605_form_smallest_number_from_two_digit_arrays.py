'''
You are given two arrays of unique digits, numbers1 and numbers2.

Return the smallest possible number that contains at least one digit from each array.

Examples:
Input: numbers1 = [4, 1, 3], numbers2 = [5, 7]
Output: 15

Input: numbers1 = [3, 5, 2, 6], numbers2 = [3, 1, 7]
Output: 3

Даны два массива уникальных цифр - numbers1 и numbers2.

Необходимо вернуть наименьшее возможное число, которое содержит хотя бы одну цифру из каждого массива.

Примеры:
Ввод: numbers1 = [4, 1, 3], numbers2 = [5, 7]
Вывод: 15

Ввод: numbers1 = [3, 5, 2, 6], numbers2 = [3, 1, 7]
Вывод: 3
'''

from typing import List

def min_number(numbers1: List[int], numbers2: List[int]) -> int:
    common_digits = set(numbers1) & set(numbers2)

    if common_digits:
        return min(common_digits)

    smallest_from_numbers1 = min(numbers1)
    smallest_from_numbers2 = min(numbers2)

    return min(smallest_from_numbers1 * 10 + smallest_from_numbers2, smallest_from_numbers2 * 10 + smallest_from_numbers1)