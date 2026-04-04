'''
You are given an integer array nums of size n.
For each index i (where 0 ≤ i < n), define a subarray: nums[start ... i] where: start = max(0, i - nums[i]).
For every index i, compute the sum of elements in its corresponding subarray.
Return the total sum of all these subarray sums.

Examples:
Input: nums = [2, 3, 1]
Output: 11

Input: nums = [3, 1, 1, 2]
Output: 13

Дан массив целых чисел nums длины n.
Для каждого индекса i (где 0 ≤ i < n) определяется подмассив: nums[start ... i] где: start = max(0, i - nums[i]).
Для каждого i необходимо вычислить сумму элементов соответствующего подмассива.
Верните сумму всех полученных значений.

Примеры:
Ввод: nums = [2, 3, 1]
Вывод: 11

Ввод: nums = [3, 1, 1, 2]
Вывод: 13
'''

from typing import List

def subarray_sum(nums: List[int]) -> int:
    n = len(nums)
    ans = 0

    for i in range(n):
        start = max(0, i - nums[i])
        for j in range(start, i + 1):
            ans += nums[j]

    return ans