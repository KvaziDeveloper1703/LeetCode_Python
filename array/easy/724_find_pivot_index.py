'''
Given an array of integers numbers.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the right of the index.
    + If the index is at the left edge of the array, the left sum is considered to be 0;
    + Similarly, if the index is at the right edge, the right sum is 0.

Return the leftmost pivot index. If no such index exists, return -1.

Examples:
Input: numbers = [1, 7, 3, 6, 5, 6]
Output: 3

Input: numbers = [1, 2, 3]
Output: -1

Дан массив целых чисел numbers.

Опорный индекс — это такой индекс, для которого сумма всех элементов строго левее равна сумме всех элементов строго правее.
    + Если индекс находится на левом краю массива, сумма слева считается равной 0;
    + Если индекс находится на правом краю, сумма справа также считается равной 0.

Нужно вернуть первый подходящий индекс. Если такого индекса нет — вернуть -1.

Примеры:
Ввод: numbers = [1, 7, 3, 6, 5, 6]
Вывод: 3

Ввод: numbers = [1, 2, 3]
Вывод: -1
'''

from typing import List

def pivotIndex(numbers: List[int]) -> int:
    total = sum(numbers)
    left_sum = 0

    for i, number in enumerate(numbers):
        right_sum = total - left_sum - number
        if left_sum == right_sum:
            return i
        left_sum += number

    return -1