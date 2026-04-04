'''
You are given an array of positive integers nums.
An array arr is called product equivalent if: prod(arr) == gcd(arr) * lcm(arr).

Where:
    - prod(arr) is the product of all elements in the array;
    - gcd(arr) is the greatest common divisor of all elements;
    - lcm(arr) is the least common multiple of all elements.

Return the length of the longest contiguous subarray of nums that is product equivalent.

Examples:
Input: nums = [1,2,1,2,1,1,1]
Output: 5

Input: nums = [2,3,4,5,6]
Output: 3

Дан массив положительных целых чисел nums.
Массив arr называется product equivalent, если выполняется условие: prod(arr) == gcd(arr) * lcm(arr).

Где:
    - prod(arr) - произведение всех элементов массива;
    - gcd(arr) - наибольший общий делитель всех элементов;
    - lcm(arr) - наименьшее общее кратное всех элементов.

Необходимо вернуть длину самого длинного непрерывного подмассива nums, который является product equivalent.

Примеры:
Ввод: nums = [1,2,1,2,1,1,1]
Вывод: 5

Ввод: nums = [2,3,4,5,6]
Вывод: 3
'''

from math import gcd
from typing import List

def max_length(nums: List[int]) -> int:
    def lcm(a, b):
        return a * b // gcd(a, b)

    n = len(nums)
    ans = 1

    for i in range(n):
        cur_gcd = nums[i]
        cur_lcm = nums[i]
        cur_prod = nums[i]

        for j in range(i, n):
            if j > i:
                cur_gcd = gcd(cur_gcd, nums[j])
                cur_lcm = lcm(cur_lcm, nums[j])
                cur_prod *= nums[j]

            if cur_prod == cur_gcd * cur_lcm:
                ans = max(ans, j - i + 1)

    return ans