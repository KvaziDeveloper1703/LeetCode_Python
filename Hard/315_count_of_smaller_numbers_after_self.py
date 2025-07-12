'''
Given an integer array numbers.

Return an integer array counts where counts[i] is the number of smaller elements to the right of numbers[i].

Examples:
Input: numbers = [5, 2, 6, 1]
Output: [2, 1, 1, 0]

Input: numbers = [-1]
Output: [0]

Input: numbers = [-1, -1]
Output: [0, 0]

Дан массив целых чисел numbers. 

Верните массив целых чисел counts, где counts[i] — это количество элементов справа от numbers[i], которые меньше numbers[i].

Примеры:
Ввод: numbers = [5, 2, 6, 1]
Вывод: [2, 1, 1, 0]

Ввод: numbers = [-1]
Вывод: [0]

Ввод: numbers = [-1, -1]
Вывод: [0, 0]
'''

from bisect import bisect_left, insort
from typing import List

def count_smaller(numbers: List[int]) -> List[int]:
    result = []
    sorted_list = []

    for number in reversed(numbers):
        index = bisect_left(sorted_list, number)
        result.append(index)
        insort(sorted_list, number)

    return result[::-1]