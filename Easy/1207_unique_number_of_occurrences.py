'''
Given an array of integers my_array.

Return True if the number of occurrences of each value in the array is unique. Otherwise, return False.

Examples:
Input: my_array = [1,2,2,1,1,3]
Output: True

Input: my_array = [1,2]
Output: False

Дан массив целых чисел my_array.

Верните True, если количество вхождений каждого значения в массиве уникально. В противном случае верните False.

Примеры:
Ввод: my_array = [1,2,2,1,1,3]
Вывод: True

Ввод: my_array = [1,2]
Вывод: False
'''

from typing import List

def unique_occurrences(my_array: List[int]) -> bool:
    counts = {}
    for number in my_array:
        counts[number] = counts.get(number, 0) + 1
    return len(set(counts.values())) == len(counts)