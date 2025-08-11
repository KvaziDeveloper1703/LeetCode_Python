'''
Given an integer array numbers sorted in non-decreasing order.

Return a new array containing the squares of each number from numbers, also sorted in non-decreasing order.

Examples:
Input: numbers = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]

Input: numbers = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]

Вам дан массив целых чисел numbers, отсортированный по неубыванию.

Ваша задача — вернуть новый массив, содержащий квадраты всех чисел из numbers, также отсортированный по неубыванию.

Примеры:
Ввод: numbers = [-4, -1, 0, 3, 10]
Вывод: [0, 1, 9, 16, 100]

Ввод: numbers = [-7, -3, 2, 3, 11]
Вывод: [4, 9, 9, 49, 121]
'''

from typing import List

def sorted_squares(numbers: List[int]) -> List[int]:
    left = 0
    right = len(numbers) - 1
    result = [0] * len(numbers)
    insert_position = len(numbers) - 1

    while left <= right:
        left_square = numbers[left] ** 2
        right_square = numbers[right] ** 2
        if left_square > right_square:
            result[insert_position] = left_square
            left += 1
        else:
            result[insert_position] = right_square
            right -= 1
        insert_position -= 1

    return result