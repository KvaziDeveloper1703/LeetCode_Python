'''
You are given a 0-indexed integer array numbers.

Determine whether there exist two different subarrays of length 2 such that the sum of their elements is equal.
The two subarrays must start at different indices.

A subarray is a contiguous, non-empty sequence of elements within an array.

Return True if such subarrays exist; otherwise, return False.

Вам дан целочисленный массив с нулевой индексацией numbers.

Необходимо определить, существуют ли два различных подмассива длины 2, у которых суммы элементов равны.
При этом подмассивы должны начинаться с разных индексов.

Подмассив - это непрерывная непустая последовательность элементов массива.

Верните True, если такие подмассивы существуют, и False - в противном случае.
'''

from typing import List

def find_subarrays(numbers: List[int]) -> bool:
    seen_sums = set()

    for index in range(len(numbers) - 1):
        current_sum = numbers[index] + numbers[index + 1]
        if current_sum in seen_sums:
            return True
        seen_sums.add(current_sum)

    return False