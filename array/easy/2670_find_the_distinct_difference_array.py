'''
You are given a 0-indexed integer array numbers of length n.

The distinct difference array of numbers is an array diff of length n, where: diff[i] is equal to the number of distinct elements in the prefix numbers[0 ... i] minus the number of distinct elements in the suffix numbers[i + 1 ... n − 1].

Return the distinct difference array diff.

Examples:
Input: numbers = [1, 2, 3, 4, 5]
Output: [-3, -1, 1, 3, 5]

Input: numbers = [3, 2, 3, 4, 2]
Output: [-2, -1, 0, 2, 3]

Вам дан целочисленный массив с нулевой индексацией numbers длины n.

Массив разности различных элементов - это массив diff длины n, где: diff[i] равен количеству различных элементов в префиксе numbers[0 ... i] минус количество различных элементов в суффиксе numbers[i + 1 ... n − 1].

Верните массив diff.

Примеры:
Ввод: numbers = [1, 2, 3, 4, 5]
Вывод: [-3, -1, 1, 3, 5]

Ввод: numbers = [3, 2, 3, 4, 2]
Вывод: [-2, -1, 0, 2, 3]
'''

from typing import List

def distinct_difference_array(numbers: List[int]) -> List[int]:
    length = len(numbers)

    suffix_distinct_count = [0] * length
    seen_in_suffix = set()

    for index in range(length - 1, -1, -1):
        seen_in_suffix.add(numbers[index])
        suffix_distinct_count[index] = len(seen_in_suffix)

    result = []
    seen_in_prefix = set()

    for index in range(length):
        seen_in_prefix.add(numbers[index])

        distinct_in_prefix = len(seen_in_prefix)
        distinct_in_suffix = (suffix_distinct_count[index + 1] if index + 1 < length else 0)

        result.append(distinct_in_prefix - distinct_in_suffix)

    return result