'''
Given an integer array numbers, return the maximum difference between two successive elements in its sorted form.
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time (O(n)) and uses linear extra space (O(n)).

Examples:
Input: numbers = [3,6,9,1]
Output: 3

Input: numbers = [10]
Output: 0

Дан массив целых чисел numbers. Верните максимальную разницу между двумя соседними элементами в отсортированной версии этого массива.
Если в массиве меньше двух элементов, верните 0.

Необходимо реализовать алгоритм с линейной сложностью по времени (O(n)) и линейной дополнительной памятью (O(n)).

Примеры:
Ввод: numbers = [3,6,9,1]
Вывод: 3

Ввод: numbers = [10]
Вывод: 0
'''

from typing import List

def maximum_gap(numbers: List[int]) -> int:
    if len(numbers) < 2:
        return 0
    min_value, max_value = min(numbers), max(numbers)
    if min_value == max_value:
        return 0
    N = len(numbers)
    bucket_size = max(1, (max_value - min_value) // (N - 1))
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets_min = [float('inf')] * bucket_count
    buckets_max = [float('-inf')] * bucket_count
    for number in numbers:
        idx = (number - min_value) // bucket_size
        buckets_min[idx] = min(buckets_min[idx], number)
        buckets_max[idx] = max(buckets_max[idx], number)
    max_gap = 0
    previous_max = min_value
    for i in range(bucket_count):
        if buckets_min[i] == float('inf'):
            continue
        max_gap = max(max_gap, buckets_min[i] - previous_max)
        previous_max = buckets_max[i]
    return max_gap