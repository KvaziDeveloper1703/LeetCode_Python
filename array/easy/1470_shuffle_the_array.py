'''
You are given an array nums consisting of 2n elements in the form: [x1, x2, ..., xn, y1, y2, ..., yn].
Return the array rearranged in the form: [x1, y1, x2, y2, ..., xn, yn].

Examples:
Input: nums = [2, 5, 1, 3, 4, 7], n = 3
Output: [2, 3, 5, 4, 1, 7]

Input: nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4
Output: [1, 4, 2, 3, 3, 2, 4, 1]

Дан массив nums, состоящий из 2n элементов в виде: [x1, x2, ..., xn, y1, y2, ..., yn].
Необходимо вернуть массив, преобразованный в вид: [x1, y1, x2, y2, ..., xn, yn].

Примеры:
Ввод: nums = [2, 5, 1, 3, 4, 7], n = 3
Вывод: [2, 3, 5, 4, 1, 7]

Ввод: nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4
Вывод: [1, 4, 2, 3, 3, 2, 4, 1]
'''

from typing import List

def shuffle(nums: List[int], n: int) -> List[int]:
    result = []

    for index in range(n):
        result.append(nums[index])
        result.append(nums[index + n])

    return result