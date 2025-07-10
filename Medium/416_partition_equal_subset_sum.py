'''
Given an integer array numbers, return True if you can partition the array into two subsets such that the sum of elements in both subsets is equal, or False otherwise.

Examples:
Input: numbers = [1, 5, 11, 5]
Output: True

Input: numbers = [1, 2, 3, 5]
Output: False

Дан массив целых чисел numbers. Верните True, если массив можно разбить на два подмножества с равной суммой элементов. Иначе — False.

Примеры:
Ввод: numbers = [1, 5, 11, 5]
Вывод: True

Ввод: numbers = [1, 2, 3, 5]
Вывод: False
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