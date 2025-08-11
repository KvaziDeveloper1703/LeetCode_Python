'''
Given an unsorted array of integers numbers.

Your task is to find the length of the longest continuous increasing subsequence within this array.
A continuous increasing subsequence is a subarray defined by two indices l and r, such that:
    [numbers[l], numbers[l + 1], ..., numbers[r]]
and for each index i in the range l <= i < r, it holds that:
    numbers[i] < numbers[i + 1]

Return the length of the longest such subsequence.

Examples:
Input: numbers = [1,3,5,4,7]
Output: 3

Input: numbers = [2,2,2,2,2]
Output: 1

Дан неотсортированный массив целых чисел numbers.

Необходимо определить длину самой длинной непрерывной возрастающей подпоследовательности в этом массиве.
Непрерывной возрастающей подпоследовательностью называется подмассив, который определяется двумя индексами l и r так, что:
    [numbers[l], numbers[l + 1], ..., numbers[r]]
и для каждого индекса i в диапазоне l <= i < r выполняется:
    numbers[i] < numbers[i + 1]
Необходимо вернуть длину такой самой длинной подпоследовательности.

Примеры:
Ввод: numbers = [1,3,5,4,7]
Вывод: 3

Ввод: numbers = [2,2,2,2,2]
Вывод: 1
'''

from typing import List

def find_length_of_LCIS(numbers: List[int]) -> int:
    if not numbers:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1

    return max_len