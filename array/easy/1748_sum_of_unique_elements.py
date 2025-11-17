'''
You are given an integer array numbers.

The unique elements of the array are the elements that appear exactly once.

Return the sum of all unique elements in numbers.

Examples:
Input: numbers = [1, 2, 3, 2]
Output: 4

Input: numbers = [1, 1, 1, 1, 1]
Output: 0

Дан массив целых чисел numbers.

Уникальные элементы массива - это те элементы, которые встречаются ровно один раз.

Верните сумму всех уникальных элементов массива numbers.

Примеры:
Ввод: numbers = [1, 2, 3, 2]
Вывод: 4

Ввод: numbers = [1, 1, 1, 1, 1]
Вывод: 0
'''

from typing import List
from collections import Counter

def sum_of_unique(numbers: List[int]) -> int:
    frequency = Counter(numbers)
    unique_sum = 0

    for number, count in frequency.items():
        if count == 1:
            unique_sum += number

    return unique_sum