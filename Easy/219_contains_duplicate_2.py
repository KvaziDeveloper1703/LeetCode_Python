'''
Given an integer array numbers and an integer k. Return true if there are two distinct indices i and j in the array such that numbers[i] == numbers[j] and abs(i - j) <= k.

Examples:
Input: numbers = [1,2,3,1], k = 3
Output: true

Input: numbers = [1,0,1,1], k = 1
Output: true

Дан массив целых чисел numbers и целое число k. Необходимо определить, существуют ли два различных индекса i и j, такие что: numbers[i] == numbers[j], и |i - j| <= k. 
Верните true, если такие индексы существуют, иначе — false.

Примеры:
Ввод: numbers = [1, 2, 3, 1], k = 3
Вывод: true

Ввод: numbers = [1, 0, 1, 1], k = 1
Вывод: true
'''

from typing import List

def contains_nearby_duplicate(numbers: List[int], k: int) -> bool:
    num_index_map = {}

    for index, number in enumerate(numbers):
        if number in num_index_map and index - num_index_map[number] <= k:
            return True
        num_index_map[number] = index

    return False