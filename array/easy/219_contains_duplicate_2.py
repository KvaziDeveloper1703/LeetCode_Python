'''
Given an integer array numbers and an integer k. Return True if there are two distinct indices i and j in the array such that numbers[i] == numbers[j] and abs(i - j) <= k.

Examples:
Input: numbers = [1,2,3,1], k = 3
Output: True

Input: numbers = [1,0,1,1], k = 1
Output: True

Дан массив целых чисел numbers и целое число k. Необходимо определить, существуют ли два различных индекса i и j, такие что: numbers[i] == numbers[j], и |i - j| <= k. 
Верните True, если такие индексы существуют, иначе — false.

Примеры:
Ввод: numbers = [1, 2, 3, 1], k = 3
Вывод: True

Ввод: numbers = [1, 0, 1, 1], k = 1
Вывод: True
'''

from typing import List

def contains_nearby_duplicate(numbers: List[int], k: int) -> bool:
    number_index_map = {}

    for index, number in enumerate(numbers):
        if number in number_index_map and index - number_index_map[number] <= k:
            return True
        number_index_map[number] = index

    return False