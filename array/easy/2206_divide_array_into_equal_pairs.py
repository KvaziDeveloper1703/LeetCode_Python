'''
You are given an integer array numbers containing 2 * n elements.

Your task is to divide numbers into n pairs such that:
    - Each element is included in exactly one pair;
    - The two elements in each pair are equal.

Return True if it is possible to divide the array into n such pairs; otherwise, return False.

Examples:
Input: numbers = [3,2,3,2,2,2]
Output: True

Input: numbers = [1,2,3,4]
Output: False

Дан массив целых чисел numbers, содержащий 2 * n элементов.

Необходимо разделить массив на n пар так, чтобы:
    - Каждый элемент входил ровно в одну пару;
    - Элементы внутри каждой пары были равны.

Верните True, если такое разбиение возможно; иначе верните False.

Примеры:
Ввод: numbers = [3,2,3,2,2,2]
Вывод: True

Ввод: numbers = [1,2,3,4]
Вывод: False
'''

from typing import List
from collections import Counter

def divide_array(numbers: List[int]) -> bool:
    frequency = Counter(numbers)

    for number, count in frequency.items():
        if count % 2 != 0:
            return False

    return True