'''
Given an integer array numbers where every element appears exactly three times except for one element which appears exactly once, find and return that single one.
You must implement a solution with linear runtime complexity (O(n)) and use only constant extra space (O(1)).

Examples:
Input: numbers = [2, 2, 3, 2]
Output: 3

Input: numbers = [0, 1, 0, 1, 0, 1, 99]
Output: 99

Дан массив целых чисел numbers, в котором каждый элемент встречается ровно три раза, кроме одного, который встречается один раз. Найдите и верните этот единственный элемент.
Решение должно иметь линейную временную сложность (O(n)) и использовать только постоянное количество дополнительной памяти (O(1)).

Примеры:
Ввод: numbers = [2, 2, 3, 2]
Вывод: 3

Ввод: numbers = [0, 1, 0, 1, 0, 1, 99]
Вывод: 99
'''

from typing import List

def single_number(numbers: List[int]) -> int:
    ones, twos = 0, 0
    for number in numbers:
        ones = (ones ^ number) & ~twos
        twos = (twos ^ number) & ~ones
    return ones