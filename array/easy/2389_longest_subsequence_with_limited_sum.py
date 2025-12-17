'''
You are given an integer array numbers of length n and an integer array queries of length m.

For each query queries[i], determine the maximum possible size of a subsequence that can be formed from numbers such that the sum of its elements is less than or equal to queries[i].

A subsequence is obtained from an array by removing some (or none) of its elements without changing the order of the remaining elements.

Return an array answer of length m, where answer[i] corresponds to the result for the i-th query.

Вам дан целочисленный массив numbers длины n и целочисленный массив queries длины m.

Для каждого запроса queries[i] необходимо определить максимально возможный размер подпоследовательности, которую можно выбрать из массива numbers, так чтобы сумма её элементов была меньше либо равна queries[i].

Подпоследовательность - это массив, полученный из другого массива путём удаления некоторых (или ни одного) элементов без изменения порядка оставшихся элементов.

Верните массив answer длины m, где answer[i] - результат для i-го запроса.
'''

from typing import List

def answer_queries(numbers: List[int], queries: List[int]) -> List[int]:
    sorted_numbers = sorted(numbers)
    prefix_sums = []

    current_sum = 0
    for number in sorted_numbers:
        current_sum += number
        prefix_sums.append(current_sum)

    answers = []
    for query in queries:
        left_index = 0
        right_index = len(prefix_sums)

        while left_index < right_index:
            middle_index = (left_index + right_index) // 2
            if prefix_sums[middle_index] <= query:
                left_index = middle_index + 1
            else:
                right_index = middle_index

        answers.append(left_index)

    return answers