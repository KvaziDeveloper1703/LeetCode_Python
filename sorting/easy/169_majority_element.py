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
Ввод: numbers = [3, 2, 3]
Вывод: 3

Ввод: numbers = [2, 2, 1, 1, 1, 2, 2]
Вывод: 2
'''

from typing import List

def majority_element(numbers: List[int]) -> int:
    candidate = None
    count = 0

    for number in numbers:
        if count == 0:
            candidate = number
        count += 1 if number == candidate else -1

    return candidate