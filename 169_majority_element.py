'''
Given an integer array numbers of size N, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times in the array.
You can assume that the majority element always exists in the input array.

Examples:
Input: numbers = [3, 2, 3]
Output: 3

Input: numbers = [2, 2, 1, 1, 1, 2, 2]
Output: 2

Дан целочисленный массив numbers размера N. 
Необходимо найти элемент большинства — то есть такой элемент, который встречается в массиве более ⌊n / 2⌋ раз.
Можно считать, что элемент большинства всегда существует во входном массиве.

Примеры:
Вход: numbers = [3, 2, 3]
Выход: 3

Вход: numbers = [2, 2, 1, 1, 1, 2, 2]
Выход: 2
'''

from typing import List

def majority_element(nums: List[int]) -> int:
    candidate = None
    count = 0

    for number in nums:
        if count == 0:
            candidate = number
        count += 1 if number == candidate else -1

    return candidate