'''
You are given two integer arrays numbers1 and numbers2, both sorted in non-decreasing order.

Your task is to find and return the smallest integer that appears in both arrays. If there is no common integer, return -1.

An integer is considered common to numbers1 and numbers2 if it appears at least once in each array.

Examples:
Input: numbers1 = [1, 2, 3], numbers2 = [2, 4]
Output: 2

Input: numbers1 = [1, 2, 3, 6], numbers2 = [2, 3, 4, 5]
Output: 2

Даны два массива целых чисел numbers1 и numbers2, отсортированные в неубывающем порядке.

Необходимо найти и вернуть наименьшее целое число, которое встречается в обоих массивах. Если общего элемента нет, верните -1.

Число считается общим для numbers1 и numbers2, если оно встречается хотя бы один раз в каждом массиве.

Примеры:
Ввод: numbers1 = [1, 2, 3], numbers2 = [2, 4]
Вывод: 2

Ввод: numbers1 = [1, 2, 3, 6], numbers2 = [2, 3, 4, 5]
Вывод: 2
'''

from typing import List

def get_common(numbers1: List[int], numbers2: List[int]) -> int:
    pointer_one = 0
    pointer_two = 0

    while pointer_one < len(numbers1) and pointer_two < len(numbers2):
        if numbers1[pointer_one] == numbers2[pointer_two]:
            return numbers1[pointer_one]
        elif numbers1[pointer_one] < numbers2[pointer_two]:
            pointer_one += 1
        else:
            pointer_two += 1

    return -1