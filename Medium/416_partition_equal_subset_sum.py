'''
Given an integer array numbers, return true if you can partition the array into two subsets such that the sum of elements in both subsets is equal, or false otherwise.

Examples:
Input: numbers = [1, 5, 11, 5]
Output: true

Input: numbers = [1, 2, 3, 5]
Output: false

Дан массив целых чисел numbers.
Верните true, если массив можно разбить на два подмножества с равной суммой элементов.
Иначе — false.

Примеры:
Вход: numbers = [1, 5, 11, 5]
Выход: true

Вход: numbers = [1, 2, 3, 5]
Выход: false
'''

from typing import List

def can_partition(numbers: List[int]) -> bool:
    total_sum = sum(numbers)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for number in numbers:
        for i in range(target, number - 1, -1):
            dp[i] = dp[i] or dp[i - number]

    return dp[target]