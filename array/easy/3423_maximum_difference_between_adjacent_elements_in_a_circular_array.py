'''
You are given a circular array nums.
Find the maximum absolute difference between any two adjacent elements.
Return the maximum absolute difference.

Examples:
Input: nums = [1, 2, 4]
Output: 3

Input: nums = [-5, -10, -5]
Output: 5

Дан циклический массив nums.
Необходимо найти максимальную абсолютную разницу между соседними элементами.
Верните максимальную абсолютную разницу.

Примеры:
Ввод: nums = [1, 2, 4]
Вывод: 3

Ввод: nums = [-5, -10, -5]
Вывод: 5
'''

from typing import List

def max_adjacent_distance(nums: List[int]) -> int:
    n = len(nums)
    ans = 0

    for i in range(n):
        diff = abs(nums[i] - nums[(i + 1) % n])
        ans = max(ans, diff)

    return ans