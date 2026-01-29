'''
You are given an integer array numbers and two integers l and r.

Your task is to find a contiguous subarray whose length is between l and r (inclusive), whose sum is greater than 0, and whose sum is as small as possible among all such subarrays.

Return the minimum sum of such a subarray. If no subarray satisfies these conditions, return -1. A subarray is a non-empty contiguous sequence of elements within an array.

Examples:
Input: numbers = [3, -2, 1, 4], l = 2, r = 3
Output: 1

Input: numbers = [-2, 2, -3, 1], l = 2, r = 3
Output: -1

Дан целочисленный массив numbers и два целых числа l и r.

Требуется найти подмассив длиной от l до r включительно, сумма элементов которого строго больше 0, и при этом эта сумма должна быть минимальной среди всех таких подмассивов.

Верните минимальную сумму такого подмассива. Если подходящего подмассива не существует, верните -1. Подмассивом считается непустая непрерывная последовательность элементов массива.

Примеры:
Ввод: numbers = [3, -2, 1, 4], l = 2, r = 3
Вывод: 1

Ввод: numbers = [-2, 2, -3, 1], l = 2, r = 3
Вывод: -1
'''

from typing import List
import bisect

def minimum_sum_subarray(numbers: List[int], l: int, r: int) -> int:
    n = len(numbers)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + numbers[i]

    sorted_prefixes = []
    answer = float('inf')

    for j in range(1, n + 1):
        if j - l >= 0:
            bisect.insort(sorted_prefixes, prefix[j - l])

        if j - r - 1 >= 0:
            index = bisect.bisect_left(sorted_prefixes, prefix[j - r - 1])
            sorted_prefixes.pop(index)

        index = bisect.bisect_left(sorted_prefixes, prefix[j])
        if index > 0:
            candidate = prefix[j] - sorted_prefixes[index - 1]
            if candidate > 0:
                answer = min(answer, candidate)

    return -1 if answer == float('inf') else answer