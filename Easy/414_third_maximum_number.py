'''
You are given an array of integers numbers.
Return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example:
Input: numbers = [3, 2, 1]
Output: 1

Вам дан массив целых чисел numbers.
Нужно вернуть третье по величине уникальное число в этом массиве.
Если третьего уникального максимума не существует, верните наибольшее число в массиве.

Пример:
Ввод: numbers = [3, 2, 1]
Вывод: 1
'''

from typing import List

def thirdMax(numbers: List[int]) -> int:
    first = second = third = float('-inf')
    for number in numbers:
        if number in (first, second, third):
            continue
        if number > first:
            first, second, third = number, first, second
        elif number > second:
            second, third = number, second
        elif number > third:
            third = number
    return third if third != float('-inf') else first