'''
You are given an integer array nums of length n, where each element nums[i] is in the range [1, n].
Return an array containing all the integers in the range [1, n] that do not appear in nums.
The order of the returned numbers does not matter.

Examples:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Input: nums = [1,1]
Output: [2]

Дан массив целых чисел nums длины n, где каждый элемент nums[i] находится в диапазоне [1, n].
Необходимо вернуть массив всех чисел из диапазона [1, n], которые не встречаются в массиве nums.
Порядок элементов в результате не имеет значения.

Примеры:
Ввод: nums = [4,3,2,7,8,2,3,1]
Вывод: [5,6]

Ввод: nums = [1,1]
Вывод: [2]
'''

from typing import List

def find_disappeared_numbers(nums: List[int]) -> List[int]:
    n = len(nums)
    seen = set(nums)

    result = []
    for i in range(1, n + 1):
        if i not in seen:
            result.append(i)

    return result