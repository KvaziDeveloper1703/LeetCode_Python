'''
You are given a 0-indexed integer array numbers of length n.

Your task is to find the maximum difference numbers[j] - numbers[i] such that:
    - 0 ≤ i < j < n;
    - numbers[i] < numbers[j].

Return the value of this maximum difference. If no valid pair (i, j) exists, return -1.

Дан целочисленный массив numbers длины n с индексацией от 0.

Нужно найти максимальную разницу numbers[j] - numbers[i] такую, что:
    - 0 ≤ i < j < n;
    - numbers[i] < numbers[j].

Верните значение этой максимальной разницы. Если ни одной подходящей пары (i, j) не существует, верните -1.
'''

from typing import List

def maximum_difference(numbers: List[int]) -> int:
    minimum_value_so_far = numbers[0]
    maximum_difference = -1

    for current_value in numbers[1:]:
        if current_value > minimum_value_so_far:
            maximum_difference = max(maximum_difference, current_value - minimum_value_so_far)
        else:
            minimum_value_so_far = current_value

    return maximum_difference