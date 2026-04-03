'''
You are given a 0-indexed integer array nums of even length.

While the array is not empty, repeat the following steps:
    - Find and remove the minimum number from nums;
    - Find and remove the maximum number from nums;
    - Calculate the average of the two removed numbers.

Return the number of distinct averages obtained during this process.

Examples:
Input: nums = [4, 1, 4, 0, 3, 5]
Output: 2

Input: nums = [1, 100]
Output: 1

Дан целочисленный массив nums чётной длины.

Пока массив не пуст, необходимо повторять:
    - Найти и удалить минимальный элемент из nums;
    - Найти и удалить максимальный элемент из nums;
    - Вычислить среднее значение этих двух чисел.

Верните количество различных средних значений, полученных в процессе.

Примеры:
Ввод: nums = [4, 1, 4, 0, 3, 5]
Вывод: 2

Ввод: nums = [1, 100]
Вывод: 1
'''

from typing import List

def distinct_averages(nums: List[int]) -> int:
    nums.sort()
    left_index = 0
    right_index = len(nums) - 1
    averages = set()

    while left_index < right_index:
        average = (nums[left_index] + nums[right_index]) / 2
        averages.add(average)
        left_index += 1
        right_index -= 1

    return len(averages)