'''
You are given an integer array numbers and an integer k.

Your task is to find a subsequence of numbers of length k that has the maximum possible sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array formed by deleting some of the elements from another array without changing the order of the remaining elements.

Examples:
Input: numbers = [2,1,3,3], k = 2
Output: [3,3]

Input: numbers = [-1,-2,3,4], k = 3
Output: [-1,3,4]

Вам дан массив целых чисел numbers и число k.

Нужно найти подпоследовательность длины k, которая имеет максимальную сумму среди всех возможных.

Верните любую такую подпоследовательность в виде массива длины k.

Подпоследовательность - это массив, который получается из другого массива путём удаления некоторых элементов без изменения порядка оставшихся.

Примеры:
Ввод: numbers = [2,1,3,3], k = 2
Вывод: [3,3]

Ввод: numbers = [-1,-2,3,4], k = 3
Вывод: [-1,3,4]
'''

from typing import List

def max_subsequence(numbers: List[int], k: int) -> List[int]:
    indexed_numbers = list(enumerate(numbers))

    sorted_by_value_descending = sorted(indexed_numbers, key=lambda pair: pair[1], reverse=True)
    largest_k_elements_with_indices = sorted_by_value_descending[:k]
    largest_k_elements_sorted_by_index = sorted(largest_k_elements_with_indices, key=lambda pair: pair[0])
    result_subsequence = [value for index, value in largest_k_elements_sorted_by_index]
    return result_subsequence