'''
You are given four integer arrays numbers_1, numbers_2, numbers_3, and numbers_4, each of length n.
Return the number of tuples (i, j, k, l) such that:
    + 0 <= i, j, k, l < n, and
    + numbers_1[i] + numbers_2[j] + numbers_3[k] + numbers_4[l] == 0

Example:
Input:  numbers_1 = [1, 2]
        numbers_2 = [-2, -1]
        numbers_3 = [-1, 2]
        numbers_4 = [0, 2]
Output: 2

Даны четыре массива целых чисел: numbers_1, numbers_2, numbers_3 и numbers_4, каждый длины n.
Найти количество четвёрок индексов (i, j, k, l), таких что:
    + 0 <= i, j, k, l < n, и
    + numbers_1[i] + numbers_2[j] + numbers_3[k] + numbers_4[l] == 0

Пример:
Ввод:   numbers_1 = [1, 2]
        numbers_2 = [-2, -1]
        numbers_3 = [-1, 2]
        numbers_4 = [0, 2]
Вывод:  2
'''

from collections import Counter
from typing import List

def four_sum_count(numbers_1: List[int], numbers_2: List[int], numbers_3: List[int], numbers_4: List[int]) -> int:
    total_count = 0
    
    sum_first_two_arrays = Counter()
    for first_array_element in numbers_1:
        for second_array_element in numbers_2:
            current_sum = first_array_element + second_array_element
            sum_first_two_arrays[current_sum] += 1
    for third_array_element in numbers_3:
        for fourth_array_element in numbers_4:
            current_sum = third_array_element + fourth_array_element
            target_sum = -current_sum
            if target_sum in sum_first_two_arrays:
                total_count += sum_first_two_arrays[target_sum]
    return total_count