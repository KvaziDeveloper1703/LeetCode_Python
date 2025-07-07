'''
You are given an integer array numbers. Move all the zeroes to the end of the array while maintaining the relative order of the non-zero elements.

You must perform this operation in-place, meaning you cannot create a copy of the array.

Examples:
Input: numbers = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: numbers = [0]
Output: [0]

Дан массив целых чисел numbers. Переместите все нули в конец массива, сохранив относительный порядок остальных элементов.

Операцию нужно выполнить на месте — без создания копии массива.

Примеры:
Ввод: numbers = [0,1,0,3,12]
Вывод: [1,3,12,0,0]

Ввод: numbers = [0]
Вывод: [0]
'''

from typing import List

def move_zeroes(numbers: List[int]) -> None:
    position_for_non_zero = 0

    for current_index in range(len(numbers)):
        if numbers[current_index] != 0:
            numbers[position_for_non_zero], numbers[current_index] = numbers[current_index], numbers[position_for_non_zero]
            position_for_non_zero += 1