'''
You are given a 0-indexed integer array numbers and two integers key and k.

A k-distant index is an index i such that there exists at least one index j where: numbers[j] == key, and |i − j| ≤ k.

Return all such k-distant indices in increasing order.

Examples:
Input: numbers = [3,4,9,1,3,9,5], key = 9, k = 1
Output: [1,2,3,4,5,6]

Input: numbers = [2,2,2,2,2], key = 2, k = 2
Output: [0,1,2,3,4]

Дан массив целых чисел numbers с нумерацией от 0, а также два числа key и k.

k-дальний индекс - это индекс i, для которого есть хотя бы один индекс j, такой что: numbers[j] == key, |i − j| ≤ k.

Нужно вернуть все такие индексы i, отсортированные по возрастанию.

Примеры:
Ввод: numbers = [3,4,9,1,3,9,5], key = 9, k = 1
Вывод: [1,2,3,4,5,6]

Ввод: numbers = [2,2,2,2,2], key = 2, k = 2
Вывод: [0,1,2,3,4]
'''

from typing import List

def find_k_distant_indices(numbers: List[int], key: int, k: int) -> List[int]:
    key_positions = []
    result_indices = []

    for current_index in range(len(numbers)):
        if numbers[current_index] == key:
            key_positions.append(current_index)

    for candidate_index in range(len(numbers)):
        for key_index in key_positions:
            if abs(candidate_index - key_index) <= k:
                result_indices.append(candidate_index)
                break

    return result_indices