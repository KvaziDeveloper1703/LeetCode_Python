'''
You are given an integer array numbers.
Return the greatest common divisor of the smallest number and the largest number in the array.

The greatest common divisor of two numbers is the largest positive integer that divides both numbers without a remainder.

Examples:
Input: numbers = [2,5,6,9,10]
Output: 2

Input: numbers = [7,5,6,8,3]
Output: 1

Дан массив целых чисел numbers.
Нужно вернуть наибольший общий делитель минимального и максимального чисел в массиве.

Наибольший общий делитель двух чисел - это самое большое положительное число, которое делит оба числа без остатка.

Примеры:
Ввод: numbers = [2,5,6,9,10]
Вывод: 2

Ввод: numbers = [7,5,6,8,3]
Вывод: 1
'''

from typing import List
from math import gcd

def find_GCD(numbers: List[int]) -> int:
    smallest_number = min(numbers)
    largest_number = max(numbers)
    return gcd(smallest_number, largest_number)