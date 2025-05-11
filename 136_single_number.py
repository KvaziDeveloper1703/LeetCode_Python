'''
Given a non-empty array of integers numbers, every element appears exactly twice except for one element that appears only once. Find and return that single one.
You must implement a solution with linear time complexity (O(n)) and use only constant extra space (O(1)).

Examples:
Input: numbers = [2, 2, 1]
Output: 1

Input: numbers = [4, 1, 2, 1, 2]
Output: 4

Дан непустой массив целых чисел numbers. Каждый элемент встречается ровно дважды, кроме одного, который встречается один раз. Найдите и верните этот единственный элемент.
Решение должно иметь линейную сложность (O(n)) и использовать только постоянное количество дополнительной памяти (O(1)).

Примеры:
Вход: numbers = [2, 2, 1]
Выход: 1

Вход: numbers = [4, 1, 2, 1, 2]
Выход: 4
'''

from typing import List

def single_number(self, numbers: List[int]) -> int:
    result = 0
    for number in numbers:
        result ^= number
    return result