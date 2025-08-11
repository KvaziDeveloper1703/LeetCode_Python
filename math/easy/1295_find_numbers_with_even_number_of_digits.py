'''
Given an array numbers of integers, return how many of them contain an even number of digits.

Examples:
Input: numbers = [12, 345, 2, 6, 7896]
Output: 2

Input: numbers = [555, 901, 482, 1771]
Output: 1

Дан массив целых чисел numbers. Верните количество чисел в массиве, у которых чётное количество цифр.

Примеры:
Ввод: numbers = [12, 345, 2, 6, 7896]
Вывод: 2

Ввод: numbers = [555, 901, 482, 1771]
Вывод: 1
'''

from typing import List

def find_numbers(numbers: List[int]) -> int:
    count = 0
    for number in numbers:
        if len(str(number)) % 2 == 0:
            count += 1
    return count