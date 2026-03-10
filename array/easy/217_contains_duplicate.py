'''
Given an integer array nums, determine whether the array contains any duplicate values.
Return true if at least one number appears two or more times in the array. Return false if all elements in the array are distinct.

Examples:
Input: nums = [1, 2, 3, 1]
Output: true

Input: nums = [1, 2, 3, 4]
Output: false

Дан массив целых чисел nums. Необходимо определить, есть ли в массиве повторяющиеся значения.
Верните true, если хотя бы одно число встречается два или более раз. Верните false, если все элементы массива различны.

Примеры:
Ввод: nums = [1, 2, 3, 1]
Вывод: true

Ввод: nums = [1, 2, 3, 4]
Вывод: false
'''
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False