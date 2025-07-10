'''
Given an integer array numbers. Return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. A sequence is strictly increasing if each element is strictly greater than the one before it.

Examples:
Input:  numbers = [10,9,2,5,3,7,101,18]
Output: 4

Input:  numbers = [0,1,0,3,2,3]
Output: 4

Дан массив целых чисел numbers. Нужно вернуть длину наибольшей строго возрастающей подпоследовательности.

Подпоследовательность — это последовательность, которую можно получить из массива, удалив некоторые элементы, не меняя порядок остальных элементов. Последовательность называется строго возрастающей, если каждый её следующий элемент больше предыдущего.

Примеры:
Ввод:  numbers = [10,9,2,5,3,7,101,18]
Вывод: 4

Ввод:  numbers = [0,1,0,3,2,3]
Вывод: 4
'''

from typing import List

def length_of_LIS(numbers: List[int]) -> int:
    if not numbers:
        return 0

    length = len(numbers)
    longest_subseq_lengths = [1] * length

        for current_index in range(length):
            for previous_index in range(current_index):
                if nums[previous_index] < nums[current_index]:
                    longest_subseq_lengths[current_index] = max(
                        longest_subseq_lengths[current_index],
                        longest_subseq_lengths[previous_index] + 1
                    )

        return max(longest_subseq_lengths)