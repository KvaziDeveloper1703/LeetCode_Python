'''
You are given an integer array numbers of size n.

Return the number in the array whose value is closest to 0.

If there are multiple such numbers, return the one with the largest value.

Examples:
Input: numbers = [-4, -2, 1, 4, 8]
Output: 1

Input: numbers = [2, -1, 1]
Output: 1

Дан массив целых чисел numbers размера n.

Нужно вернуть число из массива, которое находится ближе всего к 0.

Если таких чисел несколько, нужно вернуть наибольшее из них.

Примеры:
Ввод: numbers = [-4, -2, 1, 4, 8]
Вывод: 1

Ввод: numbers = [2, -1, 1]
Вывод: 1
'''

from typing import List

def find_closest_number(numbers: List[int]) -> int:
    closest_number = numbers[0]

    for number in numbers:
        if abs(number) < abs(closest_number):
            closest_number = number
        elif abs(number) == abs(closest_number) and number > closest_number:
            closest_number = number

    return closest_number