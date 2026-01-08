'''
You are given a 0-indexed array numbers consisting of positive integers.
A subarray of numbers is called incremovable if, after removing this subarray from numbers, the remaining elements form a strictly increasing array.
For example, the subarray [3, 4] is an incremovable subarray of [5, 3, 4, 6, 7] because removing [3, 4] results in the array [5, 6, 7], which is strictly increasing.
Your task is to count the total number of incremovable subarrays of numbers.
Return the total number of incremovable subarrays.

Examples:
Input:  numbers = [1, 2, 3, 4]
Output: 10

Input:  numbers = [6, 5, 7, 8]
Output: 7

Дан массив положительных целых чисел numbers с нумерацией элементов с нуля.
Подмассив массива numbers называется incremovable, если после его удаления из массива numbers оставшиеся элементы образуют строго возрастающий массив.
Например, подмассив [3, 4] является incremovable для массива [5, 3, 4, 6, 7], так как после его удаления получается массив [5, 6, 7], который является строго возрастающим.
Необходимо подсчитать общее количество incremovable-подмассивов массива numbers.
Верните количество incremovable-подмассивов.

Примеры:
Ввод:  numbers = [1, 2, 3, 4]
Вывод: 10

Ввод:  numbers = [6, 5, 7, 8]
Вывод: 7
'''

from typing import List

def incremovable_subarray_count(numbers: List[int]) -> int:
    length = len(numbers)

    increasing_prefix_end = 0
    while (increasing_prefix_end + 1 < length and numbers[increasing_prefix_end] < numbers[increasing_prefix_end + 1]):
        increasing_prefix_end += 1

    if increasing_prefix_end == length - 1:
        return length * (length + 1) // 2

    increasing_suffix_start = length - 1
    while (increasing_suffix_start - 1 >= 0 and numbers[increasing_suffix_start - 1] < numbers[increasing_suffix_start]):
        increasing_suffix_start -= 1

    result = 0
    right_start_index = increasing_suffix_start

    for left_start_index in range(increasing_prefix_end + 2):
        if left_start_index == 0:
            first_allowed_right_start = max(1, increasing_suffix_start)
            result += length - first_allowed_right_start + 1
        else:
            right_start_index = max(right_start_index, increasing_suffix_start, left_start_index + 1)
            while (right_start_index < length and numbers[right_start_index] <= numbers[left_start_index - 1]):
                right_start_index += 1
            result += length - right_start_index + 1

    return result