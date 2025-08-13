'''
Given an array of integers my_array.

A lucky integer is defined as an integer whose frequency in the array is equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer, return -1.

Examples:
Input: my_array = [2,2,3,4]
Output: 2

Input: my_array = [1,2,2,3,3,3]
Output: 3

Дан массив целых чисел my_array.

Счастливое число — это число, частота встречаемости которого в массиве равна его значению.

Нужно вернуть наибольшее счастливое число в массиве. Если счастливых чисел нет, вернуть -1.

Примеры:
Ввод: my_array = [2,2,3,4]
Вывод: 2

Ввод:  my_array = [1,2,2,3,3,3]
Вывод: 3
'''

from typing import List
from collections import Counter

def find_lucky(my_array: List[int]) -> int:
    frequency_map = Counter(my_array)

    lucky_numbers: List[int] = []
    for number, occurrence_count in frequency_map.items():
        if number == occurrence_count:
            lucky_numbers.append(number)

    if lucky_numbers:
        largest_lucky_number = max(lucky_numbers)
        return largest_lucky_number
    else:
        return -1