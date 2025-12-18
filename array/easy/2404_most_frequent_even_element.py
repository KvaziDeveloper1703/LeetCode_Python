'''
You are given an integer array numbers.

Your task is to return the most frequent even number in the array.
    - If there are multiple even numbers with the same highest frequency, return the smallest of them.
    - If the array contains no even numbers, return -1.

Вам дан целочисленный массив numbers.

Необходимо найти и вернуть наиболее часто встречающееся чётное число в массиве.
    - Если несколько чётных чисел встречаются одинаково часто, верните наименьшее из них.
    - Если в массиве нет чётных чисел, верните -1.
'''

from typing import List
from collections import Counter

def most_frequent_even(numbers: List[int]) -> int:
    even_numbers = [number for number in numbers if number % 2 == 0]

    if not even_numbers:
        return -1

    frequency = Counter(even_numbers)
    maximum_frequency = max(frequency.values())

    most_frequent = [
        number for number, count in frequency.items()
        if count == maximum_frequency
    ]

    return min(most_frequent)