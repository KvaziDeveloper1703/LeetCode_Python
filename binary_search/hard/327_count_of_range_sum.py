'''
Given an integer array numbers and two integers lower and upper.

Return the number of range sums that lie in the interval [lower, upper].

A range sum S(i, j) is defined as the sum of the elements in numbers between indices i and j inclusive, where i ≤ j.

Examples:
Input: numbers = [-2,5,-1], lower = -2, upper = 2
Output: 3

Input: numbers = [0], lower = 0, upper = 0
Output: 1

Дан массив целых чисел numbers и два целых числа lower и upper. 

Необходимо вернуть количество диапазонных сумм, которые попадают в интервал [lower, upper].

Диапазонная сумма S(i, j) определяется как сумма элементов массива numbers от индекса i до индекса j включительно, где i ≤ j.

Примеры:
Ввод: numbers = [-2,5,-1], lower = -2, upper = 2
Вывод: 3

Ввод: numbers = [0], lower = 0, upper = 0
Вывод: 1
'''

from typing import List

def count_range_sum(numbers: List[int], lower_bound: int, upper_bound: int) -> int:
    prefix_sums_array = [0]

    for number in numbers:
        prefix_sums_array.append(prefix_sums_array[-1] + number)

    def count_range_sums_with_merge_sort(left_index: int, right_index: int) -> int:
        if right_index - left_index <= 1:
            return 0

        middle_index = (left_index + right_index) // 2
        count = (
            count_range_sums_with_merge_sort(left_index, middle_index) +
            count_range_sums_with_merge_sort(middle_index, right_index)
        )
        range_start = range_end = middle_index

        for left_sum in prefix_sums_array[left_index:middle_index]:
            while range_start < right_index and prefix_sums_array[range_start] - left_sum < lower_bound:
                range_start += 1
            while range_end < right_index and prefix_sums_array[range_end] - left_sum <= upper_bound:
                range_end += 1

            count += range_end - range_start

        left_pointer = left_index
        right_pointer = middle_index
        merged_sorted_part = []

        while left_pointer < middle_index and right_pointer < right_index:
            if prefix_sums_array[left_pointer] < prefix_sums_array[right_pointer]:
                merged_sorted_part.append(prefix_sums_array[left_pointer])
                left_pointer += 1
            else:
                merged_sorted_part.append(prefix_sums_array[right_pointer])
                right_pointer += 1

        while left_pointer < middle_index:
            merged_sorted_part.append(prefix_sums_array[left_pointer])
            left_pointer += 1
        while right_pointer < right_index:
            merged_sorted_part.append(prefix_sums_array[right_pointer])
            right_pointer += 1

        prefix_sums_array[left_index:right_index] = merged_sorted_part

        return count

    return count_range_sums_with_merge_sort(0, len(prefix_sums_array))